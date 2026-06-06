# Validation C0 Series — FROZEN
Date: 2026-06-06
Status: Frozen — No further N-CMAPSS experiments planned

---

## Series Overview

| Stage | Purpose | Result |
|-------|---------|--------|
| C0 | Pipeline mechanics on N-CMAPSS | Weak Evidence (Ground Truth issue) |
| C0.1 | Label audit — diagnose C0 failure | Diagnosis complete |
| C0.2 | Ground Truth aligned rerun | Strong PASS |

---

## Final Conclusions

### Q1: Condition → Expected State
T50 held-out R²: 0.992~0.996
Confirmed transferable to aero engine domain.

### Q2: Residual → Degradation
T50 vs HPT_eff_mod |Spearman|: 0.772~0.826
Confirmed degradation signal in residual across two domains.

### Q3: Residual → HI
HI_v0 vs HPT_eff_mod |Spearman|: 0.951~0.994
HI amplifies degradation signal beyond raw residual.

### Early Detection
Average detection at ~23% of lifecycle (threshold: 1.5x early-life HI).

---

## Lessons Learned

1. Ground Truth alignment is prerequisite:
   Always audit degradation label distributions
   before selecting State Variables.
   HPC_eff_mod was zero in DS02-006 (HPT fault type, not HPC).

2. Data-driven variable selection outperforms intuition:
   Spearman ranking identified T50 as primary target.
   T30 (intuitive HPC analog) had near-zero correlation.

3. HI amplifies signal:
   HI Spearman (0.994) > Residual Spearman (0.826).
   Rolling RMS is not just noise reduction — it enhances trend.

4. Different DS files = different fault modes:
   N-CMAPSS DS02 = HPT fault type.
   Always check T_dev label distributions first.

---

## Boundary Conditions

This series validates ONLY:
- Expected State pipeline mechanics
- Residual generation mechanics
- HI_v0 behavior on non-HVAC data
- Segment-aware processing (artificial segments)

This series does NOT validate:
- Real maintenance events
- Baseline reset semantics
- Q4b (requires real Marine maintenance records)
- Marine domain transfer (requires ship data)

---

## Transfer Value to Marine Systems

Cross-domain pattern (HVAC → Aero Engine → Marine hypothesis):
- Downstream temperature variables (CT_SW_TEMP_1, T50)
  are consistently most sensitive to degradation
- This suggests: exhaust temperature (EGT per cylinder)
  may be the strongest candidate for Marine HI
- Data-driven sensor selection should always precede
  model training (sensor ranking audit as standard step)

---

## Why No Further N-CMAPSS Experiments

Q1, Q2, Q3 now have cross-domain evidence.
Marginal returns from additional N-CMAPSS experiments are low.
Next required evidence is Marine domain validation (Validation D).
N-CMAPSS cannot provide maintenance event semantics.
