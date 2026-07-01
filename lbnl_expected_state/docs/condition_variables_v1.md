# Condition Variables v1

Status

Frozen.

Purpose

Execute the frozen Condition Variable Selection Decision Protocol to produce Condition Variables v1.

No Expected State model was trained. No correlations, statistical feature selection, plots, residuals, normalization, or feature importance were produced.

Inputs

* Engineering Variable Taxonomy
* Condition Variable Selection Protocol
* Data Quality Audit Report
* Task B constant-column audit
* Dataset column names

---

## Section 1 - Condition Variables v1

Accepted variables only.

### Environment

* OA_TEMP
* OA_TEMP_WB

### Demand / Load

* CWL_SEC_LOAD

### Flow

* CDWL_CW_FLOW
* CWL_PRI_CW_FLOW
* CWL_SEC_CW_FLOW

### Setpoint

* CT_SW_TEMPSPT
* CWL_PRI_SW_TEMPSPT

---

## Section 2 - Rejected Variables

| Variable | Reason Code | Evidence |
| -------- | ----------- | -------- |
| Datetime | TIME_INDEX | Time index; not an operating condition descriptor under Rule 1 |
| CDWL_PM_POW_1 | HEALTH_LEAKAGE | Power measurement reflects equipment energy response |
| CDWL_PM_POW_2 | HEALTH_LEAKAGE | Power measurement reflects equipment energy response |
| CDWL_PM_POW_3 | HEALTH_LEAKAGE | Power measurement reflects equipment energy response |
| CDWL_RW_TEMP | HEALTH_LEAKAGE | Process return-water temperature may encode heat-transfer and equipment response |
| CDWL_SW_TEMP | HEALTH_LEAKAGE | Process supply-water temperature may encode heat-transfer and equipment response |
| CHL_COMP_SPD_CTRL_1 | HEALTH_LEAKAGE | Controller output rejected by default under Rule 4 |
| CHL_COMP_SPD_CTRL_2 | HEALTH_LEAKAGE | Controller output rejected by default under Rule 4 |
| CHL_COMP_SPD_CTRL_3 | HEALTH_LEAKAGE | Controller output rejected by default under Rule 4 |
| CHL_POW_1 | TARGET | Chiller power is the experiment prediction target family |
| CHL_POW_2 | TARGET | Chiller power is the experiment prediction target family |
| CHL_POW_3 | TARGET | Chiller power is the experiment prediction target family |
| CHL_SWCD_TEMP_1 | HEALTH_LEAKAGE | Chiller condenser-side temperature may encode heat-transfer and equipment response |
| CHL_SWCD_TEMP_2 | HEALTH_LEAKAGE | Chiller condenser-side temperature may encode heat-transfer and equipment response |
| CHL_SWCD_TEMP_3 | HEALTH_LEAKAGE | Chiller condenser-side temperature may encode heat-transfer and equipment response |
| CHL_RW_TEMP_1 | HEALTH_LEAKAGE | Chiller return-water temperature may encode heat-transfer and equipment response |
| CHL_RW_TEMP_2 | HEALTH_LEAKAGE | Chiller return-water temperature may encode heat-transfer and equipment response |
| CHL_RW_TEMP_3 | HEALTH_LEAKAGE | Chiller return-water temperature may encode heat-transfer and equipment response |
| CHL_STA_1 | CONSTANT | Task B constant audit reports 1 unique value and 100 percent occupancy |
| CHL_STA_2 | HEALTH_LEAKAGE | Equipment status may encode equipment availability or operating state |
| CHL_STA_3 | HEALTH_LEAKAGE | Equipment status may encode equipment availability or operating state |
| CHL_RWCD_TEMP_1 | HEALTH_LEAKAGE | Chiller condenser return-water temperature may encode heat-transfer and equipment response |
| CHL_RWCD_TEMP_2 | HEALTH_LEAKAGE | Chiller condenser return-water temperature may encode heat-transfer and equipment response |
| CHL_RWCD_TEMP_3 | HEALTH_LEAKAGE | Chiller condenser return-water temperature may encode heat-transfer and equipment response |
| CHL_SW_TEMP_1 | HEALTH_LEAKAGE | Chiller supply-water temperature may encode heat-transfer and equipment response |
| CHL_SW_TEMP_2 | HEALTH_LEAKAGE | Chiller supply-water temperature may encode heat-transfer and equipment response |
| CHL_SW_TEMP_3 | HEALTH_LEAKAGE | Chiller supply-water temperature may encode heat-transfer and equipment response |
| CT_FAN_SPD_1 | HEALTH_LEAKAGE | Actuator speed may encode controller response and equipment compensation |
| CT_FAN_SPD_2 | HEALTH_LEAKAGE | Actuator speed may encode controller response and equipment compensation |
| CT_FAN_SPD_3 | HEALTH_LEAKAGE | Actuator speed may encode controller response and equipment compensation |
| CT_FAN_SPD_CTRL_1 | HEALTH_LEAKAGE | Controller output rejected by default under Rule 4 |
| CT_FAN_SPD_CTRL_2 | HEALTH_LEAKAGE | Controller output rejected by default under Rule 4 |
| CT_FAN_SPD_CTRL_3 | HEALTH_LEAKAGE | Controller output rejected by default under Rule 4 |
| CT_POW_1 | HEALTH_LEAKAGE | Power measurement reflects equipment energy response |
| CT_POW_2 | HEALTH_LEAKAGE | Power measurement reflects equipment energy response |
| CT_POW_3 | HEALTH_LEAKAGE | Power measurement reflects equipment energy response |
| CT_RW_TEMP_1 | HEALTH_LEAKAGE | Cooling-tower return-water temperature may encode heat-rejection and equipment response |
| CT_RW_TEMP_2 | HEALTH_LEAKAGE | Cooling-tower return-water temperature may encode heat-rejection and equipment response |
| CT_RW_TEMP_3 | HEALTH_LEAKAGE | Cooling-tower return-water temperature may encode heat-rejection and equipment response |
| CT_STA_1 | CONSTANT | Task B constant audit reports 1 unique value and 100 percent occupancy |
| CT_STA_2 | HEALTH_LEAKAGE | Equipment status may encode equipment availability or operating state |
| CT_STA_3 | HEALTH_LEAKAGE | Equipment status may encode equipment availability or operating state |
| CT_SW_TEMP_1 | HEALTH_LEAKAGE | Cooling-tower supply-water temperature may encode heat-rejection and equipment response |
| CT_SW_TEMP_2 | HEALTH_LEAKAGE | Cooling-tower supply-water temperature may encode heat-rejection and equipment response |
| CT_SW_TEMP_3 | HEALTH_LEAKAGE | Cooling-tower supply-water temperature may encode heat-rejection and equipment response |
| CWL_PRI_PM_POW_1 | HEALTH_LEAKAGE | Power measurement reflects equipment energy response |
| CWL_PRI_PM_POW_2 | HEALTH_LEAKAGE | Power measurement reflects equipment energy response |
| CWL_PRI_PM_POW_3 | HEALTH_LEAKAGE | Power measurement reflects equipment energy response |
| CWL_PRI_RW_TEMP | HEALTH_LEAKAGE | Primary loop return-water temperature may encode heat-transfer and equipment response |
| CWL_PRI_SW_TEMP | HEALTH_LEAKAGE | Primary loop supply-water temperature may encode heat-transfer and equipment response |
| CWL_SEC_DP | HEALTH_LEAKAGE | Secondary differential pressure may encode pump/control response |
| CWL_SEC_DPSPT | CONSTANT | Task B constant audit reports 1 unique value and 100 percent occupancy |
| CWL_SEC_PM_POW_1 | HEALTH_LEAKAGE | Power measurement reflects equipment energy response |
| CWL_SEC_PM_POW_2 | HEALTH_LEAKAGE | Power measurement reflects equipment energy response |
| CWL_SEC_PM_SPD_1 | HEALTH_LEAKAGE | Actuator speed may encode controller response and equipment compensation |
| CWL_SEC_PM_SPD_2 | HEALTH_LEAKAGE | Actuator speed may encode controller response and equipment compensation |
| CWL_SEC_PM_STA_1 | CONSTANT | Task B constant audit reports 1 unique value and 100 percent occupancy |
| CWL_SEC_PM_STA_2 | HEALTH_LEAKAGE | Equipment status may encode equipment availability or operating state |
| CWL_SEC_RW_TEMP | HEALTH_LEAKAGE | Secondary loop return-water temperature may encode heat-transfer and equipment response |
| CWL_SEC_SW_TEMP | HEALTH_LEAKAGE | Secondary loop supply-water temperature may encode heat-transfer and equipment response |
| TWV_CTRL | HEALTH_LEAKAGE | Controller output rejected by default under Rule 4 |

