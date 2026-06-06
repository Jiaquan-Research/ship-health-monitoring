# Baseline Management v0.1

> Extracted from `docs/baseline_management_v0.1.docx` because `docs/design/baseline_management_v0.1.md` was not present.

Baseline Management Design

Ship System Health Monitoring — Q4b Design Document

v0.1

2026.06.06  |  Design Only — Not Yet Implemented



## 1. Document Scope

本文档为船舶系统健康监控项目Q4b（Baseline Management）的设计文档。


| 项目 | 说明 |
| --- | --- |
| 用途 | 指导未来Validation D（教学船发电机数据）中Baseline Management的实现 |
| 依据 | 跨行业Deep Research调研（核工业/航空/燃气轮机/油气/HVAC，2026-06-06） |
| 状态 | 设计文档，尚未实现。所有设计均为预期架构，待真实Marine数据到手后验证。 |
| 范围 | v0.1仅覆盖柴油发电机（DG）。主机/冷却系统/空压机等系统留待后续版本。 |
| 不覆盖 | 算法实现细节、具体数学公式、参数设定（数据到手前无法确定） |


本文档直接服务于Validation D：教学船发电机数据到手后，按本文档定义的框架处理维护记录和基线重置逻辑。


## 2. Problem Definition

## 2.1 为什么需要Baseline Management

当前项目已验证：


Condition Variables → Expected State → Residual → HI → Trend


这条链路在单一健康状态下成立。但实际工业设备在运行过程中会经历维护事件，维护会导致设备状态发生阶跃性变化，直接破坏上述链路的有效性。


具体问题：

维护前：Residual随退化逐渐升高，HI和Trend正常跟踪

维护后：设备性能恢复，Residual突然下降

如果没有Baseline Management：系统无法区分'维护后正常恢复'和'传感器故障'或'数据异常'

长期后果：趋势分析失效，HI失去物理意义，无法支撑Validation D


## 2.2 主要失效模式

| 失效模式 | 描述 | 后果 |
| --- | --- | --- |
| 误判维护为故障 | 维护后Residual阶跃下降被误识别为传感器故障或数据异常 | 产生大量False Alarm，系统可信度崩塌 |
| 历史趋势丢失 | 维护后直接清零HI，丢失维护前的退化历史 | 无法跨维护周期分析长期健康趋势 |
| 基线漂移 | 使用全局静态baseline，无法区分不同维护周期的退化斜率 | 误判不同阶段的退化速率 |
| 传感器阶跃误判 | 传感器校准或更换导致的阶跃被误认为设备健康恢复 | 错误重置baseline，污染趋势数据 |
| 过度重置 | 每次小维护都触发full reset，导致趋势历史碎片化 | 无法积累长期退化证据 |


## 2.3 Failure Scenario（具体失效案例）

以下是没有Baseline Management时的典型失效场景：


| 时间 | 事件 | 系统行为（无BM） | 正确行为（有BM） |
| --- | --- | --- | --- |
| 2027-01 | 发电机#3缸喷油嘴积炭，燃烧效率下降 | Residual↑，HI↑，Trend上升，正常跟踪 | 同左，正常跟踪 |
| 2027-02
月底 | Residual继续升高，接近预警阈值 | HI接近告警边界 | 同左，标记为退化趋势加速 |
| 2027-03
月初 | 轮机员更换#3缸喷油嘴 | 无维护记录输入 | 记录维护事件：Partial Reset触发 |
| 2027-03
维护后 | 排温恢复正常，Residual突然下降 | 系统误判：传感器故障？数据异常？
或：HI直接归零，丢失历史趋势 | 识别为维护恢复，开启新Segment
保留历史退化记录作为资产元数据 |
| 2027-04 | 新喷油嘴开始正常退化 | 趋势基线混乱，无法判断新退化起点 | 从新Segment的clean baseline开始
独立跟踪新退化趋势 |


关键：没有Baseline Management，维护后的Residual变化无法被正确解释，长期健康监控无法成立。


## 3. Design Principles

以下设计原则来自跨行业调研（核工业、航空ETM、燃气轮机、油气旋转机械、HVAC），是成熟PHM系统的共同模式：


