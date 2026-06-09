# Baseline Management in Industrial PHM Systems

## Executive finding

The strongest cross-industry pattern is not “one baseline for life,” but **asset-specific baselines that are re-established after interventions that materially change either the physical condition of the asset or the measurement chain**. Nuclear maintenance programs require baseline criteria, post-maintenance verification, configuration control, and calibration control; aircraft engine EHM uses corrected engine-specific deltas, shop-visit segmentation, and fleet context; gas turbine monitoring often separates short-term fouling recovery from long-term irreversible degradation by anchoring trends to after-wash states; rotating machinery programs explicitly treat the first data after overhaul/repair as a new baseline; and chiller FDD systems use either a manufacturer baseline or a “best baseline” model that can be replaced when performance demonstrably improves. citeturn8view0turn9view0turn17view0turn14view0turn12view0turn22view0turn29view0turn29view1turn32view0

For your ship PHM chain, the most defensible path from `Residual → HI → Trend` to `Maintenance Event → Baseline Reset → Long-Term Health Monitoring` is an **event-aware, multi-segment, hybrid architecture**: keep the expected-state model physics-informed, classify maintenance events by how much they restore hardware or alter sensors/configuration, reset only the affected baseline scope, compute HI and trend **within each maintenance segment**, and preserve asset-level continuity through maintenance markers plus a restoration factor or virtual-age variable instead of forcing a single continuous absolute HI across all lifecycle segments. That pattern is the closest match to what mature PHM programs already do in open literature and industrial guidance. citeturn36search12turn36search0turn37search0turn12view0turn22view0turn29view0turn32view0

If one public dataset must be chosen to **start** Q4b work, choose **N-CMAPSS**, but only as a **surrogate validation scaffold**, not as a direct proof of maintenance-reset logic. It has rich operating-context channels, explicit cycle structure, multiple fault modes, and run-to-failure trajectories under real flight conditions, which makes it the best public platform for validating segmentation, normalization, and trend-continuation mechanics under operational variability. It does **not** contain real maintenance events or maintenance-restart lifecycles, so it cannot close Q4b by itself. citeturn42view0

## Baseline practices across mature PHM systems

Across the surveyed domains, the practical definition of a baseline is usually **equipment-specific expected behavior under controlled or normalized operating conditions**, with fleet information used as context rather than as the sole reference. Full resets are typically triggered by overhaul, replacement, repair, or measurement-chain interventions; rolling or adaptive updates are used only to manage environmental and operational variability, not to erase major maintenance discontinuities. citeturn8view0turn14view0turn12view0turn22view0turn29view0turn32view0

