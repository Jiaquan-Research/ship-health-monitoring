# Industrial Dataset Zoo Inventory

Date: 2026-06-10

Status: Data collection inventory only.

Scope: No preprocessing, no analysis, no experiments, no conclusions, no claim upgrades.

Raw data policy: raw datasets are stored under `data/` and remain ignored by Git. This inventory is the only file committed for this collection task.

---

## Collection Summary

| Priority | Dataset | Domain | Source URL | Local status | Approximate size | File format | Short notes | Possible operating regimes (observation only) |
|---|---|---|---|---|---:|---|---|---|
| P0 | ZEMA Hydraulic System Condition Monitoring Dataset | Hydraulic test rig / industrial condition monitoring | https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems | Downloaded to `data/hydraulic/condition_monitoring_of_hydraulic_systems.zip` | 76.6 MB | ZIP containing original `.txt` channels plus `description.txt`, `documentation.txt`, and `profile.txt` | Original archive preserved unchanged. | Pressure regime, cooler/valve/accumulator/pump condition states, load-cycle profile. |
| P1 | NASA C-MAPSS Turbofan Engine Degradation Simulation Dataset | Aero-engine simulation / RUL benchmark | https://phm-datasets.s3.amazonaws.com/NASA/6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip | Downloaded to `data/cmapss/6_Turbofan_Engine_Degradation_Simulation_Data_Set.zip` | 12.4 MB | ZIP containing original nested `CMAPSSData.zip`; inner archive contains FD001, FD002, FD003, FD004 train/test/RUL `.txt`, `readme.txt`, and PDF | Original archive preserved unchanged. FD001-FD004 are present inside the nested NASA archive. | Single-condition and multi-condition simulated operating regimes; single-fault and multi-fault subsets. |
| P2 | Paderborn Bearing Dataset | Bearing fault diagnosis / rotating machinery | https://groups.uni-paderborn.de/kat/BearingDataCenter/ | Downloaded to `data/bearing/paderborn/` | 5.1 GB | Original `.rar` archives plus `readme_versions.txt` | Original archives preserved unchanged. Downloaded 32 condition archives (`K*`, `KA*`, `KB*`, `KI*`) and README metadata. | Speed regime, load torque regime, healthy/artificial damage/real damage bearing conditions. |
| P3 | FEMTO Bearing Dataset / IEEE PHM 2012 Challenge / PRONOSTIA | Bearing run-to-failure / PHM challenge | https://www.femto-st.fr/en/Research-departments/AS2M/Research-groups/PHM/IEEE-PHM-2012-Data-challenge.php | Source identified; automatic download not completed in this session | Not recorded locally | Original challenge archives not retrieved | FEMTO page redirects to DATA-PHM team page and did not expose stable direct archive links through static retrieval. Keep as future manual/portal collection item. | Speed regime, load regime, run-to-failure lifecycle regime. |
| P4 | XJTU-SY Bearing Dataset | Bearing accelerated degradation / rotating machinery | https://biaowang.tech/xjtu-sy-bearing-datasets/ | Source identified; automatic download not completed in this session | Not recorded locally | Cloud-mirror archives not retrieved | Source page exposes Google Drive, Dropbox, MediaFire, MEGA, and Baidu mirrors. No raw files were downloaded automatically to avoid unstable interactive/cloud-folder behavior. | Speed regime, load regime, bearing lifecycle regime. |

---

## Downloaded Raw Files

### ZEMA Hydraulic

Local path:

`data/hydraulic/condition_monitoring_of_hydraulic_systems.zip`

Archive validation:

- ZIP archive present.
- Contains original channel text files.
- Contains original documentation/metadata files.

Observed archive members include:

- `CE.txt`
- `CP.txt`
- `description.txt`
- `EPS1.txt`
- `FS1.txt`
- `FS2.txt`
- `profile.txt`
- `PS1.txt` through `PS6.txt`
- `SE.txt`
- `TS1.txt` through `TS4.txt`
- `VS1.txt`
- `documentation.txt`

### NASA C-MAPSS

Local path:

`data/cmapss/6_Turbofan_Engine_Degradation_Simulation_Data_Set.zip`

Archive validation:

- Outer ZIP archive present.
- Contains original nested `CMAPSSData.zip`.
- Inner archive contains FD001-FD004 files.

Observed inner archive members:

- `Damage Propagation Modeling.pdf`
- `readme.txt`
- `RUL_FD001.txt`
- `RUL_FD002.txt`
- `RUL_FD003.txt`
- `RUL_FD004.txt`
- `test_FD001.txt`
- `test_FD002.txt`
- `test_FD003.txt`
- `test_FD004.txt`
- `train_FD001.txt`
- `train_FD002.txt`
- `train_FD003.txt`
- `train_FD004.txt`

### Paderborn Bearing

Local path:

`data/bearing/paderborn/`

Downloaded original files:

- `K001.rar`
- `K002.rar`
- `K003.rar`
- `K004.rar`
- `K005.rar`
- `K006.rar`
- `KA01.rar`
- `KA03.rar`
- `KA04.rar`
- `KA05.rar`
- `KA06.rar`
- `KA07.rar`
- `KA08.rar`
- `KA09.rar`
- `KA15.rar`
- `KA16.rar`
- `KA22.rar`
- `KA30.rar`
- `KB23.rar`
- `KB24.rar`
- `KB27.rar`
- `KI01.rar`
- `KI03.rar`
- `KI04.rar`
- `KI05.rar`
- `KI07.rar`
- `KI08.rar`
- `KI14.rar`
- `KI16.rar`
- `KI17.rar`
- `KI18.rar`
- `KI21.rar`
- `readme_versions.txt`

---

## Source-Identified Datasets Not Automatically Retrieved

### FEMTO / PRONOSTIA / IEEE PHM 2012

Source checked:

`https://www.femto-st.fr/en/Research-departments/AS2M/Research-groups/PHM/IEEE-PHM-2012-Data-challenge.php`

Collection status:

- Source page was reachable.
- It redirected to the FEMTO-ST DATA-PHM team page.
- Static page retrieval did not expose direct archive URLs.
- No raw FEMTO files were added.

### XJTU-SY Bearing

Source checked:

`https://biaowang.tech/xjtu-sy-bearing-datasets/`

Collection status:

- Source page was reachable.
- The page exposes cloud mirror links.
- Raw files were not downloaded automatically from the cloud mirrors in this session.
- No raw XJTU-SY files were added.

---

## Regime Notes

These regime descriptions are working observations only.

They are not hypotheses.

They are not conclusions.

They are not evidence.

| Dataset family | Possible operating regimes (observation only) |
|---|---|
| Hydraulic | Pressure regime, valve states, load-cycle profile, cooler/pump/accumulator condition states. |
| C-MAPSS | Single condition, multi-condition, single-fault and multi-fault simulated subsets. |
| Bearing | Speed regime, load regime, defect type, run-to-failure lifecycle regime. |
| Battery | Temperature regime, charge/discharge profile, aging-cycle regime. |
| HVAC | Seasonal regime, load regime, setpoint regime. |
| N-CMAPSS | Flight regime, unit lifecycle regime, degradation-label regime. |

---

## Git Handling

Raw datasets remain under `data/`.

`data/` is ignored by Git.

No raw dataset files are staged or committed.

Only this inventory is committed.