---

## Section 3 - Representative Standby Variables

| Variable | Representative Variable | Engineering Group | Engineering Justification | Reason Code |
| -------- | ----------------------- | ----------------- | ------------------------- | ----------- |
| CHL_CD_FLOW_1 | CDWL_CW_FLOW | Condenser water flow | Chiller-level condenser water branch flow; plant-level condenser water flow is the representative operating-condition measure. | REDUNDANT_STANDBY |
| CHL_CD_FLOW_2 | CDWL_CW_FLOW | Condenser water flow | Chiller-level condenser water branch flow; plant-level condenser water flow is the representative operating-condition measure. | REDUNDANT_STANDBY |
| CHL_CD_FLOW_3 | CDWL_CW_FLOW | Condenser water flow | Chiller-level condenser water branch flow; plant-level condenser water flow is the representative operating-condition measure. | REDUNDANT_STANDBY |
| CHL_CW_FLOW_1 | CWL_PRI_CW_FLOW | Primary chilled-water flow | Chiller-level chilled-water branch flow; primary-loop chilled-water flow is the representative operating-condition measure. | REDUNDANT_STANDBY |
| CHL_CW_FLOW_2 | CWL_PRI_CW_FLOW | Primary chilled-water flow | Chiller-level chilled-water branch flow; primary-loop chilled-water flow is the representative operating-condition measure. | REDUNDANT_STANDBY |
| CHL_CW_FLOW_3 | CWL_PRI_CW_FLOW | Primary chilled-water flow | Chiller-level chilled-water branch flow; primary-loop chilled-water flow is the representative operating-condition measure. | REDUNDANT_STANDBY |
| CT_FLOW_1 | CDWL_CW_FLOW | Condenser water flow | Cooling-tower branch flow; plant-level condenser water flow is the representative operating-condition measure. | REDUNDANT_STANDBY |
| CT_FLOW_2 | CDWL_CW_FLOW | Condenser water flow | Cooling-tower branch flow; plant-level condenser water flow is the representative operating-condition measure. | REDUNDANT_STANDBY |
| CT_FLOW_3 | CDWL_CW_FLOW | Condenser water flow | Cooling-tower branch flow; plant-level condenser water flow is the representative operating-condition measure. | REDUNDANT_STANDBY |