| 原则 | 含义 | 来源参考 |
| --- | --- | --- |
| Asset-specific baseline | 每台设备维护自己的baseline，不使用机队平均值作为唯一参考 | 航空ETM、油气旋转机械 |
| Event-triggered re-baselining | 维护事件触发baseline重建，不是定时重建，不是连续滑动 | 核工业、燃气轮机wash-cycle |
| Lifecycle history preservation | 维护后不删除历史数据，而是用metadata标记维护节点，保留资产完整生命周期记录 | 航空ETM、油气ABS/DNV规范 |
| Segment-internal computation | HI和Trend在当前有效Segment内计算，不跨越维护边界强行拼接绝对值 | 航空MTU ETM、燃气轮机PHM |
| Scope-matched reset | 重置范围与维护事件的物理影响范围匹配：局部维护只重置受影响的残差，不触发全局重置 | 油气DNV规范、HVAC best-baseline |
| Separation of concerns | 健康恢复 / 正常工况变化 / 传感器伪影，三种信号必须在处理逻辑上严格区分 | 核工业配置控制、航空ETM步变分析 |


跨行业共同结论：成熟PHM不是'一条baseline用到底'，而是multi-segment + event-triggered re-baselining + preserved lifecycle history的组合架构。


## 4. Event Taxonomy（维护事件分类框架）

所有维护事件按以下六类处理。分类依据是事件对物理健康状态和测量链的实际影响范围。


| 事件类型 | Marine发电机例子 | Reset范围 | 新Segment | HI/Trend处理 |
| --- | --- | --- | --- | --- |
| Major Restorative
（大修） | 发电机大修
发动机整体翻修 | Full Reset
所有残差和baseline重置 | Yes | 开启全新Segment
历史数据保留为资产元数据 |
| Partial Restorative
（局部修复） | 更换喷油嘴
更换缸套
更换轴承 | Partial Reset
仅受影响子系统/缸的残差重置 | Yes（局部） | 仅重置受影响部分的HI
不受影响的HI保持连续 |
| Recoverable Fouling Removal
（可恢复污垢清除） | 清洗涡轮增压器
清洗中冷器
清洗空冷器 | Clean-anchor Reset
以清洗后稳定状态为新锚点 | Yes（循环内） | 短期：可恢复损失趋势重置
长期：清洗后到清洗后的对比保持连续 |
| Measurement-chain Intervention
（测量链干预） | 排温传感器更换/校准
压力传感器校准 | Sensor Reset
仅重置该传感器的测量baseline | No | 先验证传感器一致性
再决定是否更新残差基线
不自动声明健康恢复 |
| Control/Config Change
（控制/配置变更） | 调速器参数调整
控制逻辑更新 | Model Version Update
依赖该控制信号的预测模型打版本标签 | No | 重新归一化后继续趋势
新旧版本模型结果不直接比较 |
| Operating-context Shift
（工况漂移） | 换季导致环境温度显著变化
港口/航行模式切换 | No Reset
工况归一化处理 | No | Segment内继续
工况归一化足以处理，不触发重置 |


## 4.1 事件分类判断流程

给定一个维护事件，按以下顺序判断处理方式：


Step 1: 是否涉及传感器/测量设备更换或校准？

→ Yes: Measurement-chain Intervention → Sensor Reset

→ No:  继续Step 2


Step 2: 是否涉及控制参数/软件/配置变更？

→ Yes: Control/Config Change → Model Version Update

→ No:  继续Step 3


Step 3: 是否只是工况/环境/负荷模式变化？

→ Yes: Operating-context Shift → No Reset

→ No:  继续Step 4


Step 4: 是否涉及物理部件的清洗（可恢复性维护）？

→ Yes: Recoverable Fouling Removal → Clean-anchor Reset

→ No:  继续Step 5


Step 5: 是局部部件更换，还是大范围翻修？

→ 局部: Partial Restorative → Partial Reset

→ 整体: Major Restorative → Full Reset


## 5. Segment Model（分段模型）

Segment是Baseline Management的核心数据结构。每个Segment代表一段连续的、基线稳定的设备运行期间。


## 5.1 Segment定义

Segment起点：设备初次投入使用，或触发new-segment的维护事件完成后

Segment终点：下一次触发new-segment的维护事件发生时

Segment内部：HI和Trend独立计算，不跨越Segment边界

Segment元数据：记录触发事件类型、维护内容、恢复程度（如可知）


## 5.2 跨Segment的资产级历史

Segment之间不强行拼接绝对HI值，但保留以下资产级信息：


