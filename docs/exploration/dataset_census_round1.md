# Dataset Census Round 1

Date: 2026-06-11

Protocol: `docs/exploration/dataset_audit_v0.1.md`

Status: Observation only.

This document is NOT:

- validation
- evidence generation
- support for Q0
- dataset ranking
- dataset comparison

No analysis.

No experiments.

No conclusions.

---

## Summary Table

| Dataset | Source | Domain | Approximate Size | File Format | Number of Files | Number of Variables | Sequence Length | Sampling Information | Current Status | Natural Regimes (only if obvious) | Notes |
|---|---|---|---:|---|---:|---|---|---|---|---|---|
| NASA Battery Dataset | https://data.nasa.gov/dataset/li-ion-battery-aging-datasets | Lithium-ion batteries | 209.7 MB | ZIP containing nested ZIP archives and `.mat` files | 1 outer ZIP; 6 nested ZIPs; 38 `.mat` files visible inside nested archives; README files present | MATLAB structures; visible README fields include cycle type, ambient temperature, voltage, current, temperature, capacity, impedance fields | Varies by battery/cycle; not counted in this census | Charge, discharge, and impedance operations; some README files state room temperature, 24 deg C, or 4 deg C | Downloaded | temperature; charge/discharge/impedance profile; cutoff-voltage/current profile | Original archive preserved under `data/battery/nasa_li_ion/`. |
| Oxford Battery Degradation Dataset 1 | https://ora.ox.ac.uk/objects/uuid:03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac | Lithium-ion batteries | 266.2 MB main `.mat`; 0.07 MB example `.mat`; README 5.6 KB | `.mat`, `.txt` | 3 local files | Main file contains 8 cell structs; README lists time, voltage, charge, temperature, and current for example discharge | Characterisation every 100 cycles; exact series lengths not counted in this census | README states 40 deg C chamber; CC-CV charge and drive-cycle discharge | Downloaded | temperature; charge/discharge profile; drive-cycle discharge; characterisation interval | Original files preserved under `data/battery/oxford/`. |
| ZEMA Hydraulic System Condition Monitoring Dataset | https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems | Hydraulic systems | 76.6 MB | ZIP containing `.txt` channels and documentation | 20 archive members | 17 signal/profile text files plus documentation; row widths vary by sensor file | 2205 rows for main signal/profile files | Direct sampling rates are in documentation; not parsed beyond archive-level census | Downloaded | pressure region; valve/cooler/pump/accumulator states visible through profile file | Original archive preserved under `data/hydraulic/`. |
| C-MAPSS FD001 | https://phm-datasets.s3.amazonaws.com/NASA/6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip | Aero engine simulation | 5.74 MB inside nested C-MAPSS archive | `.txt` | 3 files (`train`, `test`, `RUL`) | 26 columns in train/test rows | train 20,631 rows; test 13,096 rows; RUL 100 rows | Operating condition columns present in standard C-MAPSS format | Downloaded inside nested archive | operating conditions | Original nested archive preserved. |
| C-MAPSS FD002 | https://phm-datasets.s3.amazonaws.com/NASA/6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip | Aero engine simulation | 14.82 MB inside nested C-MAPSS archive | `.txt` | 3 files (`train`, `test`, `RUL`) | 26 columns in train/test rows | train 53,759 rows; test 33,991 rows; RUL 259 rows | Operating condition columns present in standard C-MAPSS format | Downloaded inside nested archive | operating conditions | Original nested archive preserved. |
| C-MAPSS FD003 | https://phm-datasets.s3.amazonaws.com/NASA/6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip | Aero engine simulation | 7.04 MB inside nested C-MAPSS archive | `.txt` | 3 files (`train`, `test`, `RUL`) | 26 columns in train/test rows | train 24,720 rows; test 16,596 rows; RUL 100 rows | Operating condition columns present in standard C-MAPSS format | Downloaded inside nested archive | operating conditions | Original nested archive preserved. |
| C-MAPSS FD004 | https://phm-datasets.s3.amazonaws.com/NASA/6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip | Aero engine simulation | 17.31 MB inside nested C-MAPSS archive | `.txt` | 3 files (`train`, `test`, `RUL`) | 26 columns in train/test rows | train 61,249 rows; test 41,214 rows; RUL 248 rows | Operating condition columns present in standard C-MAPSS format | Downloaded inside nested archive | operating conditions | Original nested archive preserved. |
| Paderborn Bearing Dataset | https://groups.uni-paderborn.de/kat/BearingDataCenter/ | Bearing systems | 5.1 GB | `.rar`, `.txt` | 32 `.rar` archives plus `readme_versions.txt` | Not counted; archives preserved without extraction | Not counted; archives preserved without extraction | Not counted in this census | Downloaded | speed; load | Original archives preserved under `data/bearing/paderborn/`. |
| FEMTO Bearing Dataset / IEEE PHM 2012 / PRONOSTIA | https://www.femto-st.fr/en/Research-departments/AS2M/Research-groups/PHM/IEEE-PHM-2012-Data-challenge.php | Bearing systems | Not available locally | Not available locally | 0 local files | Not available locally | Not available locally | Not available locally | Source identified; not downloaded | speed; load | Source page reachable, but stable direct archive links were not exposed during collection. |
| XJTU-SY Bearing Dataset | https://biaowang.tech/xjtu-sy-bearing-datasets/ | Bearing systems | Not available locally | Not available locally | 0 local files | Not available locally | Not available locally | Not available locally | Source identified; not downloaded | speed; load | Source page exposes cloud mirrors; raw files were not automatically downloaded. |