| Industry | How baseline is defined in practice | What triggers update vs reset | How post-reset transition is handled | Evidence of long-term deployment |
|---|---|---|---|---|
| **Nuclear power plant PHM / online monitoring** | Asset-specific **baseline criteria** are established from commissioning, startup testing, and initial power operation; these criteria cover function/performance expectations and acceptance margins. citeturn8view0turn7search1 | **Reset / re-baseline:** overhaul, repair, configuration changes that invalidate prior assumptions, calibration interventions, non-identical replacements. **Update:** maintenance procedures and monitoring plans are revised when plant configuration changes. citeturn9view0turn9view2turn9view3 | Equipment returns to service only after **post-maintenance verification/testing**, configuration verification, record review, and fitness-for-service assessment; the implication is that new valid reference data are taken only after that gate. citeturn9view0turn9view1 | DOE/EPRI guidance reports that online monitoring at several plants has been effective for finding out-of-calibration channels and equipment degradation; recent NRC/industry work continues to use OLM for calibration interval extension. citeturn10search12turn10search16turn35search19 |
| **Aircraft engine EHM / ETM** | Baseline is typically an **engine-specific corrected baseline model** referenced to ambient/thrust-normalized conditions; manufacturers historically supplied new-engine baselines, and operators may derive a peak-performance in-flight baseline if factory data are unavailable. Fleet averages are used as context, not as the sole baseline. citeturn14view0turn12view0turn13view0 | **Reset / segment restart:** shop visit, overhaul, on-wing restoration actions, some module/component replacements, and obvious maintenance-induced parameter step changes. **Update:** smoothed deterioration gradients and fleet comparisons continue within a segment. citeturn12view0turn15view1 | Use **stability-point filtering**, corrected deltas, and a new deterioration slope after the intervention. MTU explicitly tracks “shop visit effects (regained performance)” and “workscope-specific deterioration,” while prognostic gradients are re-estimated from segment history. citeturn12view0turn13view0turn13view1 | EASA ETOPS guidance requires a validated engine condition monitoring process and a verification program for adverse trends; MTU reports ETM deployment across 150+ airlines and “substantial experience since 2006.” citeturn17view0turn12view0 |
| **Industrial gas turbine PHM** | Baseline is often **physics-informed, normalized performance**, but operationally many programs use **after-wash clean condition** as the local baseline anchor for a fouling cycle and compare successive after-wash states for long-term structural degradation. citeturn22view0turn23view0turn23view1 | **Reset / local re-baseline:** compressor wash, servicing performed with the wash, overhaul, or major maintenance affecting performance map. **Update:** ambient compensation and continuous performance monitoring within a cycle. citeturn22view0turn23view0 | Short-term trend = before-wash vs after-wash within a wash cycle; long-term trend = after-wash-to-after-wash comparison versus the first wash, explicitly separating recoverable fouling from irreversible degradation. citeturn22view0turn23view1 | PHM Society work demonstrates this split on repeated service cycles; ASME reports real-time online monitoring on GE Frame 7 units for continuous tracking of efficiency and combustion/compressor issues. citeturn22view0turn20search8turn19search0 |
| **Oil and gas rotating machinery PHM** | Baseline is usually an **asset-specific vibration fingerprint / reference spectrum** taken when the machine is in good order. ABS defines baseline data as initial CM data when entering the program or the first CM data after overhaul/repair that invalidates the previous baseline. citeturn29view0 | **Reset:** overhaul or repair that invalidates the previous baseline; startup after new install or overhaul is treated as a new transient/steady-state reference opportunity. **Update:** periodic comparison to the current valid baseline. citeturn29view0turn29view1 | DNV highlights startup/shutdown vibration collection after new installation or overhaul to establish the vibration baseline, then compares current vibration against it; after maintenance, diagnostics distinguish whether high 1× vibration is simply maintenance-induced unbalance or a developing defect. citeturn29view1 | API 670 codifies the protection layer around critical rotating equipment, while ABS/DNV guidance shows sustained industrial use of baseline-based monitoring for compressors, pumps, and turbines. citeturn25search0turn29view0turn29view1 |
| **HVAC PHM, especially chillers** | Baseline is commonly a **manufacturer baseline model** or a field-derived **best baseline** built from the best observed historical performance. Chiller FDD systems use modeled expected performance rather than a single raw operating point. citeturn32view0turn33search2 | **Reset / replacement of baseline model:** substantial maintenance or fault correction that measurably improves COP/IPLV or restores approach metrics; older chillers without factory data may adopt a better field-derived baseline when achieved. **Update:** best-baseline replacement or EWMA/SPC tracking. citeturn32view0 | Compare actual performance to manufacturer/best baseline using model residuals and control charts; after problems are corrected, performance should approach the original baseline for the same load condition. citeturn32view0turn34search1 | Open evidence is weaker than in nuclear/aviation, but industrial BMS/FDD implementations, ASHRAE-aligned metrics such as IPLV, and practical maintenance literature all converge on baseline-model comparison for long-term monitoring. citeturn32view0turn34search1turn30search6 |

**Comparative conclusion.** The most mature pattern is: **individual-equipment baseline + operating-condition normalization + event-triggered re-baselining + preserved lifecycle history**. Pure rolling baselines and pure fleet baselines appear mostly as supporting mechanisms, not as the primary answer to maintenance discontinuities. citeturn12view0turn22view0turn29view0turn32view0

## Maintenance event classification and baseline strategies

A usable Q4b design needs to classify maintenance events by **scope of physical restoration** and **scope of observability change**. That is how mature systems avoid conflating “health recovery,” “normal operational shift,” and “sensor artifact.” The classification below is the minimum structure needed to make baseline management auditable. The logic is inferred from nuclear configuration-control practice, aircraft ETM step-shift interpretation, gas-turbine wash-cycle segmentation, rotating-machinery post-overhaul baselining, and chiller baseline-model management. citeturn9view3turn15view1turn23view1turn29view0turn32view0

