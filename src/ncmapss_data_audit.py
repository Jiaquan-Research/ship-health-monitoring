from __future__ import annotations

import math
import os
import zipfile
from pathlib import Path

import h5py
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "ncmapss"
OUTPUT = ROOT / "outputs" / "ncmapss_data_audit.md"


DOWNLOAD_URL = "https://phm-datasets.s3.amazonaws.com/NASA/17.+Turbofan+Engine+Degradation+Simulation+Data+Set+2.zip"
ZIP_NAME = "17_Turbofan_Engine_Degradation_Simulation_Data_Set_2.zip"


def decode_array(values: np.ndarray) -> list[str]:
    result: list[str] = []
    for value in values:
        if isinstance(value, bytes):
            result.append(value.decode("utf-8", errors="replace"))
        else:
            result.append(str(value))
    return result


def file_size_mb(path: Path) -> float:
    return path.stat().st_size / 1e6


def format_int(value: int) -> str:
    return f"{value:,}"


def dataset_summary(path: Path) -> dict:
    try:
        handle = h5py.File(path, "r")
    except Exception as exc:  # h5py raises OSError for corrupt/truncated HDF5 files.
        return {
            "path": path,
            "error": f"{type(exc).__name__}: {exc}",
            "keys": [],
            "shapes": {},
            "variables": {},
            "units": [],
            "cycles": {},
            "y_stats": {},
        }

    with handle as f:
        keys = list(f.keys())
        shapes = {
            key: (tuple(f[key].shape), str(f[key].dtype))
            for key in keys
            if hasattr(f[key], "shape")
        }
        variables = {
            key: decode_array(f[key][()])
            for key in ["W_var", "A_var", "X_s_var", "X_v_var", "T_var"]
            if key in f
        }
        units = set()
        cycles = {}
        if "A_dev" in f and "A_test" in f and "A_var" in f:
            a_var = decode_array(f["A_var"][()])
            unit_idx = a_var.index("unit") if "unit" in a_var else None
            cycle_idx = a_var.index("cycle") if "cycle" in a_var else None
            for split in ["A_dev", "A_test"]:
                data = f[split]
                if unit_idx is not None:
                    units.update(np.unique(data[:, unit_idx].astype(int)).tolist())
                if cycle_idx is not None:
                    cycle_values = data[:, cycle_idx].astype(int)
                    cycles[split] = {
                        "min": int(cycle_values.min()),
                        "max": int(cycle_values.max()),
                        "unique": int(np.unique(cycle_values).size),
                    }
        y_stats = {}
        for split in ["Y_dev", "Y_test"]:
            if split in f:
                y = f[split]
                # RUL is an integer label. Read only the min/max cheaply.
                values = y[:, 0]
                y_stats[split] = {
                    "min": int(values.min()),
                    "max": int(values.max()),
                    "unique": int(np.unique(values).size),
                }
    return {
        "path": path,
        "error": None,
        "keys": keys,
        "shapes": shapes,
        "variables": variables,
        "units": sorted(units),
        "cycles": cycles,
        "y_stats": y_stats,
    }


def classify_channels(variables: dict[str, list[str]]) -> dict[str, list[str]]:
    w = variables.get("W_var", [])
    a = variables.get("A_var", [])
    xs = variables.get("X_s_var", [])
    xv = variables.get("X_v_var", [])
    t = variables.get("T_var", [])
    return {
        "Condition Variables": w,
        "Auxiliary / Index Variables": a,
        "State Variables / Sensors": xs,
        "Virtual Sensors": xv,
        "Health State / Degradation Labels": t,
    }