---

## NASA Battery Dataset

Dataset Name:

NASA Battery Dataset

Source:

https://data.nasa.gov/dataset/li-ion-battery-aging-datasets

Domain:

Lithium-ion batteries

Approximate Size:

209.7 MB

File Format:

ZIP containing nested ZIP archives and `.mat` files.

Number of Files:

1 outer ZIP.

6 nested ZIP archives visible.

38 `.mat` files visible inside nested archives.

README files present.

Number of Variables:

MATLAB structures.

Visible README fields include:

- cycle type
- ambient temperature
- voltage
- current
- temperature
- capacity
- impedance-related fields

Sequence Length:

Varies by battery and cycle.

Not counted in this census.

Sampling Information:

Charge, discharge, and impedance operations are described in README files.

Some README files directly state room temperature, 24 deg C, or 4 deg C.

Current Status:

Downloaded.

Natural Regimes:

- temperature
- charge/discharge/impedance profile
- cutoff-voltage/current profile

Notes:

Original archive preserved unchanged.

---

## Oxford Battery Dataset

Dataset Name:

Oxford Battery Degradation Dataset 1

Source:

https://ora.ox.ac.uk/objects/uuid:03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac

Domain:

Lithium-ion batteries

Approximate Size:

266.2 MB main `.mat`.

0.07 MB example `.mat`.

README 5.6 KB.

File Format:

`.mat` and `.txt`.

Number of Files:

3 local files.

Number of Variables:

Main file contains 8 cell structs.

README lists:

- time
- voltage
- charge
- temperature
- current in example discharge file

Sequence Length:

Characterisation measurements every 100 cycles.

Exact series lengths were not counted in this census.

Sampling Information:

README states 40 deg C chamber.

README describes CC-CV charge and drive-cycle discharge.

Current Status:

Downloaded.

Natural Regimes:

- temperature
- charge/discharge profile
- drive-cycle discharge
- characterisation interval

Notes:

Original files preserved unchanged.

---

## ZEMA Hydraulic Dataset

Dataset Name:

ZEMA Hydraulic System Condition Monitoring Dataset

Source:

https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems

Domain:

Hydraulic systems

Approximate Size:

76.6 MB

File Format:

ZIP containing `.txt` channels and documentation.

Number of Files:

20 archive members.

Number of Variables:

17 signal/profile text files plus documentation.

Row widths vary by sensor file.

Sequence Length:

2205 rows for main signal/profile files.

Sampling Information:

Sampling details are present in documentation.

They were not parsed beyond archive-level census.

Current Status:

Downloaded.

Natural Regimes:

- pressure region
- valve states
- cooler/pump/accumulator states visible through profile file

Notes:

Original archive preserved unchanged.

---

## C-MAPSS FD001

Dataset Name:

C-MAPSS FD001

Source:

https://phm-datasets.s3.amazonaws.com/NASA/6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip

Domain:

Aero engine simulation

Approximate Size:

5.74 MB inside nested C-MAPSS archive.

File Format:

`.txt`

Number of Files:

3 files:

- `train_FD001.txt`
- `test_FD001.txt`
- `RUL_FD001.txt`

Number of Variables:

26 columns in train/test rows.

Sequence Length:

train 20,631 rows.

test 13,096 rows.

RUL 100 rows.

Sampling Information:

Operating condition columns present in standard C-MAPSS format.