| 信息项 | 含义 | 用途 |
| --- | --- | --- |
| Segment序号 | 第N个运行周期 | 追踪设备生命周期位置 |
| 维护事件类型 | 按Event Taxonomy分类 | 解释Segment边界的物理原因 |
| 维护前HI状态 | Segment结束时的HI值（退化程度记录） | 评估维护前设备状态 |
| 维护后HI基线 | 新Segment开始时的baseline水平 | 判断维护是否充分恢复 |
| Segment退化斜率 | 本Segment内HI的平均变化速率 | 跨Segment比较退化速度 |
| Virtual Age（概念） | 等效累计运行损耗，跨Segment的连续性指标 | 待数据支撑后定义，v0.1仅保留概念 |
| Restoration Factor（概念） | 维护后的性能恢复程度（0=无恢复，1=完全恢复） | 待数据支撑后定义，v0.1仅保留概念 |


注：Virtual Age和Restoration Factor在v0.1中仅作为概念占位，不定义具体公式。数学定义需等到真实Marine数据到手后基于实际退化模式设计。


## 5.3 Segment可视化示意


健康状态

|

|  Seg 1          Seg 2            Seg 3

|  (新机)         (换喷油嘴后)      (清洗增压器后)

## 1.0|━━━━┓            ━━━━┓             ━━━━┓

|    ┃退化          ┃退化              ┃退化

|    ┃↓            ┃↓                ┃↓

## 0.x|    ┗━→维护       ┗━→维护            ┗━→(当前)

|─────────────────────────────────────────▶ 时间

↑             ↑                 ↑

Seg1起点   Partial Reset      Fouling Reset


每个Segment内独立计算HI和Trend，Segment元数据记录维护事件和恢复程度。跨Segment的退化斜率对比是长期健康评估的核心。


## 6. Marine Mapping（发电机专项，v0.1范围）

v0.1范围：柴油发电机（Diesel Generator）。主机/冷却系统/空压机等系统留待后续版本覆盖。


| 维护事件 | Event类型 | 受影响参数 | Reset动作 | 验证方法 |
| --- | --- | --- | --- | --- |
| 发电机大修
（整体翻修） | Major Restorative | 全部残差 | Full Reset
开启新Segment | 维护后各参数残差应快速收敛至新baseline附近 |
| 更换喷油嘴
（单缸或多缸） | Partial Restorative | 该缸排温残差
总功率残差（轻微） | Partial Reset
仅重置受影响缸的排温相关residual | 维护后该缸排温残差应阶跃下降并稳定 |
| 清洗涡轮增压器 | Recoverable Fouling | 扫气压力残差
排温（轻微）
比油耗（如有） | Clean-anchor Reset
以清洗后稳定状态为新锚点 | 清洗后扫气压力残差应阶跃恢复，与清洗前对比量化可恢复损失 |
| 清洗中冷器/空冷器 | Recoverable Fouling | 进气温度残差
排温（间接） | Clean-anchor Reset | 清洗后进气温度残差阶跃恢复 |
| 换油/滤芯 | Partial Restorative
（轻微） | 滑油压力残差
滑油温度残差 | Partial Reset（可选）
影响较小，视数据决定 | 滑油参数残差轻微变化，通常无需独立Segment |
| 排温传感器更换/校准 | Measurement-chain | 该传感器的排温读数 | Sensor Reset
先验证一致性 | 维护前后同工况下排温读数对比，确认校准前后的偏移量 |
| 调速器参数调整 | Control/Config | 控制器相关残差 | Model Version Update | 新版本模型重新归一化后趋势应恢复正常 |


注：上述对应关系基于发电机物理机制推断，尚未在真实Marine数据上验证。具体参数响应需Validation D确认。


## 7. Data Requirements

实现Baseline Management所需的数据，分为运行数据和维护记录两部分。


## 7.1 运行数据需求

与Marine Data Requirement Sheet v0.3保持一致，Priority A字段为必须：

时间戳（精确到分钟或更细）

主负荷指标（功率/负荷%/电流，反映工况）

各缸排温

冷却水出口温度

滑油压力

滑油温度


Baseline Management的额外需求：

数据时间跨度必须覆盖至少1次维护事件（否则无法验证Segment切换）

维护事件前后的数据必须连续，不能有大段缺失


## 7.2 维护记录需求

维护记录是Baseline Management的核心依赖，优先级等同于传感器数据。


