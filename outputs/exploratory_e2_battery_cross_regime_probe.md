# Exploratory E-2 Battery Cross-Regime Probe

Status: Observation only.

This is NOT validation.

This is NOT evidence generation.

This does NOT support Q0.

---

## Protocol Reference

`docs/exploration/e2_battery_cross_regime_probe_v0.1.md`

---

## Datasets

- NASA Battery Dataset
- Oxford Battery Dataset

Only already-downloaded files were used.

---

## Method

Simple same-window and cross-window evaluation.

Model:

Linear regression.

NASA raw inputs:

- time
- measured current
- measured temperature

Oxford raw inputs:

- time
- charge
- temperature

Target:

Voltage.

No PCA, clustering, UMAP, HDBSCAN, Koopman, SINDy, MoE, Transformer, Autoencoder, or deep learning was used.

---

## Regime Windows

| Dataset | Regime | Rows Used |
|---|---|---:|
| NASA Battery | NASA_room_24C_square_4A | 50000 |
| NASA Battery | NASA_cold_4C_fixed_2A | 23736 |
| Oxford Battery | Oxford_C1_discharge | 50000 |
| Oxford Battery | Oxford_OCV_discharge | 50000 |

---

## Key Metrics

| Dataset        | Train_Regime            | Test_Regime             | Comparison   | Train_Rows | Test_Rows | R2       | RMSE   | Spearman |
| -------------- | ----------------------- | ----------------------- | ------------ | ---------- | --------- | -------- | ------ | -------- |
| NASA Battery   | NASA_room_24C_square_4A | NASA_room_24C_square_4A | same-window  | 50000      | 50000     | 0.7460   | 0.1431 | 0.7581   |
| NASA Battery   | NASA_room_24C_square_4A | NASA_cold_4C_fixed_2A   | cross-window | 50000      | 23736     | -1.8348  | 2.2043 | -0.0761  |
| NASA Battery   | NASA_cold_4C_fixed_2A   | NASA_room_24C_square_4A | cross-window | 23736      | 50000     | -14.5824 | 1.1211 | -0.5006  |
| NASA Battery   | NASA_cold_4C_fixed_2A   | NASA_cold_4C_fixed_2A   | same-window  | 23736      | 23736     | 0.2738   | 1.1157 | 0.0573   |
| Oxford Battery | Oxford_C1_discharge     | Oxford_C1_discharge     | same-window  | 50000      | 50000     | 0.8745   | 0.0832 | 0.9964   |
| Oxford Battery | Oxford_C1_discharge     | Oxford_OCV_discharge    | cross-window | 50000      | 50000     | 0.8149   | 0.0987 | 0.9959   |
| Oxford Battery | Oxford_OCV_discharge    | Oxford_C1_discharge     | cross-window | 50000      | 50000     | 0.8284   | 0.0973 | 0.9956   |
| Oxford Battery | Oxford_OCV_discharge    | Oxford_OCV_discharge    | same-window  | 50000      | 50000     | 0.8657   | 0.0841 | 0.9968   |

---

## Verdict

Collapse observed.

---

## Output Restrictions

No conclusion is implied.

No support for Q0 is implied.

No claim upgrade is implied.