| Event class | Typical examples | What it really means | Baseline action | HI / trend implication |
|---|---|---|---|---|
| **Major restorative intervention** | Major overhaul, hot-section restoration, rotor/bearing/impeller replacement, full turbocharger rebuild | Physical health state has materially changed. Pre- and post-event residual distributions are not commensurate. | **Full reset** of affected asset/subsystem baseline; open a new maintenance segment. citeturn29view0turn12view0 | Start a new segment-local HI; carry forward asset history only through metadata such as event type, workscope, and restoration factor. citeturn13view0turn36search12 |
| **Partial restorative intervention** | Injector replacement, valve replacement, filter replacement, localized cleaning | Some channels should improve abruptly; others should not. | **Partial reset** only for affected residuals/features/subsystem models. citeturn15view1turn29view1 | Do not reset unrelated HIs. Preserve unaffected trends. |
| **Recoverable fouling removal** | Compressor wash, heat-exchanger/chiller tube cleaning, air-path cleaning | Restores recoverable performance loss but does not erase irreversible aging. | **Cycle-local reset** to a clean-condition anchor; retain long-term trend on successive post-clean anchors. citeturn22view0turn23view1turn34search1 | Best represented as two linked trends: short-term recoverable loss and long-term irreversible degradation. citeturn22view0turn23view1 |
| **Measurement-chain intervention** | Sensor recalibration, transmitter replacement, DAQ channel swap, rewiring | Apparent step change may be instrumentation, not equipment recovery. | **Sensor-baseline reset only**; no automatic health recovery claim. Require sensor validation first. citeturn9view2turn35search19turn35search2 | HI/trend should be held or re-expressed only after measurement consistency checks. |
| **Control / software / configuration intervention** | Firmware change, governor tuning, control logic update, setpoint changes | Expected-state manifold changes. Raw residuals may shift even if hardware health does not. | **Model/version update** and possibly baseline reset for control-dependent residuals. citeturn9view3turn32view0 | Create a new model version tag; trend continuity only after re-normalization. |
| **Operating-context shift** | Seasonal ambient change, mission profile change, different fuel, load regime change | Context changed, not necessarily health. | **No reset** if physics/context normalization handles it; otherwise retrain/update contextual normalizer, not health state. citeturn14view0turn22view0turn38search17 | Continue segment, but only with proper contextual correction. |

### Distinguishing recovery, variation, and sensor artifacts

Industrial systems do not rely on a single signal step. They use **coincidence of event logs, changepoints, operating-condition normalization, cross-sensor consistency, and post-maintenance verification windows**. In aircraft ETM, gradual deterioration appears as drift in parameter deltas, while maintenance can create abrupt step shifts; the A320 example shows an abrupt Delta-EGT shift and another shift after valve replacement, which maintenance analysts specifically interpret as event signatures rather than ordinary drift. citeturn15view1turn14view0

A practical discrimination rule is:

- **True health recovery**: coherent improvement across physically linked residuals after a declared maintenance event, confirmed in a stable operating window and consistent with expected performance relationships. Gas turbine wash-cycle studies show after-wash power-related indicators improve while long-term after-wash anchors still reveal irreversible degradation. citeturn22view0turn23view1  
- **Normal operational variation**: apparent shift disappears or shrinks after ambient/load/mission normalization. Aircraft trend monitoring explicitly corrects for ambient and thrust conditions, and gas-turbine studies explicitly remove ambient-temperature influence before estimating short- and long-term deterioration. citeturn14view0turn22view0  
- **Sensor artifact**: isolated or implausible channel movement, inconsistent with mass/energy balance or with companion sensors; nuclear and HVAC literature both treat sensor drift/recalibration as a distinct problem that must be estimated or recalibrated rather than interpreted as equipment health change. citeturn35search0turn35search19turn35search2

### Baseline strategy survey

The table below is a practical survey of the strategies relevant to Q4b. “Marine suitability” is an engineering assessment based on the literature and on the operational constraints stated in your brief.