### Representative Selection Summary

| Engineering Group | Representative | Engineering Justification |
| ----------------- | -------------- | ------------------------- |
| Condenser water flow | CDWL_CW_FLOW | Plant-level condenser water flow represents the shared condenser-water operating condition more directly than chiller-level or tower-level branch measurements. |
| Primary chilled-water flow | CWL_PRI_CW_FLOW | Primary-loop chilled-water flow represents the primary chilled-water operating condition more directly than individual chiller branch measurements. |
| Secondary chilled-water flow | CWL_SEC_CW_FLOW | Secondary-loop chilled-water flow represents the distribution-side chilled-water operating condition and has no same-quantity standby selected in v1. |

---

## Section 4 - Evidence Traceability Table

Every dataset variable appears exactly once.

| Variable | Decision | Evidence | Reason Code |
| -------- | -------- | -------- | ----------- |
| Datetime | Reject | Time index; not an operating condition descriptor under Rule 1 | TIME_INDEX |
| CDWL_CW_FLOW | Accept | Plant-level condenser water flow representative; engineering taxonomy Flow | CONDITION |
| CDWL_PM_POW_1 | Reject | Power measurement reflects equipment energy response | HEALTH_LEAKAGE |
| CDWL_PM_POW_2 | Reject | Power measurement reflects equipment energy response | HEALTH_LEAKAGE |
| CDWL_PM_POW_3 | Reject | Power measurement reflects equipment energy response | HEALTH_LEAKAGE |
| CDWL_RW_TEMP | Reject | Process return-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CDWL_SW_TEMP | Reject | Process supply-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CHL_CD_FLOW_1 | Standby | Chiller-level condenser water branch flow; CDWL_CW_FLOW selected as plant-level representative | REDUNDANT_STANDBY |
| CHL_CD_FLOW_2 | Standby | Chiller-level condenser water branch flow; CDWL_CW_FLOW selected as plant-level representative | REDUNDANT_STANDBY |
| CHL_CD_FLOW_3 | Standby | Chiller-level condenser water branch flow; CDWL_CW_FLOW selected as plant-level representative | REDUNDANT_STANDBY |
| CHL_COMP_SPD_CTRL_1 | Reject | Controller output rejected by default under Rule 4 | HEALTH_LEAKAGE |
| CHL_COMP_SPD_CTRL_2 | Reject | Controller output rejected by default under Rule 4 | HEALTH_LEAKAGE |
| CHL_COMP_SPD_CTRL_3 | Reject | Controller output rejected by default under Rule 4 | HEALTH_LEAKAGE |
| CHL_CW_FLOW_1 | Standby | Chiller-level chilled water branch flow; CWL_PRI_CW_FLOW selected as primary-loop representative | REDUNDANT_STANDBY |
| CHL_CW_FLOW_2 | Standby | Chiller-level chilled water branch flow; CWL_PRI_CW_FLOW selected as primary-loop representative | REDUNDANT_STANDBY |
| CHL_CW_FLOW_3 | Standby | Chiller-level chilled water branch flow; CWL_PRI_CW_FLOW selected as primary-loop representative | REDUNDANT_STANDBY |
| CHL_POW_1 | Reject | Chiller power is the experiment prediction target family | TARGET |
| CHL_POW_2 | Reject | Chiller power is the experiment prediction target family | TARGET |
| CHL_POW_3 | Reject | Chiller power is the experiment prediction target family | TARGET |
| CHL_SWCD_TEMP_1 | Reject | Chiller condenser-side temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CHL_SWCD_TEMP_2 | Reject | Chiller condenser-side temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CHL_SWCD_TEMP_3 | Reject | Chiller condenser-side temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CHL_RW_TEMP_1 | Reject | Chiller return-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CHL_RW_TEMP_2 | Reject | Chiller return-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CHL_RW_TEMP_3 | Reject | Chiller return-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CHL_STA_1 | Reject | Task B constant audit reports 1 unique value and 100 percent occupancy | CONSTANT |
| CHL_STA_2 | Reject | Equipment status may encode equipment availability or operating state | HEALTH_LEAKAGE |
| CHL_STA_3 | Reject | Equipment status may encode equipment availability or operating state | HEALTH_LEAKAGE |
| CHL_RWCD_TEMP_1 | Reject | Chiller condenser return-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CHL_RWCD_TEMP_2 | Reject | Chiller condenser return-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CHL_RWCD_TEMP_3 | Reject | Chiller condenser return-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CHL_SW_TEMP_1 | Reject | Chiller supply-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CHL_SW_TEMP_2 | Reject | Chiller supply-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CHL_SW_TEMP_3 | Reject | Chiller supply-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CT_FAN_SPD_1 | Reject | Actuator speed may encode controller response and equipment compensation | HEALTH_LEAKAGE |
| CT_FAN_SPD_2 | Reject | Actuator speed may encode controller response and equipment compensation | HEALTH_LEAKAGE |
| CT_FAN_SPD_3 | Reject | Actuator speed may encode controller response and equipment compensation | HEALTH_LEAKAGE |
| CT_FAN_SPD_CTRL_1 | Reject | Controller output rejected by default under Rule 4 | HEALTH_LEAKAGE |
| CT_FAN_SPD_CTRL_2 | Reject | Controller output rejected by default under Rule 4 | HEALTH_LEAKAGE |
| CT_FAN_SPD_CTRL_3 | Reject | Controller output rejected by default under Rule 4 | HEALTH_LEAKAGE |
| CT_FLOW_1 | Standby | Cooling-tower branch flow; CDWL_CW_FLOW selected as plant-level condenser-water representative | REDUNDANT_STANDBY |
| CT_FLOW_2 | Standby | Cooling-tower branch flow; CDWL_CW_FLOW selected as plant-level condenser-water representative | REDUNDANT_STANDBY |
| CT_FLOW_3 | Standby | Cooling-tower branch flow; CDWL_CW_FLOW selected as plant-level condenser-water representative | REDUNDANT_STANDBY |
| CT_POW_1 | Reject | Power measurement reflects equipment energy response | HEALTH_LEAKAGE |
| CT_POW_2 | Reject | Power measurement reflects equipment energy response | HEALTH_LEAKAGE |
| CT_POW_3 | Reject | Power measurement reflects equipment energy response | HEALTH_LEAKAGE |
| CT_RW_TEMP_1 | Reject | Cooling-tower return-water temperature may encode heat-rejection and equipment response | HEALTH_LEAKAGE |
| CT_RW_TEMP_2 | Reject | Cooling-tower return-water temperature may encode heat-rejection and equipment response | HEALTH_LEAKAGE |
| CT_RW_TEMP_3 | Reject | Cooling-tower return-water temperature may encode heat-rejection and equipment response | HEALTH_LEAKAGE |
| CT_STA_1 | Reject | Task B constant audit reports 1 unique value and 100 percent occupancy | CONSTANT |
| CT_STA_2 | Reject | Equipment status may encode equipment availability or operating state | HEALTH_LEAKAGE |
| CT_STA_3 | Reject | Equipment status may encode equipment availability or operating state | HEALTH_LEAKAGE |
| CT_SW_TEMPSPT | Accept | Cooling tower supply-water temperature setpoint; engineering taxonomy Setpoint | CONDITION |
| CT_SW_TEMP_1 | Reject | Cooling-tower supply-water temperature may encode heat-rejection and equipment response | HEALTH_LEAKAGE |
| CT_SW_TEMP_2 | Reject | Cooling-tower supply-water temperature may encode heat-rejection and equipment response | HEALTH_LEAKAGE |
| CT_SW_TEMP_3 | Reject | Cooling-tower supply-water temperature may encode heat-rejection and equipment response | HEALTH_LEAKAGE |
| CWL_PRI_CW_FLOW | Accept | Primary chilled-water loop flow representative; engineering taxonomy Flow | CONDITION |
| CWL_PRI_PM_POW_1 | Reject | Power measurement reflects equipment energy response | HEALTH_LEAKAGE |
| CWL_PRI_PM_POW_2 | Reject | Power measurement reflects equipment energy response | HEALTH_LEAKAGE |
| CWL_PRI_PM_POW_3 | Reject | Power measurement reflects equipment energy response | HEALTH_LEAKAGE |
| CWL_PRI_RW_TEMP | Reject | Primary loop return-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CWL_PRI_SW_TEMP | Reject | Primary loop supply-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CWL_PRI_SW_TEMPSPT | Accept | Primary chilled-water supply temperature setpoint; engineering taxonomy Setpoint | CONDITION |
| CWL_SEC_CW_FLOW | Accept | Secondary chilled-water loop flow representative; engineering taxonomy Flow | CONDITION |
| CWL_SEC_DP | Reject | Secondary differential pressure may encode pump/control response | HEALTH_LEAKAGE |
| CWL_SEC_DPSPT | Reject | Task B constant audit reports 1 unique value and 100 percent occupancy | CONSTANT |
| CWL_SEC_LOAD | Accept | Secondary loop cooling load; engineering taxonomy Demand / Load | CONDITION |
| CWL_SEC_PM_POW_1 | Reject | Power measurement reflects equipment energy response | HEALTH_LEAKAGE |
| CWL_SEC_PM_POW_2 | Reject | Power measurement reflects equipment energy response | HEALTH_LEAKAGE |
| CWL_SEC_PM_SPD_1 | Reject | Actuator speed may encode controller response and equipment compensation | HEALTH_LEAKAGE |
| CWL_SEC_PM_SPD_2 | Reject | Actuator speed may encode controller response and equipment compensation | HEALTH_LEAKAGE |
| CWL_SEC_PM_STA_1 | Reject | Task B constant audit reports 1 unique value and 100 percent occupancy | CONSTANT |
| CWL_SEC_PM_STA_2 | Reject | Equipment status may encode equipment availability or operating state | HEALTH_LEAKAGE |
| CWL_SEC_RW_TEMP | Reject | Secondary loop return-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| CWL_SEC_SW_TEMP | Reject | Secondary loop supply-water temperature may encode heat-transfer and equipment response | HEALTH_LEAKAGE |
| OA_TEMP | Accept | Outdoor air dry-bulb temperature; engineering taxonomy Environment | CONDITION |
| OA_TEMP_WB | Accept | Outdoor air wet-bulb temperature; engineering taxonomy Environment | CONDITION |
| TWV_CTRL | Reject | Controller output rejected by default under Rule 4 | HEALTH_LEAKAGE |

---

## Section 5 - Summary

Total variables

78

Accepted

8

Rejected

61

Representative Standby

9

Verification

```text
Accepted + Rejected + Standby = 78

8 + 61 + 9 = 78
```

Pending variables

0

---

## Reviewer Review

Questions

1.

Does every accepted variable satisfy the engineering definition of Condition?

2.

Does any accepted variable risk encoding equipment health?

3.

Are any important operating conditions missing?

4.

Are any representative selections questionable?

Reviewer Decision

PASS

Reviewer Notes

No Pending variables remain. Every accepted variable belongs to a Candidate Condition Category from the frozen taxonomy. Controller Output and Equipment Status variables do not enter Condition Variables v1.
