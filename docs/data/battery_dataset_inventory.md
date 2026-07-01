# Battery Dataset Inventory

Date: 2026-06-10

Purpose:

Prepare battery datasets for future exploratory work.

No preprocessing was performed.

No scripts were created.

No experiments were run.

Raw data remains under `data/battery/` and is ignored by Git.

---

## Dataset 1: NASA Li-ion Battery Aging Dataset

Dataset name:

NASA Li-ion Battery Aging Dataset / NASA Battery Data Set

Source URL:

https://data.nasa.gov/dataset/li-ion-battery-aging-datasets

Current download source used:

https://phm-datasets.s3.amazonaws.com/NASA/5.+Battery+Data+Set.zip

Source notes:

The NASA Open Data Portal page currently points to the legacy Dashlink record and lists no attached data resources. The current NASA PCoE Data Set Repository page lists the battery dataset download through the PHM datasets S3 mirror.

Local path:

`data/battery/nasa_li_ion/5_Battery_Data_Set.zip`

File formats:

ZIP archive containing nested ZIP archives for NASA battery aging data.

Approximate size:

200.0 MB

Downloaded file:

| File | Size |
|---|---:|
| `data/battery/nasa_li_ion/5_Battery_Data_Set.zip` | 209,708,670 bytes |

Archive contents observed:

| Archive member |
|---|
| `5. Battery Data Set/1. BatteryAgingARC-FY08Q4.zip` |
| `5. Battery Data Set/2. BatteryAgingARC_25_26_27_28_P1.zip` |
| `5. Battery Data Set/3. BatteryAgingARC_25-44.zip` |
| `5. Battery Data Set/4. BatteryAgingARC_45_46_47_48.zip` |
| `5. Battery Data Set/5. BatteryAgingARC_49_50_51_52.zip` |
| `5. Battery Data Set/6. BatteryAgingARC_53_54_55_56.zip` |

Notes:

Original archive kept unchanged.

No extraction was performed.

No preprocessing was performed.

---

## Dataset 2: Oxford Battery Degradation Dataset 1

Dataset name:

Oxford Battery Degradation Dataset 1

Alternative title:

Long term battery ageing tests of 8 Kokam (SLPB533459H4) 740 mAh lithium-ion pouch cells

Source URL:

https://ora.ox.ac.uk/objects/uuid:03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac

Direct download sources used:

| File | Source URL |
|---|---|
| `ExampleDC_C1.mat` | `https://ora.ox.ac.uk/objects/uuid:03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac/files/me9fc40a60ac98708f1b73f3a836548e9` |
| `Oxford_Battery_Degradation_Dataset_1.mat` | `https://ora.ox.ac.uk/objects/uuid:03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac/files/m5ac36a1e2073852e4f1f7dee647909a7` |
| `Readme.txt` | `https://ora.ox.ac.uk/objects/uuid:03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac/files/m43cc05e7c5f1245f4895d9dbd495e52f` |

Local path:

`data/battery/oxford/`

File formats:

MATLAB `.mat` files and plain text README.

Approximate size:

253.9 MB total.

Downloaded files:

| File | Size |
|---|---:|
| `data/battery/oxford/ExampleDC_C1.mat` | 72,593 bytes |
| `data/battery/oxford/Oxford_Battery_Degradation_Dataset_1.mat` | 266,164,290 bytes |
| `data/battery/oxford/Readme.txt` | 5,643 bytes |

Notes:

Original files kept unchanged.

`Readme.txt` was preserved.

No preprocessing was performed.

The ORA record states that the dataset contains long-term cycling results for 8 lithium-ion cells and that full details are provided in the README.

---

## Git Tracking

Raw data location:

`data/battery/`

Git status:

Raw data is ignored by the existing `.gitignore` rule:

`data/`

Only this inventory document is intended to be committed.