| Strategy | Concept | Published / industrial example | Main advantage | Main failure mode | Marine suitability |
|---|---|---|---|---|---|
| **Static baseline** | Fixed reference from initial healthy / commissioned state | Nuclear commissioning/startup baseline criteria; manufacturer new-engine baseline in aviation. citeturn8view0turn14view0 | Simple, auditable | Becomes stale with aging, maintenance, and environment | **Low** |
| **Adaptive baseline** | Reference model updated as new data arrives | Chiller “best baseline” model can replace the prior baseline when higher IPLV/COP is achieved; adaptive gas-path methods exist for turbine health estimation. citeturn32view0turn21search18 | Handles slow drift and missing factory baseline | Can absorb true degradation if update policy is too permissive | **Medium** |
| **Rolling baseline** | Short moving-window reference | Chiller EWMA/SPC monitoring uses recent model error history; many FDD systems use moving statistics. citeturn32view0 | Good for noise suppression and recent drift | Can erase long-memory degradation and confound maintenance discontinuities | **Medium** |
| **Multi-segment baseline** | Separate baseline per maintenance / wash / shop-visit segment | MTU workscope-specific deterioration and shop-visit effects; gas turbine after-wash vs after-wash long-term trend; imperfect-maintenance and multi-phase degradation literature. citeturn13view0turn23view1turn36search12turn37search0 | Preserves history without forcing false continuity | Requires event labeling, segment metadata, and lifecycle-aware analytics | **High** |
| **Fleet-based baseline** | Use population of similar assets to define expected behavior | MTU uses fleet-average and single-engine deterioration rates; CMAPSS/N-CMAPSS encode fleet variability. citeturn13view0turn42view0turn43search0 | Useful for new assets and peer ranking | Needs sufficient comparable fleet data; can hide individual peculiarities | **Low** for your current project |
| **Physics-informed baseline** | First-principles expected-state model | Nuclear online monitoring / MSET-type models; aircraft thermodynamic engine models; chiller model-based baseline; gas-turbine GPA. citeturn10search12turn12view0turn32view0turn21search18 | Interpretable, portable across contexts | Higher modeling/calibration cost | **Medium** |
| **Hybrid baseline** | Physics + data-driven correction / normalization | Chiller hybrid FDD, aircraft ETM with thermodynamic model plus historical pattern matching, gas-turbine analytics with normalized performance indices. citeturn12view0turn22view0turn31search0 | Best balance of interpretability and adaptability | Implementation complexity and governance burden | **High** |

**Recommended strategy.** For ship systems, the best fit is **multi-segment baseline + hybrid expected-state model**. Static baselines are too brittle for long deployments; fully adaptive baselines risk hiding gradual degradation; pure rolling baselines discard the long memory that makes HI/trend valuable. citeturn13view0turn23view1turn36search12turn32view0

## Dataset audit for Q4b validation

### Audit result

No priority public benchmark retrieved in this review provides **documented maintenance events with restart-to-failure continuation**. The priority aviation and bearing datasets are overwhelmingly **run-to-failure** benchmarks. This is consistent with NASA’s own explanation of the data bottleneck: monitored field systems are often prevented from running to failure **or are subject to maintenance that eliminates fault-evolution signatures**, which is precisely why maintenance-aware PHM validation has poor public benchmark support. citeturn42view0turn43search0turn41view1turn1search6turn2search18turn41view0turn43search2

| Rank | Dataset | Maintenance events | Multi-lifecycle segments | Q4b suitability | Status | Notes |
|---|---|---:|---:|---|---|---|
| 1 | **N-CMAPSS** | **No** citeturn42view0 | **No** real maintenance-restart cycles; synthetic run-to-failure only. citeturn42view0 | **Low** as direct Q4b evidence; **best surrogate** for segmentation under variable operating conditions | **Not suitable for direct Q4b; suitable as surrogate** | Public challenge documentation says it uses run-to-failure degradation trajectories of 100 engines under real flight conditions, with seven failure modes and cycle structure. citeturn42view0 |
| 2 | **LBNL / OpenEI chiller plant FDD datasets** | **No documented real maintenance events** in the retrieved dataset descriptions. citeturn39search5turn39search25 | **Partial** fault-free/faulted states across simulation/lab/field, but not maintenance-reset-restart lifecycles. citeturn39search25turn39search14 | **Low** | **Not suitable for direct Q4b** | Useful for faulted/fault-free and context-normalized HVAC modeling, not for maintenance-event baseline resets. citeturn39search25turn39search2 |
| 3 | **CMAPSS original** | **No** citeturn43search0turn43search1 | **No**. Each engine develops a fault and training data continue until failure. citeturn43search0turn43search1 | **Low** | **Not suitable** | Classic run-to-failure benchmark with multiple operating conditions and sensor noise, but no maintenance events. citeturn43search0 |
| 4 | **PHM 2008 challenge dataset** | **No** citeturn41view1 | **No**. Multiple engines, each with degradation trajectories only. citeturn41view1 | **Low** | **Not suitable** | Same structural limitation as CMAPSS. citeturn41view1 |
| 5 | **PRONOSTIA / FEMTO bearings** | **No evidence of maintenance events**; challenge framing is bearing degradation to failure. citeturn2search18 | **No** | **Not suitable** | **Not suitable** | The platform/challenge is widely used for bearing degradation prognosis, not maintenance-reset studies. citeturn2search18 |
| 6 | **XJTU-SY bearing dataset** | **No** citeturn2search18 | **No** | **Not suitable** | **Not suitable** | Public description emphasizes complete run-to-failure sampling of bearings. citeturn2search18 |
| 7 | **IMS bearing dataset** | **No** explicit maintenance events in dataset description. citeturn41view0 | **No** | **Not suitable** | **Not suitable** | NASA page describes bearing experiments and degradation/prognostics use, but not maintenance segmentation. citeturn41view0 |
| 8 | **Public HVAC datasets with documented maintenance logs** | **Unknown** | **Unknown** | **Unknown / likely low** | **Unknown — needs further investigation** | This review found public labeled fault datasets and operational datasets, but not a high-confidence public benchmark with explicit service logs and post-maintenance restart segments. citeturn39search2turn39search25turn39search27 |
| 9 | **Public industrial rotating datasets with maintenance logs** | **Unknown** | **Unknown** | **Unknown / likely low** | **Unknown — needs further investigation** | No authoritative public benchmark with explicit maintenance-event annotations was identified in the retrieved sources. citeturn40search1turn29view0 |

