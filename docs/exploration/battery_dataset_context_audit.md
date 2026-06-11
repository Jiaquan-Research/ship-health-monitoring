# Battery Dataset Context Audit

NASA vs Oxford

---

## 1. Purpose

E-2 produced different observations for NASA and Oxford battery data.

Before updating experiment or question ledgers, audit whether the two datasets are comparable.

Goal:

Understand experimental context.

Not:

Interpret E-2.

Not:

Support Q0.

Not:

Explain collapse.

This is context audit only.

No conclusions are implied.

---

## 2. Sources Inspected

NASA sources:

- local NASA Battery archive under `data/battery/nasa_li_ion/`
- local README files inside nested NASA Battery archives
- NASA Open Data page already used in the project:
  https://data.nasa.gov/dataset/li-ion-battery-aging-datasets

Oxford sources:

- local Oxford files under `data/battery/oxford/`
- local `Readme.txt`
- Oxford ORA source already used in the project:
  https://ora.ox.ac.uk/objects/uuid:03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac

---

## 3. Context Table

| Item | NASA | Oxford | Notes |
|---|---|---|---|
| Cell format | Li-ion batteries; specific manufacturer/cell format not stated in inspected local README excerpts | 8 small lithium-ion pouch cells; Kokam SLPB533459H4, 740mAh | Oxford cell identity is explicit in local README. NASA local README excerpts identify battery numbers but not cell format/manufacturer. |
| Number of cells | Multiple groups of four batteries per sub-archive; E-2 used batteries 25-28 and 49-52 | 8 cells | Counts refer to local README-visible groups. |
| Temperature regime | Room temperature; 24 deg C; 4 deg C groups visible in local README files | 40 deg C thermal chamber | E-2 NASA regimes mixed 24 deg C and 4 deg C groups. E-2 Oxford regimes came from the same 40 deg C dataset. |
| Charge profile | CC at 1.5A to 4.2V, then CV until current dropped to 20mA in inspected README files | Constant-current-constant-voltage charging profile; characterisation includes 1-C cycles; example file includes 2-C constant current charge | Both describe charge profiles, but not identical experiment framing. |
| Discharge profile | Multiple profiles visible: 2A constant-current discharge; 4A square-wave loading at 0.05Hz and 50% duty cycle; 1A fixed load; 2A fixed load | Drive-cycle discharge based on Urban Artemis profile; characterisation includes 1-C discharge and pseudo-OCV discharge | NASA has several sub-archive discharge regimes. Oxford E-2 used branches within one dataset. |
| Current/load variation | NASA README files state 1A, 2A, 4A, and 4A square-wave loading across different groups | Oxford README states 740mA 1-C cycles, 40mA pseudo-OCV cycles, and example 1480mA 2-C charge | Load/current variation exists in both, but E-2 selected different kinds of regime contrast. |
| Cutoff voltage variation | NASA README files state different discharge cutoff voltages such as 2.0V, 2.2V, 2.5V, and 2.7V depending on battery/group | Cutoff voltage variation not emphasized in inspected Oxford README excerpt | NASA cutoff variation is directly visible in local README files. |
| Impedance/EIS | Included; EIS frequency sweep from 0.1Hz to 5kHz stated in NASA README files | Not listed as an E-2 branch in inspected Oxford README; Oxford file structure includes C1 and OCV characterisation branches | NASA includes impedance operations. E-2 used discharge data only. |
| Characterization interval | NASA cycles include charge, discharge, and impedance operations; interval varies by archive and was not normalized in this audit | Characterisation measurements every 100 cycles | Oxford characterisation interval is explicitly stated. |
| E-2 regimes used | `NASA_room_24C_square_4A`: BatteryAgingARC_25_26_27_28_P1, batteries 25-28; `NASA_cold_4C_fixed_2A`: BatteryAgingARC_49_50_51_52, batteries 49-52 | `Oxford_C1_discharge`; `Oxford_OCV_discharge` | E-2 NASA regimes came from different NASA sub-archives. E-2 Oxford regimes came from branches inside the same Oxford dataset. |
| Regime strength | Stronger visible experimental differences: temperature differs, discharge profile differs, and cutoff voltage set differs across selected NASA groups | Weaker visible experimental differences in E-2: C1 discharge vs pseudo-OCV discharge within the same 40 deg C dataset | This is a context note only, not an E-2 interpretation. |

---

## 4. NASA Context Notes

NASA local README files state that batteries were run through:

- charge operations
- discharge operations
- impedance operations

Visible NASA ambient temperature contexts include:

- room temperature
- 24 deg C
- 4 deg C

Visible NASA charge profile:

- constant current at 1.5A until 4.2V
- constant voltage until charge current dropped to 20mA

Visible NASA discharge profiles include:

- constant-current discharge at 2A
- 4A square-wave loading profile at 0.05Hz and 50% duty cycle
- fixed load current level of 1A
- fixed load current level of 2A

Visible NASA cutoff voltages include:

- 2.0V
- 2.2V
- 2.5V
- 2.7V

NASA includes impedance/EIS:

- EIS frequency sweep from 0.1Hz to 5kHz

E-2 NASA regimes used:

- `NASA_room_24C_square_4A`
- `NASA_cold_4C_fixed_2A`

These regimes came from different NASA sub-archives.

---

## 5. Oxford Context Notes

Oxford local README states:

- 8 small lithium-ion pouch cells
- Kokam SLPB533459H4
- 740mAh
- thermal chamber at 40 deg C

Oxford charge/discharge context:

- constant-current-constant-voltage charging profile
- drive-cycle discharging profile from Urban Artemis
- characterisation measurements every 100 cycles

Oxford characterisation data include:

- 1-C charge
- 1-C discharge
- pseudo-OCV charge
- pseudo-OCV discharge

Oxford local README lists fields:

- time
- voltage
- charge
- temperature
- current in the example discharge file

E-2 Oxford regimes used:

- `Oxford_C1_discharge`
- `Oxford_OCV_discharge`

These regimes came from branches inside the same Oxford dataset.

---

## 6. E-2 Context Note

E-2 should not yet be interpreted as:

"NASA Battery differs from Oxford Battery"

because the experimental regimes may be different in strength and type.

Allowed context wording:

"NASA and Oxford battery datasets are not directly comparable without context normalization."

"NASA E-2 regimes appear to mix stronger experimental differences than Oxford E-2 regimes."

Forbidden wording:

"NASA proves battery collapse."

"Oxford disproves battery collapse."

"Battery supports Q0."

"Battery rejects Q0."

---

## 7. Evidence Status

Evidence level:

None.

Context audit only.

No claim upgrades.

No question upgrades.

No theory.

---

## Version History

v0.1

2026-06-11

Initial context audit created after E-2.

No conclusions.

