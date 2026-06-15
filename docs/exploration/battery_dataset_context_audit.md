# Battery Dataset Context Audit (P0)

Status: Audit only.

No new models, retraining, or metrics were used. This document records
read-only inspection of dataset documentation, metadata, data structures,
the E-2 implementation, and existing E-2 output.

Purpose: determine whether the NASA and Oxford battery datasets are
comparable enough for the divergent E-2 observations to be meaningful
before any further interpretation.

---

## 1. Sources Inspected

Primary local sources:

- `data/battery/nasa_li_ion/5_Battery_Data_Set.zip`
  - README files inside all six nested archives
  - `.mat` structures for the two groups used by E-2
- `data/battery/oxford/Readme.txt`
- `data/battery/oxford/Oxford_Battery_Degradation_Dataset_1.mat`
- `data/battery/oxford/ExampleDC_C1.mat`
- `src/exploratory_e2_battery_cross_regime_probe.py`
- `outputs/exploratory_e2_battery_cross_regime_probe.md`
- `docs/exploration/e2_battery_cross_regime_probe_v0.1.md`

Supporting project records:

- `docs/exploration/dataset_cards/battery_nasa.md`
- `docs/exploration/dataset_cards/battery_oxford.md`
- `docs/exploration/dataset_census_round1.md`
- `docs/exploration/e2_postmortem.md`

---

## 2. NASA Battery Dataset

### Chemistry and cell type

The local documentation identifies the units only as Li-ion batteries.
Manufacturer, package format, electrode chemistry, and cell model are not
documented. The first archive describes a rated capacity of 2 Ah, but the
documentation does not establish that every NASA sub-archive uses an
identical cell specification.

### Number of cells or units

The outer archive contains 38 `.mat` files representing 34 unique battery
identifiers. Batteries 25-28 occur both in a phase-one archive and in the
larger 25-44 archive.

E-2 used eight units:

- room-temperature group: batteries 25, 26, 27, and 28
- cold group: batteries 49, 50, 51, and 52

### Discharge profile

The dataset is not governed by one discharge profile. Documented profiles
include:

- constant-current 2 A discharge;
- 4 A square-wave loading at 0.05 Hz and 50% duty cycle;
- fixed 1 A, 2 A, or 4 A loads;
- groups with multiple fixed load levels of 1 A, 2 A, and 4 A.

E-2 selected:

- batteries 25-28: 4 A square-wave loading, 0.05 Hz, 50% duty cycle;
- batteries 49-52: fixed 2 A loading.

### Temperature conditions

The README files document room temperature, 24 deg C, 43 deg C, 44 deg C,
and 4 deg C conditions, depending on the battery group. Batteries 38-40
were explicitly tested at multiple ambient temperatures.

E-2 used discharge data at:

- 24 deg C for batteries 25-28;
- 4 deg C for batteries 49-52.

In the cold-group `.mat` files, charge and discharge operations have an
ambient-temperature field of 4 deg C, while impedance operations have
24 deg C. E-2 filtered to discharge operations only.

### Charge profile

The inspected README files consistently describe:

- constant-current charging at 1.5 A until 4.2 V;
- constant-voltage charging until current falls to 20 mA.

This is a CC-CV profile.

### Cutoff voltages

Documented discharge cutoffs are 2.0 V, 2.2 V, 2.5 V, and 2.7 V, assigned
by battery within each group.

For the E-2 groups:

- batteries 25-28 used 2.0 V, 2.2 V, 2.5 V, and 2.7 V respectively;
- batteries 49-52 used 2.0 V, 2.2 V, 2.5 V, and 2.7 V respectively.

Thus each E-2 NASA regime combines four different cutoff voltages.

### Cycling protocol and rest periods

The NASA files contain interleaved charge, discharge, and impedance
operations. The documentation describes repeated charge and discharge
cycling with periodic impedance measurement. It does not state a standard
rest-period protocol, so rest duration and consistency are unknown.

### Definition of a cycle

In the NASA MATLAB structure, `cycle` is the top-level operation array.
Each entry is typed as `charge`, `discharge`, or `impedance`. The
documentation does not define one combined charge-discharge pair as a
separate aging-cycle object.

For this audit, "NASA discharge cycle" means one top-level operation whose
type is `discharge`, matching the E-2 filter.

### Capacity measurement