### Dataset choice for starting work

If you must start with one dataset now, use **N-CMAPSS** for **Validation C**, with the research question framed narrowly:

> **Can a segment-aware baseline and normalization pipeline preserve `Residual → HI → Trend` under large operating-context variability, and can it recover stable trend interpretation when synthetic maintenance-reset events are inserted?**

That is defensible because N-CMAPSS gives you operating context (`w`), measured signals (`xs`), cycle IDs, flight classes, multiple fault modes, and run-to-failure health evolution. It does **not** validate real maintenance semantics, but it is the best public substrate for building the mechanics you will later test on real maintenance logs. citeturn42view0

## Trend continuity and baseline-management failure modes

### How mature systems connect pre- and post-maintenance trends

The dominant industrial pattern is:

1. **Do not force absolute continuity of the health indicator across a major maintenance event.**  
2. **Preserve full asset history and event markers.**  
3. **Start a new segment baseline for the post-maintenance period.**  
4. **Connect segments through restoration metadata** such as regained performance, workscope, or virtual age. citeturn13view0turn23view1turn29view0turn36search12turn36search0

Aircraft EHM expresses this clearly. MTU tracks cycles since installation, workscope-specific deterioration, and shop-visit regained performance, while still keeping fleet and engine history. Gas turbine monitoring similarly treats each wash interval as a segment: the short-term deterioration is measured within the cycle, and long-term deterioration is measured across after-wash anchors. Rotating-machinery guidance explicitly states that overhaul/repair can invalidate the previous baseline, requiring a new baseline. In reliability literature, imperfect maintenance is modeled as moving the system to a state somewhere between “as good as new” and “as bad as old,” often expressed through **virtual age** or multi-phase degradation models. citeturn13view0turn23view1turn29view0turn36search12turn36search0turn37search0

That implies the following representation for your use case:

```text
Asset history
 ├─ Segment S0: baseline_0, HI_0(t), trend_0(t) until maintenance M1
 ├─ Maintenance marker M1: type, scope, affected subsystem, sensor/config version
 ├─ Commissioning window after M1: stable data + post-maintenance verification
 ├─ Segment S1: baseline_1, HI_1(t), trend_1(t)
 └─ Cross-segment link: restoration factor / virtual age / regained-performance delta
```

This keeps the validated chain intact by making `Residual → HI → Trend` **segment-local**, while `Maintenance Event → Baseline Reset → Long-Term Monitoring` becomes the **asset-level orchestration layer**. That is the cleanest way to avoid mathematically meaningless concatenation of pre- and post-maintenance residual histories. citeturn9view0turn13view0turn23view1turn36search12

### Failure modes and mitigations