| 字段 | Priority | 说明 |
| --- | --- | --- |
| 维护日期 | A（必须） | 精确到天，用于定位Segment边界 |
| 维护内容描述 | A（必须） | 足以判断Event Taxonomy分类 |
| 受影响部件/缸号 | A（必须） | 确定Partial Reset的范围 |
| 累计运行小时（如有） | B（推荐） | 支持Virtual Age计算 |
| 维护后测试结果（如有） | B（推荐） | 量化Restoration Factor |
| 执行人/班次 | C（加分项） | 辅助数据质量判断 |


## 7.5 Maintenance Event Log Template

以下是向教学船或实船请求维护记录时建议使用的最低模板格式。提前定义格式，避免数据到手后发现维护记录不可用。


| 字段 | 格式 | 例子 | 必须/推荐 |
| --- | --- | --- | --- |
| Date | YYYY-MM-DD | 2027-03-15 | 必须 |
| Asset | 设备名/编号 | DG1 / Generator #1 | 必须 |
| Event Description | 自由文本 | Replaced fuel injector, cylinder #3 | 必须 |
| Event Type
（可选，参考4.1） | Major/Partial/Fouling/Sensor/Config/Context | Partial Restorative | 推荐 |
| Affected Components | 部件名+编号 | Injector #3 | 必须 |
| Running Hours at Event | 数字（小时） | 4823 h | 推荐 |
| Post-maintenance Test | 测试结果描述 | Exhaust temp normal after 2h run-in | 推荐 |
| Technician/Watch | 姓名或班次 | 2nd Engineer / Day Watch | 可选 |
| Notes | 任何补充说明 | Old injector showed heavy carbon deposit | 可选 |


最低可接受的维护记录：Date + Asset + Event Description + Affected Components。这四个字段足以支持Event Taxonomy分类和Segment边界定位。


建议在与教学船同学联络时，将此模板作为'数据需求清单附件'一并提供，明确说明维护记录和传感器数据同等重要。


## 8. Validation D Success Criteria

Validation D的目标是在真实Marine数据上验证Baseline Management逻辑的有效性，即Q4b的第一批Marine域证据。


## 8.1 理想情况（Ideal Scenario）

数据条件：

Priority A字段完整，采样间隔≤1小时，时间跨度≥6个月

至少1次有明确维护记录的维护事件（日期+内容+受影响部件）

维护前后各有≥2周的连续运行数据


验证通过标准：


| 验证项 | 成功标准 | 物理意义 |
| --- | --- | --- |
| 维护前退化趋势 | 维护前Residual和HI呈上升趋势（Spearman rho > 0.5） | 退化信号在维护前可观测 |
| 维护后Residual恢复 | 维护后Residual阶跃下降，幅度与Event类型匹配 | 维护效果在残差中可见 |
| Segment切换成功 | 新Segment的baseline与旧Segment显著不同（t-test p < 0.05） | Baseline Management正确识别边界 |
| 新Segment趋势重启 | 新Segment内Trend从新baseline重新建立，方向物理合理 | 维护后监控可以正常继续 |
| 历史记录保留 | 维护前的退化历史可查询，不被新Segment覆盖 | 资产级历史完整性 |


## 8.2 最低可接受情况（Minimum Acceptable Scenario）

数据条件：

Priority A字段基本完整（缺失率<20%）

只知道维护大概发生的月份，不知道具体日期和内容

维护前后各有≥1周的连续运行数据


验证通过标准（降级版）：


| 验证项 | 最低标准 | 备注 |
| --- | --- | --- |
| 维护时间点识别 | 能通过Residual分布变化点检测定位大致维护时间（±2周） | 利用统计变化点检测替代精确维护记录 |
| Segment切换 | 维护前后Residual分布有显著差异（KS test p < 0.05） | 证明系统能区分两种状态 |
| 趋势方向合理 | 新Segment内趋势方向与物理预期一致（退化应为上升趋势） | 不要求完整的趋势统计显著性 |


最低可接受情况不能关闭Q4b，只能提供初步证据。完整Q4b验证必须有精确的维护记录。


## 9. Known Limitations and Open Questions

## 9.1 已知局限

N-CMAPSS等公开数据集不含真实维护事件，只能用于验证分段逻辑（Surrogate），不能关闭Q4b

本文档所有Marine发电机的维护事件映射基于物理机制推断，未经真实数据验证

Virtual Age和Restoration Factor的具体定义需等数据到手后确定，v0.1仅保留概念

多机并联场景（多台DG同时运行）的Baseline Management逻辑未覆盖

传感器校准导致的阶跃台阶（Gemini提示的工程风险）需要在数据预处理中单独识别


## 9.2 开放问题