Discharge records contain `Capacity` in Ah. The README describes this as
battery capacity for discharge to 2.7 V, even in groups where individual
batteries have other stated cutoff voltages. The local documentation does
not explain the calculation or resolve that wording ambiguity.

### Regime or mode changes

Across the full dataset, temperature, load profile, load current, cutoff
voltage, and stopping criteria differ by sub-archive or battery. Batteries
38-40 explicitly include multiple temperatures and current levels.

Within the E-2 selection, the two NASA regimes are different experimental
groups. The room group also comes from an archive named
`BatteryAgingARC_25_26_27_28_P1`, indicating a phase-one subset. No
documented partway protocol change was found inside either selected
group, but cutoff voltage differs between cells.

### End-of-life criterion

NASA does not use one uniform stopping rule across the archive:

- some groups stopped at 30% rated-capacity fade, from 2.0 Ah to 1.4 Ah;
- some groups stopped at 20% fade, at 1.6 Ah;
- the README for the E-2 room group does not state an EOL criterion;
- the E-2 cold-group experiment stopped when control software crashed,
  not at a defined EOL threshold.

Several cold-group discharge records are documented as having unusually
low capacity or voltage for reasons not fully analyzed.

---

## 3. Oxford Battery Dataset

### Chemistry and cell type

The dataset contains eight Kokam SLPB533459H4 740 mAh small Li-ion pouch
cells. The local README does not state the electrode chemistry.

### Number of cells or units

Eight cells were tested. E-2 used data from all eight cells.

### Discharge profile

The aging protocol used a variable-current drive-cycle discharge derived
from the Urban Artemis profile.

Characterization every 100 drive cycles included:

- 1-C discharge at 740 mA;
- pseudo-OCV discharge at 40 mA.

E-2 used the two characterization branches, not the variable-current aging
drive-cycle discharge.

### Temperature conditions

All cells were tested in a thermal chamber at 40 deg C. No temperature
regime change is documented.

### Charge profile

The README describes the aging charge as constant-current-constant-voltage
(CC-CV), but does not give its voltage limit or CV termination current.
The example first cycle separately records a 2-C, 1480 mA constant-current
charge. Characterization data also contain 1-C and pseudo-OCV charge
branches, but E-2 did not use them.

### Cutoff voltages

Charge and discharge cutoff voltages are not stated in the inspected local
README. They could not be determined from the field definitions alone.

### Cycling protocol and rest periods

The documented sequence is repeated Urban Artemis drive cycles with
characterization measurements every 100 drive cycles. Rest periods are
not documented, so their presence, duration, and consistency are unknown.

### Definition of a cycle

The aging cycle is one drive cycle based on the Urban Artemis profile.
Names such as `cyc0100` denote characterization performed after 100 drive
cycles. Each characterization checkpoint contains separate 1-C charge,
1-C discharge, pseudo-OCV charge, and pseudo-OCV discharge branches.

E-2 treated each discharge branch at each checkpoint as source data; it
did not use individual drive-cycle records.

### Capacity measurement

Characterization branches record charge `q` in mAh together with time,
voltage, and temperature. The README does not document the integration,
calibration, or capacity-estimation procedure beyond those recorded
fields.

### Regime or mode changes

No partway change to chamber temperature or aging protocol is documented.
The deliberate periodic switch from drive-cycle aging to 1-C and
pseudo-OCV characterization is part of the protocol.

The eight cells have different final recorded characterization points,
ranging from `cyc5000` to `cyc8200`.

### End-of-life criterion

The README says characterization continued until cell end of life, but
does not define an EOL threshold. A common numeric EOL criterion therefore
could not be confirmed from the local documentation.

---

## 4. Side-by-Side Comparability