| Failure mode | Consequence | Practical mitigation |
|---|---|---|
| **False recovery detection**: maintenance artifact is interpreted as true health recovery | HI drops or improves even though the change is only local, temporary, or measurement-related | Require maintenance log correlation, stable operating window, and multi-sensor/physics-consistency confirmation. Gas-turbine work shows servicing during a wash can create a larger-than-normal step change; do not treat every upward step as uniform recovery. citeturn22view0 |
| **Sensor replacement / calibration step change mistaken as health shift** | Trend discontinuity contaminates residual distribution and HI | Separate sensor-baseline reset from health-baseline reset; estimate/calibrate sensor drift explicitly and hold health trend until sensor validation passes. Nuclear and HVAC literature both treat sensor drift as its own diagnostic problem. citeturn35search0turn35search19turn35search2 |
| **Baseline drift due to gradual environmental change** | Residual loses meaning; alert thresholds shift silently | Use contextual normalization (ambient/load/mission) before HI computation. Aircraft and gas-turbine monitoring both correct/normalize before delta analysis. citeturn14view0turn22view0 |
| **Seasonal / operational variability masks degradation** | Real degradation is hidden behind environment-driven signal movement | Include environment and operating condition variables explicitly in the expected-state model; SHM literature shows environmental/operational changes can mask damage signatures if untreated. citeturn38search17turn38search1 |
| **Over-resetting** | You destroy long-term trend memory and lose cumulative degradation context | Restrict full resets to classified restorative/configuration events; otherwise use no reset or partial reset. Support cross-segment virtual age instead of frequent full zeroing. citeturn36search12turn36search0 |
| **Under-resetting** | Stale baseline makes residuals non-stationary and HI invalid after maintenance | When repair/overhaul invalidates reference behavior, explicitly open a new segment. This is codified in rotating-machinery guidance and implied in nuclear configuration-control practice. citeturn29view0turn9view3 |
| **Adaptive baseline absorbing true degradation** | Slow deterioration disappears into the moving reference | Keep adaptive updates bounded and subordinate to maintenance segments; do not let long-term baseline learning proceed unchecked during suspected degradation periods. Chiller “best baseline” logic only replaces the baseline when performance is demonstrably better, not merely different. citeturn32view0 |

## Marine mapping and recommended architecture

### System-level mapping

The table below is an inference from the industrial survey, aligned to ship machinery behavior.

| Marine system | Typical maintenance events | Baseline reset challenge | Recommended strategy |
|---|---|---|---|
| **Diesel generator** | Injector replacement, turbo cleaning, governor update, major overhaul | Need to separate injector/turbo recovery from load, ambient, and fuel-quality variation | **Hybrid + multi-segment baseline.** Use engine-specific expected-state residuals; full reset for overhaul, partial reset for injector/turbo events, model-version update for governor/software changes. This mirrors aircraft/gas-turbine practice. citeturn14view0turn12view0turn22view0 |
| **Central cooling system / chiller-like seawater-freshwater loop** | Heat-exchanger cleaning, pump overhaul, sensor recalibration | Fouling removal creates large efficiency step changes; sensor recalibration can imitate recovery | **Physics-informed baseline + maintenance markers + partial/full segment logic.** Treat cleaning as a clean-anchor reset for thermal-performance indicators, not as history erasure. This mirrors chiller and gas-turbine wash-cycle practice. citeturn23view1turn32view0turn34search1 |
| **Air compressor** | Valve replacement, filter change, bearing replacement | Pressure build-up and efficiency can jump after maintenance, but some components remain aged | **Partial-reset multi-segment baseline.** Reset affected performance/vibration indicators only; preserve motor/drive trend if untouched. This mirrors rotating-machinery baseline practice. citeturn29view0turn29view1 |
| **Turbocharger** | Washing/cleaning, bearing replacement, rotor balancing | Cleanings create recoverable performance restoration; bearing work changes vibration signature abruptly | **Dual-timescale baseline.** Short-term clean-vs-fouled segment baseline plus long-term post-clean anchor trend, with vibration baseline re-established after bearing/balance work. This mirrors gas-turbine and rotating-machinery practice. citeturn23view1turn29view1 |

### Recommended ship PHM architecture

The recommended architecture for Ship System Health Monitoring is:

| Layer | Function | Design recommendation |
|---|---|---|
| **Expected-state layer** | Compute residuals with environmental / operational normalization | Use a **physics-informed or hybrid expected-state model** per subsystem, so normal mission/load/ambient shifts are removed before health inference. citeturn14view0turn22view0turn32view0 |
| **Event layer** | Detect/classify maintenance or configuration changes | Combine maintenance logs with changepoint detection; classify events into restorative, measurement-chain, software/configuration, and context-only categories. citeturn9view3turn15view1turn35search0 |
| **Segment layer** | Manage baselines across lifecycle discontinuities | Store **baseline segments** keyed by event ID, affected subsystem, and sensor/model version. Full reset only when the prior baseline is invalidated. citeturn29view0turn9view0 |
| **HI layer** | Compute health indicators | Compute HI **within segment**, not globally across the whole asset life. Use affected-subsystem scope for partial resets. |
| **Trend layer** | Trend continuation across maintenance | Preserve asset-level history with maintenance markers; connect segment trends through **restoration factor / virtual age / regained-performance delta**, not by concatenating raw HIs. citeturn13view0turn36search12turn36search0 |
| **Governance layer** | Operational acceptance of resets | Require post-maintenance stable-data window, sensor validation, and acceptance-test checks before a new segment becomes “current.” This is directly aligned with nuclear post-maintenance verification logic. citeturn9view0 |

This architecture is the cleanest way to preserve the scientific validity of your chain:

```text
Residual → HI → Trend
```

without pretending that maintenance discontinuities do not exist. The chain remains valid **inside each segment**, and the long-term deployment problem is handled by the segment/governance layer. citeturn23view1turn29view0turn36search12

## Research roadmap and decision path

### Recommended validation sequence

**Validation C** should use **N-CMAPSS** as a surrogate benchmark for segmentation mechanics, not for real maintenance semantics. The concrete question should be:

> Can segment-aware residual normalization and segment-local HI computation preserve trend interpretability under highly variable operating conditions, and can synthetic reset events be handled without corrupting long-term asset history?

Use cycle boundaries, fault-onset timing, and the available operating-context variables to evaluate static, adaptive, and multi-segment baselines. If you inject synthetic “maintenance” events, keep the claim narrow: this is **method validation**, not real-world maintenance validation. citeturn42view0

**Validation D** should be the first **real Q4b** test on a marine generator or closely analogous asset with explicit maintenance records. The question should be:

> After injector replacement / overhaul / turbo cleaning, can the monitoring stack distinguish true recovered performance from normal load/context variation and from sensor or calibration artifacts?

Success criterion: post-maintenance residuals re-stationarize within the new segment, unrelated residuals do not falsely reset, and long-term asset history remains explorable across events. This design is directly motivated by aircraft engine step-shift analysis, gas-turbine wash-cycle segmentation, and rotating-machinery post-overhaul baselining. citeturn15view1turn23view1turn29view0

**Validation E**, if possible, should target a **marine cooling or turbocharging subsystem** where maintenance-induced thermal/performance steps are common and easier to observe than catastrophic failures. The question should be:

> Does a clean-anchor or post-service anchor baseline preserve both short-term recovery semantics and long-term irreversible degradation trend?

This is the nearest marine analog to gas-turbine after-wash logic and chiller best-baseline logic. citeturn23view1turn32view0turn34search1

### Final recommendation

For deployment, implement **event-aware multi-segment baseline management with hybrid expected-state models**. Concretely:

- Treat **major restorative maintenance** as a **new health segment**.  
- Treat **localized restorative maintenance** as a **partial reset** on affected channels only.  
- Treat **sensor/calibration interventions** as **measurement resets**, not health resets.  
- Treat **software/configuration changes** as **model-version changes** that may require re-normalization.  
- Keep the **full asset history**, but compute HI and trend **inside the current valid segment**.  

That is the most defensible, standards-aligned, and marine-feasible path from:

```text
Residual → HI → Trend
```

to:

```text
Maintenance Event → Baseline Reset → Long-Term Health Monitoring
```

because it matches how mature PHM domains already manage discontinuities while preserving interpretability and operational auditability. citeturn9view0turn17view0turn23view1turn29view0turn32view0turn36search12

### Open questions and limitations

Public evidence is strong on **how mature industries operationally handle baselines**, but weak on **open benchmark datasets with explicit maintenance-restart lifecycles**. The open dataset conclusion is therefore high-confidence in the negative direction: the common public PHM benchmarks reviewed here are not direct Q4b validators. What remains incomplete is identification of a public dataset with trustworthy maintenance annotations and post-maintenance restart segments; none was confirmed in the retrieved sources. citeturn42view0turn43search0turn41view1turn1search6turn2search18turn41view0turn39search25