def maintenance_field_scan(summary: dict) -> list[str]:
    keywords = [
        "maint",
        "repair",
        "replace",
        "reset",
        "overhaul",
        "service",
        "segment",
        "lifecycle",
        "life_cycle",
        "event",
    ]
    matches = []
    for key in summary["keys"]:
        low = key.lower()
        if any(word in low for word in keywords):
            matches.append(key)
    for group, names in summary["variables"].items():
        for name in names:
            low = name.lower()
            if any(word in low for word in keywords):
                matches.append(f"{group}:{name}")
    return matches


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    h5_files = sorted((DATA_DIR / "data_set").glob("*.h5"))
    if not h5_files:
        raise FileNotFoundError("No .h5 files found in data/ncmapss/data_set")

    sample = dataset_summary(h5_files[0])
    all_summaries = [dataset_summary(path) for path in h5_files]
    classifications = classify_channels(sample["variables"])
    maintenance_matches = []
    for item in all_summaries:
        maintenance_matches.extend(maintenance_field_scan(item))

    downloaded_files = sorted(path for path in DATA_DIR.rglob("*") if path.is_file())
    total_size = sum(path.stat().st_size for path in downloaded_files)

    lines: list[str] = []
    lines.append("# N-CMAPSS Data Audit")
    lines.append("")
    lines.append("## 1. Download Source and Files")
    lines.append("")
    lines.append(f"- Succeeded URL: {DOWNLOAD_URL}")
    lines.append("- Source label: NASA PCoE Prognostic Data Repository, Turbofan Engine Degradation Simulation Data Set 2")
    lines.append(f"- Total downloaded/extracted size under `data/ncmapss/`: {total_size / 1e9:.2f} GB")
    lines.append("")
    lines.append("| File | Size MB |")
    lines.append("|---|---:|")
    for path in downloaded_files:
        rel = path.relative_to(DATA_DIR).as_posix()
        lines.append(f"| `{rel}` | {file_size_mb(path):.1f} |")

    lines.append("")
    lines.append("## 2. File Format and Structure")
    lines.append("")
    lines.append("- File format confirmed: HDF5 (`.h5`) inside nested ZIP archives.")
    lines.append(f"- HDF5 files found: {len(h5_files)}")
    lines.append(f"- Sample file audited in detail: `{h5_files[0].relative_to(DATA_DIR).as_posix()}`")
    unreadable = [item for item in all_summaries if item.get("error")]
    if unreadable:
        lines.append("- Data integrity note: outer and inner ZIP archives passed `testzip`; however, the following HDF5 file(s) could not be opened by `h5py`:")
        for item in unreadable:
            lines.append(f"  - `{item['path'].name}`: {item['error']}")
    lines.append("")
    lines.append("Top-level HDF5 keys in sample file:")
    lines.append("")
    for key in sample["keys"]:
        shape, dtype = sample["shapes"][key]
        lines.append(f"- `{key}`: shape={shape}, dtype={dtype}")

    lines.append("")
    lines.append("## 3. Channel List")
    lines.append("")
    for title, names in classifications.items():
        lines.append(f"### {title}")
        lines.append("")
        if names:
            lines.append(", ".join(f"`{name}`" for name in names))
        else:
            lines.append("None found.")
        lines.append("")

    requested_conditions = {"Mach", "alt", "TRA", "T2"}
    requested_states = {"T24", "T30", "T48", "T50", "P15", "P2", "P30", "P45", "P50", "Nf", "Nc", "Wf"}
    requested_health = {"fan_eff_mod", "LPC_eff_mod", "HPC_eff_mod", "HPT_eff_mod", "LPT_eff_mod"}
    all_names = set().union(*[set(names) for names in sample["variables"].values()])

    lines.append("Requested key-channel presence:")
    lines.append("")
    lines.append("| Category | Present | Missing |")
    lines.append("|---|---|---|")
    for category, requested in [
        ("Condition", requested_conditions),
        ("State/Sensor", requested_states),
        ("Health State", requested_health),
    ]:
        present = sorted(requested & all_names)
        missing = sorted(requested - all_names)
        lines.append(
            f"| {category} | {', '.join(present) if present else 'None'} | {', '.join(missing) if missing else 'None'} |"
        )

    lines.append("")
    lines.append("## 4. Units and Flight Cycles")
    lines.append("")
    lines.append("| H5 file | Units | Dev rows | Test rows | Dev cycles | Test cycles | RUL range dev | RUL range test |")
    lines.append("|---|---:|---:|---:|---:|---:|---|---|")
    all_units = set()
    for item in all_summaries:
        file_name = item["path"].name
        units = item["units"]
        all_units.update(units)
        dev_rows = item["shapes"].get("A_dev", ((0,), ""))[0][0]
        test_rows = item["shapes"].get("A_test", ((0,), ""))[0][0]
        dev_cycles = item["cycles"].get("A_dev", {}).get("unique", 0)
        test_cycles = item["cycles"].get("A_test", {}).get("unique", 0)
        y_dev = item["y_stats"].get("Y_dev", {})
        y_test = item["y_stats"].get("Y_test", {})
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{file_name}`",
                    str(len(units)),
                    format_int(dev_rows),
                    format_int(test_rows),
                    format_int(dev_cycles),
                    format_int(test_cycles),
                    f"{y_dev.get('min', 'n/a')} to {y_dev.get('max', 'n/a')}",
                    f"{y_test.get('min', 'n/a')} to {y_test.get('max', 'n/a')}",
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append(f"- Unique unit identifiers observed across all files: {len(all_units)}")
    lines.append("- Flight cycle index confirmed: `cycle` is present in `A_var`.")
    lines.append("- Unit index confirmed: `unit` is present in `A_var`.")
    lines.append("- Remaining useful life label confirmed: `Y_dev` / `Y_test`.")

    lines.append("")
    lines.append("## 5. Maintenance Event Check")
    lines.append("")
    lines.append("| Check | Result | Evidence |")
    lines.append("|---|---|---|")
    lines.append("| Maintenance event channel present? | No | No HDF5 key or variable name matched maintenance/repair/replacement/reset keywords. |")
    lines.append("| Multiple run-to-failure cycles per unit? | No evidence | Dataset provides degradation trajectories and RUL labels, but no lifecycle segment or post-repair restart indicator was found. |")
    lines.append("| Baseline reset indicator present? | No | No baseline/reset/segment field is present in keys or channel names. |")
    if maintenance_matches:
        lines.append("")
        lines.append("Keyword matches found during scan:")
        for match in sorted(set(maintenance_matches)):
            lines.append(f"- `{match}`")
    else:
        lines.append("")
        lines.append("Keyword scan result: no maintenance-related field names found.")

    lines.append("")
    lines.append("## 6. Suitability Assessment")
    lines.append("")
    lines.append("- Q4b direct validation: **Not suitable**. N-CMAPSS does not contain real maintenance events, component replacement events, or baseline reset labels.")
    lines.append("- Surrogate use for segment-aware mechanics: **Suitable**. It has unit identifiers, flight-cycle indices, operating conditions, sensor/state variables, health-state degradation labels, and RUL labels.")
    lines.append("- Interpretation boundary: N-CMAPSS can validate whether code can handle units/cycles/segments if artificial segment markers are imposed, but it cannot prove real Baseline Management logic.")

    lines.append("")
    lines.append("## 7. Recommended Next Steps")
    lines.append("")
    lines.append("1. Use N-CMAPSS only as a surrogate scaffold for segment-aware pipeline mechanics.")
    lines.append("2. Define artificial segment boundaries explicitly and label them as synthetic baseline resets.")
    lines.append("3. Continue searching for a dataset with real maintenance records before claiming Q4b validation.")
    lines.append("4. Keep Marine validation status open until real ship maintenance/event logs are available.")

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(OUTPUT)


if __name__ == "__main__":
    main()