| Dimension | NASA | Oxford | Assessment | Basis |
|---|---|---|---|---|
| Battery chemistry / cell type | Li-ion; model, format, and electrode chemistry undocumented | Li-ion Kokam SLPB533459H4, 740 mAh pouch; electrode chemistry undocumented | Unknown | Both are Li-ion, but chemistry equivalence cannot be established and NASA cell type is unspecified. |
| Number of cells / units | 34 unique identifiers overall; E-2 used 8 units in two disjoint groups of 4 | 8 cells overall; E-2 used all 8 in both branches | Different | E-2 compares separate NASA populations but repeated measurements from the same Oxford population. |
| Discharge profile | Multiple fixed/square-wave profiles; E-2 used 4 A square wave versus fixed 2 A | Urban Artemis aging profile; E-2 used 740 mA 1-C versus 40 mA pseudo-OCV characterization | Different | Load shapes and the role of the selected discharges in the aging protocol differ. |
| Current levels | E-2: 4 A amplitude versus fixed 2 A | E-2: 740 mA versus 40 mA | Different | Absolute currents, rates, and contrasts differ. |
| Temperature | E-2: 24 deg C versus 4 deg C | 40 deg C for both E-2 branches | Different | Temperature is part of NASA's regime contrast but not Oxford's. |
| Charge profile | CC 1.5 A to 4.2 V, then CV to 20 mA | CC-CV documented, exact limits incomplete | Comparable | Broad charge mode is equivalent, but Oxford limits are not documented. |
| Discharge cutoff voltage | E-2 combines 2.0, 2.2, 2.5, and 2.7 V cutoffs per regime | Not documented | Unknown | Oxford cutoff cannot be compared. |
| Cycling protocol | Charge/discharge cycling with impedance operations | Urban Artemis aging cycles with characterization every 100 cycles | Different | The measurement schedules and operation types differ. |
| Rest periods | Not documented | Not documented | Unknown | Neither local source establishes a rest protocol. |
| Meaning of "cycle" | Top-level operation typed charge, discharge, or impedance | One Urban Artemis drive cycle; E-2 data are characterization checkpoints | Different | The stored and E-2-selected observational units are not equivalent. |
| Capacity measurement | `Capacity` in Ah on discharge records; calculation detail ambiguous | Characterization `q` in mAh; calculation detail undocumented | Unknown | Recorded quantities are related, but methodological equivalence is not documented. |
| Regime/mode changes | Multiple temperatures, loads, cutoffs, and group protocols; E-2 uses separate groups | Fixed 40 deg C aging protocol with periodic C1/OCV characterization | Different | NASA regimes are between experimental groups; Oxford regimes are within-checkpoint measurement branches. |
| End-of-life criterion | Heterogeneous: 20%, 30%, unstated, or software-crash termination | EOL mentioned but threshold undefined | Unknown | A common stopping criterion cannot be established. |

---

## 5. E-2 Implementation Review

### NASA regime definition

NASA regimes were hard-coded as archive and battery selections:

- `NASA_room_24C_square_4A`
  - archive: `BatteryAgingARC_25_26_27_28_P1.zip`
  - units: batteries 25-28
  - documented context: 24 deg C and 4 A square-wave discharge
- `NASA_cold_4C_fixed_2A`
  - archive: `BatteryAgingARC_49_50_51_52.zip`
  - units: batteries 49-52
  - documented context: 4 deg C and fixed 2 A discharge

The loader retained all top-level `discharge` operations, concatenated
them across the four units, and discarded cycle and unit identifiers.

### Oxford regime definition

Oxford regimes were hard-coded as branches within every available
characterization checkpoint for all eight cells:

- `Oxford_C1_discharge` maps to `C1dc`;
- `Oxford_OCV_discharge` maps to `OCVdc`.

These are 740 mA 1-C and 40 mA pseudo-OCV characterization discharges,
respectively. They are not two chamber-temperature or aging-protocol
groups.

### Consistency of regime criteria

Dataset-specific definitions were used.

NASA "regime" means a different set of cells, temperature, load shape,
and archive. Oxford "regime" means a different characterization branch
measured on the same cells at the same chamber temperature. The regime
contrast is therefore not operationalized by the same criterion.

### Sample size used by E-2

| Dataset / regime | Units | Discharge cycles or characterization checkpoints | Raw rows before cap | Rows used by E-2 |
|---|---:|---:|---:|---:|
| NASA room, square-wave 4 A | 4 | 112 discharge operations (28 per cell) | 65,352 | 50,000 |
| NASA cold, fixed 2 A | 4 | 100 discharge operations (25 per cell) | 23,736 | 23,736 |
| Oxford C1 discharge | 8 | 519 cell-checkpoints | 1,610,378 | 50,000 |
| Oxford pseudo-OCV discharge | 8 | 519 cell-checkpoints | 6,059,207 | 50,000 |

Oxford checkpoint counts differ by cell: 46-78 checkpoints, with final
labels from `cyc5000` to `cyc8200`.

### Preprocessing differences

Common processing:

- convert selected arrays to one-dimensional numeric vectors;
- truncate fields within each record to their shared minimum length;
- replace infinities and drop rows containing missing values;
- concatenate records within each named regime;
- if over 50,000 rows, retain 50,000 evenly spaced row positions;
- use voltage as the target;
- apply the same linear-regression evaluation function.

Dataset-specific processing:

- NASA filters top-level operations to `type == "discharge"`; Oxford reads
  `C1dc` and `OCVdc` branches from characterization checkpoints.
- NASA predictors are time, measured current, and measured temperature.
- Oxford predictors are time, accumulated charge, and temperature.
- NASA regimes use disjoint four-cell populations; Oxford regimes use the
  same eight-cell population and the same checkpoint set.
- NASA room data and both Oxford branches are downsampled to 50,000 rows;
  NASA cold data remain uncapped at 23,736 rows.
- Concatenation removes unit and cycle/checkpoint identity before
  downsampling and evaluation. There is no unit-balanced or
  cycle-balanced sampling.

The existing output reports one final global verdict from all cross-window
rows. The postmortem's separate NASA and Oxford descriptions are inferred
from their dataset-specific metric rows rather than emitted as separate
verdict fields by the script.

---

## 6. Three-Layer Diagnosis

### Layer 1: Acquisition Protocol Comparability

Assessment: **Different**

The two E-2 comparisons do not measure equivalent regime contrasts. NASA
uses disjoint cell groups with simultaneous temperature and load-profile
differences, multiple cutoff voltages within each group, and different
termination context. Oxford uses two characterization discharge rates on
the same cells, at the same temperature, at the same characterization
checkpoints. "Battery discharge voltage data" is common to both, but the
acquisition contexts are not comparable enough to treat the divergent
E-2 outcomes as a controlled cross-dataset comparison of Type C.

### Layer 2: Chemistry/Degradation Mechanism

Assessment: **Unknown**

Both datasets are documented as Li-ion. Oxford supplies a manufacturer,
model, pouch format, and rated capacity; NASA does not document comparable
cell identity or electrode chemistry. Neither local source directly
identifies the active-material chemistry needed for a chemistry-level
comparison. The aging protocols and temperatures differ, but this audit
does not establish which degradation mechanisms dominated either
dataset. A same-versus-different mechanism assessment cannot be made from
the inspected evidence.

### Layer 3: E-2 Implementation Consistency

Assessment: **Inconsistent**

The same regression/evaluation function was used, but the inputs were not
constructed consistently. Regime definitions, predictors, source
populations, observational units, and effective sampling paths differ.
NASA compares different cells under different temperature/load contexts
using current as a predictor; Oxford compares two branches from the same
cells/checkpoints using charge as a predictor. These implementation
differences are sufficient to prevent attributing the divergent E-2
results solely to a dataset property.

---

## 7. Summary Table

| Layer | Assessment | Confidence | Notes |
|-------|-----------|------------|-------|
| Layer 1 (Acquisition) | Different | High | NASA E-2 contrasts disjoint cells at 24 deg C/4 A square-wave versus 4 deg C/2 A fixed load; Oxford contrasts 1-C versus pseudo-OCV characterization on the same cells at 40 deg C. |
| Layer 2 (Chemistry) | Unknown | High | Both are Li-ion, but NASA cell identity and both datasets' electrode chemistry/degradation mechanism are not documented sufficiently for comparison. |
| Layer 3 (E-2 Implementation) | Inconsistent | High | The evaluation function is shared, but regime definitions, predictors, populations, observational units, row counts, and capping paths differ. |

---

## 8. Explicit Non-Conclusions

This audit does **not** determine:

- whether Type C is real in either dataset;
- whether the NASA or Oxford E-2 result is more correct;
- any implication for Q0;
- any implication for the engineering line.

The E-2 divergence cannot currently be interpreted as a meaningful
NASA-versus-Oxford difference. Acquisition and implementation differences
are documented, while chemistry and degradation-mechanism comparability
remain unresolved. Further interpretation would require comparable
protocol definitions and additional documentation or data inspection;
this audit does not perform that work.

This document does not modify the Claim Registry, Concept Paper,
`baseline_management_v0.2`, or `validation_d_protocol`. It does not
propose unification with any other exploration line.

---

## Version History

v0.2 - 2026-06-15 - P0 audit expanded from primary local documentation,
metadata, data structures, E-2 source, and existing E-2 output. Added
side-by-side comparability, implementation consistency, three-layer
diagnosis, summary, and explicit non-conclusions.