Current Status:

Downloaded inside nested archive.

Natural Regimes:

- operating conditions

Notes:

Original nested archive preserved unchanged.

---

## C-MAPSS FD002

Dataset Name:

C-MAPSS FD002

Source:

https://phm-datasets.s3.amazonaws.com/NASA/6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip

Domain:

Aero engine simulation

Approximate Size:

14.82 MB inside nested C-MAPSS archive.

File Format:

`.txt`

Number of Files:

3 files:

- `train_FD002.txt`
- `test_FD002.txt`
- `RUL_FD002.txt`

Number of Variables:

26 columns in train/test rows.

Sequence Length:

train 53,759 rows.

test 33,991 rows.

RUL 259 rows.

Sampling Information:

Operating condition columns present in standard C-MAPSS format.

Current Status:

Downloaded inside nested archive.

Natural Regimes:

- operating conditions

Notes:

Original nested archive preserved unchanged.

---

## C-MAPSS FD003

Dataset Name:

C-MAPSS FD003

Source:

https://phm-datasets.s3.amazonaws.com/NASA/6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip

Domain:

Aero engine simulation

Approximate Size:

7.04 MB inside nested C-MAPSS archive.

File Format:

`.txt`

Number of Files:

3 files:

- `train_FD003.txt`
- `test_FD003.txt`
- `RUL_FD003.txt`

Number of Variables:

26 columns in train/test rows.

Sequence Length:

train 24,720 rows.

test 16,596 rows.

RUL 100 rows.

Sampling Information:

Operating condition columns present in standard C-MAPSS format.

Current Status:

Downloaded inside nested archive.

Natural Regimes:

- operating conditions

Notes:

Original nested archive preserved unchanged.

---

## C-MAPSS FD004

Dataset Name:

C-MAPSS FD004

Source:

https://phm-datasets.s3.amazonaws.com/NASA/6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip

Domain:

Aero engine simulation

Approximate Size:

17.31 MB inside nested C-MAPSS archive.

File Format:

`.txt`

Number of Files:

3 files:

- `train_FD004.txt`
- `test_FD004.txt`
- `RUL_FD004.txt`

Number of Variables:

26 columns in train/test rows.

Sequence Length:

train 61,249 rows.

test 41,214 rows.

RUL 248 rows.

Sampling Information:

Operating condition columns present in standard C-MAPSS format.

Current Status:

Downloaded inside nested archive.

Natural Regimes:

- operating conditions

Notes:

Original nested archive preserved unchanged.

---

## Paderborn Bearing Dataset

Dataset Name:

Paderborn Bearing Dataset

Source:

https://groups.uni-paderborn.de/kat/BearingDataCenter/

Domain:

Bearing systems

Approximate Size:

5.1 GB

File Format:

`.rar` and `.txt`

Number of Files:

32 `.rar` archives plus `readme_versions.txt`.

Number of Variables:

Not counted.

Archives preserved without extraction.

Sequence Length:

Not counted.

Archives preserved without extraction.

Sampling Information:

Not counted in this census.

Current Status:

Downloaded.

Natural Regimes:

- speed
- load

Notes:

Original archives preserved unchanged.

---

## FEMTO Bearing Dataset

Dataset Name:

FEMTO Bearing Dataset / IEEE PHM 2012 / PRONOSTIA

Source:

https://www.femto-st.fr/en/Research-departments/AS2M/Research-groups/PHM/IEEE-PHM-2012-Data-challenge.php

Domain:

Bearing systems

Approximate Size:

Not available locally.

File Format:

Not available locally.

Number of Files:

0 local files.

Number of Variables:

Not available locally.

Sequence Length:

Not available locally.

Sampling Information:

Not available locally.

Current Status:

Source identified.

Not downloaded.

Natural Regimes:

- speed
- load

Notes:

Source page reachable.

Stable direct archive links were not exposed during collection.

---

## XJTU-SY Bearing Dataset

Dataset Name:

XJTU-SY Bearing Dataset

Source:

https://biaowang.tech/xjtu-sy-bearing-datasets/

Domain:

Bearing systems

Approximate Size:

Not available locally.

File Format:

Not available locally.

Number of Files:

0 local files.

Number of Variables:

Not available locally.

Sequence Length:

Not available locally.

Sampling Information:

Not available locally.

Current Status:

Source identified.

Not downloaded.

Natural Regimes:

- speed
- load

Notes:

Source page exposes cloud mirrors.

Raw files were not automatically downloaded.