| 问题 | 当前状态 | 解决路径 |
| --- | --- | --- |
| Segment边界如何精确定位（当维护记录不精确时） | 未解决 | 统计变化点检测（CUSUM/PELT）+ 维护记录粗粒度对齐 |
| Partial Reset的范围如何定义（哪些残差受影响） | 概念级 | 需要领域专家确认+数据验证 |
| Restoration Factor如何量化 | 概念占位 | 待真实维护前后数据对比后定义 |
| 跨Segment的退化速率对比是否有统计意义 | 未验证 | 需要多个完整Segment的数据 |
| 多机并联时的负荷切换如何与退化信号分离 | 未设计 | 需要机组状态记录（推断字段） |


## 10. Version History

| 版本 | 日期 | 内容 |
| --- | --- | --- |
| v0.1 | 2026-06-06 | 初版。基于跨行业Deep Research调研设计。覆盖六类事件分类、Segment模型、发电机专项映射、维护记录模板、双标准验证准则。v0.1仅设计，未实现。 |



Baseline Management Design v0.1 | 2026.06.06 | Design Only — Awaiting Marine Data for Implementation

---

# Baseline Management v0.2 Additions
Date: 2026-06-06

---

## Section 11: Event Detection Heuristics

### Important Principle: Probabilistic Classification

Event classification is probabilistic, not deterministic.
All automatically detected events shall be assigned
a confidence level:

| Confidence | Condition |
|------------|-----------|
| A | Maintenance record AND data pattern agree |
| B | Strong data pattern, maintenance record absent |
| C | Weak pattern or insufficient evidence |

Segment actions should preserve and carry forward
the confidence level of the triggering event.
Evidence from Confidence C segments should not be
used in primary validation conclusions.

---

### 11.1 Major Restorative (Full Reset trigger)

Observable pattern:
- Simultaneous step change in MULTIPLE residuals
  (≥3 state variables shift at same time)
- Step magnitude: > 3× baseline residual std
- All affected residuals shift downward
  (performance improvement direction)
- New stable level maintained for ≥ 1 week

Distinguishing from sensor artifact:
- Sensor artifact affects ONE channel only
- Major restoration affects multiple physically
  coupled channels simultaneously

Marine DG example:
After overhaul: exhaust temp residual drops,
lube oil pressure residual normalizes,
cooling water temp residual drops
→ ALL simultaneously → Full Reset triggered

---

### 11.2 Partial Restorative (Partial Reset trigger)

Observable pattern:
- Step change in SPECIFIC residuals only
  (1-2 state variables physically coupled to
   the replaced component)
- Other residuals remain stable
- Step magnitude: > 2× baseline residual std
  for affected channels only

Marine DG example:
After injector replacement on cylinder #3:
exhaust temp of CYL3 drops sharply,
other cylinders unchanged,
total power residual shows minor improvement
→ Partial Reset on CYL3 exhaust only

---

### 11.3 Recoverable Fouling Removal (Clean-anchor Reset)

Observable pattern:
- Gradual degradation trend reverses abruptly
- Residual returns toward (but NOT to) original
  commissioning baseline
- Improvement is partial, not complete

IMPORTANT: Performance improves but does NOT return
to original commissioning baseline.
This is the key characteristic distinguishing
Fouling Removal from Major Restorative events.
If residual fully returns to commissioning level
→ reclassify as Major Restorative.

Marine DG example:
After turbocharger cleaning:
scavenge pressure residual improves,
exhaust temp may show slight improvement,
but scavenge pressure does not reach original level
→ Clean-anchor Reset

---

### 11.4 Measurement-chain Intervention (Sensor Reset only)

Observable pattern:
- Step change in ONE sensor reading only
- Physically uncoupled sensors show NO change
- Step may be positive or negative
- Step does not follow physical degradation logic

Key check: Does the step make physical sense
given current operating conditions?
If NOT → likely sensor artifact, not health event

---

### 11.5 Control/Config Change (Model Version Update)

Observable pattern:
- Setpoint variables show step change
- Expected State model predictions shift
  even when equipment health unchanged
- Residuals shift due to model mismatch,
  not actual health change

Detection: if residual shift correlates with
setpoint shift → config change, not health event

---

### 11.6 Operating-context Shift (No Reset)

Observable pattern:
- Gradual drift in residuals correlated with
  known environmental variables
- Drift is reversible when context returns
- No step change, only gradual movement

---

## Section 12: Decision Tree for Event Classification

Given an observed residual pattern, apply in order:

Step 1: Is there a sudden step change (within 1-3 sampling intervals)?
  → No: Operating-context Shift or normal noise → No Reset
  → Yes: Continue to Step 2

Step 2: How many state variables show the step?
  → 1 variable only: → Step 3A (sensor check)
  → 2-3 variables (physically coupled): Partial Restorative
  → 4+ variables (system-wide): Major Restorative
  → Setpoint variables also changed: Control/Config Change

Step 3A (single variable check):
  Does the step make physical sense?
  → No: Sensor artifact → Sensor Reset only
  → Yes: Partial Restorative

Step 4: Is maintenance record available?
  → Yes: Cross-validate with record → Confidence A
  → No: Use heuristic classification → Confidence B or C

Step 5: Does the new state remain stable
  for at least 1 week (or 7+ data points at 1h sampling)?
  → No: Likely transient disturbance (port maneuver,
         load switching, sea state change) → No Reset
  → Yes: Event confirmed → apply Reset action

Note: Step 5 is critical for marine systems where
short-term operational disturbances are common
and must not trigger Segment resets.

---

## Section 13: Minimum Data Requirements for Event Detection

| Requirement | Minimum | Ideal |
|-------------|---------|-------|
| Sampling interval | ≤ 1 hour | ≤ 15 min |
| Continuous coverage around event | ±1 week | ±2 weeks |
| State variables available | ≥ 3 (incl. exhaust temp) | All Priority A fields |
| Maintenance record | Month-level date | Exact date + component |

If sampling interval is 2h (logbook):
Step detection still possible but may miss transient
effects within the 2h window.
Recommend using ±2 week stability window for confirmation.

---

## Section 14: Marine DG Event Classification Examples

| Scenario | Observable Pattern | Classification | Confidence | Segment Action |
|----------|-------------------|----------------|------------|----------------|
| DG overhaul after 8000h | All residuals step down simultaneously, sustained | Major Restorative | A (with record) | Full Reset |
| Injector replacement CYL3 | Only CYL3 exhaust temp drops, others stable | Partial Restorative | A (with record) | Partial Reset CYL3 |
| Turbocharger cleaning | Scavenge pressure improves, partial recovery | Fouling Removal | B (no record) | Clean-anchor Reset |
| Exhaust temp sensor replaced | CYL2 reading jumps +15°C, no load change | Sensor Artifact | A | Sensor Reset only |
| Harbor → ocean voyage | Residuals drift with ambient, reverse on return | Context Shift | — | No Reset |
| Governor parameter adjusted | Expected State predictions shift, load tracking changes | Config Change | A | Model Version Update |
| Port maneuver (1 day) | Brief residual spike, returns to baseline within 48h | Transient Disturbance | — | No Reset (Step 5 check) |

---

## Section 15: Segment Quality Levels

Segment quality reflects the confidence in the
segment boundary definition and the maintenance
event that triggered it.

| Quality | Definition | Evidence Basis |
|---------|-----------|----------------|
| A | Exact maintenance date + event description + data pattern confirms | Maintenance record AND data pattern agree |
| B | Maintenance month known or event description incomplete + data pattern strong | Data pattern strong, record partial |
| C | No maintenance record, segment boundary inferred from data only | Data pattern only, no record |
| D | Segment boundary uncertain, data quality insufficient | Cannot reliably identify boundary |

### Evidence Use Policy for Validation D

| Quality | Primary Validation | Exploratory Analysis | Discard |
|---------|-------------------|---------------------|---------|
| A | ✔ Include | ✔ Include | — |
| B | ✔ Include | ✔ Include | — |
| C | — | ✔ Include | — |
| D | — | — | ✔ Discard |

Primary validation conclusions (Q4b PASS/FAIL determination)
use only Quality A and B segments.
Quality C results are reported separately as
exploratory evidence and cannot close Q4b.
Quality D data is excluded from all analysis.

### Reporting Requirement

All Validation D results must state:
"This conclusion is based on N segments of Quality A/B.
[X] Quality C segments were analyzed separately.
[Y] Quality D segments were excluded."

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v0.1 | 2026-06-06 | Initial design. Event taxonomy, Segment model, Marine DG mapping, data requirements. |
| v0.2 | 2026-06-06 | Added: Probabilistic classification principle, Event detection heuristics (Sec 11), Decision tree with stability check (Sec 12), Data requirements (Sec 13), Worked examples with confidence levels (Sec 14), Segment Quality Levels (Sec 15). |
