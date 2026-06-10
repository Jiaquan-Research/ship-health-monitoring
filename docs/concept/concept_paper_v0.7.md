船舶系统健康监控

Ship System Health Monitoring

Concept Paper  v0.7

2026.06.05  |  内部讨论稿

# 1. 为什么现在值得做

工业设备健康管理的思路，在过去二十年里发生了一次根本性转变：

| 过去的模式 | 目标模式 |
| --- | --- |
| 设备正常运行 | 持续监测退化趋势 |
| 报警触发 | 趋势预警（早于报警） |
| 故障发生 | 状态主动干预 |
| 紧急处理 | 计划性维护 |
| 非计划停机 | 避免故障，减少停机 |

这条路线，高可靠性工业领域已经走了很长时间：

| 领域 | 代表实践 | 核心方法 |
| --- | --- | --- |
| 核工业 | IAEA在线监测，系统健康指数程序 | 层级健康指数聚合，FP严格控制 |
| 航空工业 | NASA/GE发动机EHM，EGT margin监控 | 工况归一化残差，margin decay趋势 |
| 油气工程 | API 670旋转机械监控，平台PHM | 多传感器融合，无监督异常检测 |
| 建筑HVAC | Deng et al. 2026，冷水机组HI构建 | VIB残差+跨维护周期健康指标 |

船舶工程是这条路线目前覆盖最薄弱的领域之一。设备商有数据管道和报警系统，但标准化的系统健康度层级监控方案在公开文献中尚未出现。

这不是在做聊天机器人，也不是在做故障分类器。

这是在做PHM（Prognostics and Health Management）的Marine路线——把已在其他高可靠性工业领域验证过的健康监控逻辑，系统性地迁移到船舶工程。

# 2. 项目是什么

我们正在构建一套船舶系统健康度层级监控系统（Ship System Health Hierarchy Monitoring）。

核心目标是：在传统报警系统发出故障报警之前，通过持续监测系统参数的退化趋势，提前识别设备健康状态的下降，并输出可供轮机员参考的维护建议。

Health = 距离允许边界还有多远，以及这个距离在缩小的速度——而不是"是否已经超过报警阈值"。

不在做的事情：

* 不是故障诊断系统（发生了什么故障）

* 不是实时控制系统

* 不依赖大量故障标注数据

* 不需要RUL（剩余使用寿命）作为第一交付物

* 不是替代轮机员决策——系统输出健康状态与维护建议，最终决策由轮机员做出

# 3. 核心科学问题

本项目围绕以下五个科学问题展开，构成完整的研究链条：

| 问题 | 内容 | 当前状态 |
| --- | --- | --- |
| Q1 | Condition Variables是否足以支持工况归一化和Expected State建模？ | Strong Evidence<br><br>Validation B1: R²=0.970~0.993（LBNL Chiller Plant）<br>Validation B3A: 1h采样R²=0.975，2h采样R²=0.939，采样频率鲁棒性确认 |
| Q2 | Residual是否携带物理退化信息？ | Strong Evidence<br><br>Validation B2.1: 四个目标严格单调响应故障严重度<br>Spearman rho=1.0 |
| Q3 | Health Indicator是否能够从Residual构造？ | Initial Evidence<br><br>HI_v0验证：Rolling RMS，四个目标HI_mean严格单调。CT_SW_TEMP_1最优（W=6h）。<br><br>注：单故障类型，单数据集，最优HI形式仍为开放问题（Q3a）。 |
| Q4a | Residual是否天然形成可用于健康监控的趋势？ | Initial Evidence<br><br>Validation B4：4/4目标严格单调，Spearman rho=1.0（20/20），Strong PASS。<br>RMS为最佳趋势指标，CT_SW_TEMP_1的Cohen's d=1.84。 |
| Q4b | 维护事件后如何管理基线？（Baseline Management） | Q4b最终验证依赖真实Marine维护记录。<br>公开数据集（N-CMAPSS / CMAPSS / PRONOSTIA / XJTU-SY）<br>均不包含真实维护事件，只能作为Surrogate Validation，<br>用于验证分段逻辑和趋势延续机制，不能关闭Q4b。<br>这是经数据集审计确认的高置信度负面结论（2026-06-06）。 |
| Q5 | 健康度输出能否支持维护指导？ | Open — 依赖Q4b完成<br>Marine-LLM定位为MD（Maintenance Decision）Layer工程入口。<br>分工如下：<br>Health Monitoring负责：Residual / HI / Trend计算<br>Marine-LLM负责：Trend解释 / 维护建议生成 / 知识库检索 / 工程交互 |

注：Q1/Q2的验证证据来自HVAC域（LBNL Chiller Plant），向Marine系统迁移尚未验证。Domain Transfer Risk明确存在。

# 4. 为什么有价值

## 学术视角

* 性能退化型故障监控：经行业与高校从业者讨论，具有进一步研究价值

* 系统健康度层级（Health Hierarchy）：基于当前调研结果，公开文献中尚未发现成熟且透明的跨OEM标准方案，研究空间确认

* PHM领域共识：HCM层（健康状态监测）成熟，MD层（维护决策）最不成熟——我们的工作跨越了两端

## 现场工程视角

* 船上现有系统：Kongsberg等设备商提供报警+趋势监控，但无标准化层级健康指数

* 轮机员实际需求：健康状态是在变好还是变坏？距离运行边界还有多远？是否需要提前安排维护？

* 空白市场：制冷/空调、空压机、液压泵等辅机系统船上基本无健康监控

## 行业Gap

| 层级 | 行业现状 | 我们的位置 |
| --- | --- | --- |
| HCM 健康状态监测 | 设备商已有，但多为单设备、单参数 | 层级聚合，多系统覆盖 |
| FD 故障诊断 | 规则库成熟，深度诊断弱 | Marine-LLM已有原型 |
| HP 健康预测 | 选择性存在，无统一框架 | 核心研究目标 |
| MD 维护决策 | 最不成熟，基本靠人工经验 | Marine-LLM提供辅助入口 |

# 5. 技术路线概要

整体技术链路如下：

传感器数据（K-Chief / 记录簿）

↓

工况归一化（Condition Normalization）

↓  ← 核心技术挑战：消除负荷/环境变化的干扰

预测模型（Expected State Model）

↓  给定当前工况，预测"正常应该是什么值"

残差（Residual）

├─ 主线：Health Monitoring Route

│       ↓ Health Indicator → Trend → Maintenance Guidance

│

└─ 探索线：Structure Monitoring Route（来自TEP，尚未整合进主线）

↓ Statistical Structure Change（探索性研究）

| 路线 | 做什么 | 当前状态 |
| --- | --- | --- |
| 预测模型路线 | 建立工况→期望状态的映射，输出残差作为退化信号 | B1 PASS：R²=0.970（CHL_POW_1） |
| 结构监测路线 | 分析残差在状态空间中的统计结构变化 | TEP初步验证（EL-3冻结） |

# 6. 当前进展

| 模块 | 当前状态 | 主要成果 |
| --- | --- | --- |
| TEP研究线（Validation A） | 完成 | 化工仿真数据集上观察到：性能退化型故障在表示空间中呈现稳定统计结构现象（F13/F14 archetype，500-run验证通过）。<br>注：该现象仅在TEP仿真环境观察到，不构成Marine系统存在同类结构的证据。<br>TEP→Marine的迁移是Domain Transfer Risk的核心，尚未验证。 |
| Marine-LLM | 原型完成，架构冻结 | L1规则路由引擎，96.7%准确率，FP=0%，已覆盖冷却/燃油/空气/燃烧四个域，基于K-Chief相关手册和操作流程完成验证 |
| Health Monitoring — Validation B1 | 完成 | LBNL Chiller Plant：6个工况变量预测4个状态变量，R²=0.970~0.993，Expected State路线成立 |
| Health Monitoring — Validation B2.1 | 完成 | 残差严格单调响应冷却塔污垢严重度，四个目标全部通过，CT_SW_TEMP_1灵敏度最高（Sensitivity Score=4.60） |
| Health Monitoring — HI_v0 | 完成（Moderate PASS） | Rolling RMS of normalized residual。四个目标HI_mean严格单调。CT_SW_TEMP_1最优（W=6h，Sensitivity=5.99）。Rolling RMS非普适增强器，Q3a（最优HI形式）仍为开放问题。 |
| Health Monitoring — Validation B4 | 完成（Strong PASS） | 残差趋势审计：4/4目标严格单调，Spearman rho=1.0（20/20），RMS为最佳趋势指标，CT_SW_TEMP_1的Cohen's d=1.84。Q4a获得Initial Evidence。 |

# 7. 验证链条状态（2026-06-04）

以下验证结果为当前项目的实证基础：

| 验证阶段 | 问题 | 结果 | 数据来源 | 范围限制 |
| --- | --- | --- | --- | --- |
| Validation A<br>TEP结构发现 | 退化故障是否存在稳定统计结构？ | PASS | TEP仿真数据集 | 仅在化工仿真环境验证 |
| Validation B1<br>Expected State Model | Condition Variables是否足以预测State Variables？ | PASS<br>R²=0.970~0.993 | LBNL Chiller Plant | HVAC域，Marine迁移待验证 |
| Validation B2<br>残差严重度分析 | Residual是否随故障严重度增加？ | 初始FAIL<br>→标签语义审计<br>→修正后PASS | LBNL Chiller Plant | 标签语义（065=最严重，095=最轻）需注意 |
| Validation B2.1<br>修正后复验 | 修正排序后残差是否单调响应？ | STRONG PASS<br>4/4目标严格单调 | LBNL Chiller Plant | HVAC域，冷却塔污垢故障类型 |
| HI_v0<br>Health Indicator构造 | Residual能否构造Health Indicator？ | Moderate PASS<br>HI_mean 4/4严格单调 | LBNL Chiller Plant | Rolling RMS非普适；最优HI形式未知（Q3a） |
| Validation B3A<br>时间分辨率审计 | 路线对采样频率敏感吗？ | 1h PASS<br>2h主要目标可用<br>关键：灵敏度随频率降低反升 | LBNL Chiller Plant（重采样） | HVAC域结论，Marine域需独立验证 |
| Validation B4<br>残差趋势审计 | Residual是否天然形成趋势？ | Strong PASS<br>4/4目标严格单调<br>Spearman rho=1.0（20/20）<br>Cohen's d=1.84（CT_SW_TEMP_1） | LBNL Chiller Plant（B2.1冻结残差） | HVAC域Pseudo Degradation Path，非真实时序退化 |

当前已验证链路：Condition Variables → Expected State → Residual → Physical Degradation → Health Indicator → Trend（Q4a）。状态：HVAC域Q1-Q4a均有证据，Marine域尚未验证。当前瓶颈：Q4b Baseline Management，需含维护事件的数据集。

灵敏度排名（Validation B2.1，冷却塔污垢场景）：

| 排名 | 目标变量 | Sensitivity Score | 物理解释 |
| --- | --- | --- | --- |
| 1 | CT_SW_TEMP_1 | 4.60 | 冷却塔出水温度——热传递退化的直接信号 |
| 2 | CHL_RWCD_TEMP_1 | 3.09 | 冷凝器回水温度——换热效率退化信号 |
| 3 | CHL_SW_TEMP_1 | 0.26 | 冷冻水出水温度——受控变量，响应较弱 |
| 4 | CHL_POW_1 | 0.13 | 压缩机功率——受工况调节影响较大 |

注：此灵敏度排名适用于HVAC域冷却塔污垢场景，不可直接推断Marine系统中各变量的相对灵敏度。

# 8. 下一步与数据需求

## 验证路线

| 验证阶段 | 目标 | 前提条件 | 当前状态 |
| --- | --- | --- | --- |
| Validation A<br>TEP结构发现 | 验证退化故障的统计结构 | TEP数据集 | ✔ 完成 |
| Validation B1<br>Expected State | 验证工况归一化+HI构造方法 | LBNL公开数据集 | ✔ 完成 |
| Validation B2.1<br>Residual vs Degradation | 验证残差携带退化信息 | LBNL公开数据集 | ✔ 完成 |
| Validation B3A<br>时间分辨率审计 | 验证路线对采样频率的敏感性 | LBNL数据重采样 | ✔ 完成<br>1h PASS，2h主要目标可用 |
| Validation C<br>Marine冷却系统 | 验证海事系统迁移能力 | 教学船或公开Marine数据 | 待数据 |
| Validation D<br>Marine发电机 | 真实船舶数据全链路验证 | 教学船发电机数据 | 取决于数据获取进展 |

## K-Chief历史数据确认清单（Phase 0，需现场核实）

| 问题 | 重要性 | 两种结果的影响 |
| --- | --- | --- |
| 历史时序数据是否持久化存储？ | Critical | 否：只能用记录簿<br>是：进入下一步确认 |
| 存储时间跨度多长？ | Critical | < 3个月：数据不足<br>> 6个月含维护事件：理想 |
| 采样间隔是多少？ | Critical | 2h记录簿：只能做长周期趋势<br>分钟级：可做Expected State Model |
| 能否导出？导出格式？ | High | 无法导出：需另想办法<br>CSV/Excel：直接可用 |
| 覆盖哪些参数点？ | High | 至少需要：功率/排温（各缸）/冷却水温/滑油压力/转速 |
| 维护记录在哪里？能否对应时间戳？ | High | 维护记录是Baseline Reset的关键 |
| 有无累计电度表读数？ | Medium | 有：可计算比油耗趋势 |
| 数据是否存在传感器校准导致的突变台阶？ | Medium | 有：预处理时需单独标注，不可误判为退化信号 |

关键判断（基于Validation B3A更新）：
1h采样已获得实证支持（B3A Strong PASS）。
2h采样对主要目标仍保留退化信号，但部分指标出现单调性失败，
属于Borderline结果，需Marine域独立验证后方可推广。

# 9. 合作边界

| 事项 | 负责方 | 说明 |
| --- | --- | --- |
| 数据获取 | 你 | 教学船K-Chief数据确认与获取，维护记录收集 |
| 领域知识验证 | 你 | 船舶参数物理意义、报警标准、现场工程判断 |
| 学术渠道 | 你 | 文献获取、潜在合作院校联络 |
| 代码实现 | 我 | 全部算法开发、数据处理、模型构建 |
| 技术路线设计 | 共同 | 你提供领域约束，我提供技术方案，联合决策 |
| 成果发表 | 共同 | 署名与贡献边界需在项目成熟前明确，建议提前约定 |

# 10. 风险登记

| 风险ID | 风险描述 | 影响 | 优先级 | 当前状态 |
| --- | --- | --- | --- | --- |
| R-01 | Domain Transfer Risk：TEP/HVAC结构是否能迁移至真实Marine系统 | 方法论核心不确定性 | Critical | 未验证，Validation D核心挑战 |
| R-02 | Operating Condition Normalization Risk：工况变化掩盖退化信号 | HI失效→Trend失效→全链路崩塌 | Critical | HVAC域已验证，Marine待验证 |
| R-03 | Sensor Availability Risk：可获取数据与研究需求不匹配 | 参数缺失/采样不足/维护记录缺失 | High | 待教学船Phase 0确认 |
| R-04 | 发电机功率记录为瞬时值 | 比油耗趋势计算困难 | Medium | 待确认是否有累计电度表 |
| R-05 | 设备商数据接口不开放 | 真实数据只能靠人脉渠道 | Medium | 待二次核实 |
| R-06 | 合作分工边界模糊 | 后续发表署名可能产生摩擦 | Medium | 需在项目成熟前明确 |
| R-07 | Marine-LLM定位问题 | 现有路线学术/商务价值均受限 | Low | 需与健康监控线整合规划 |
| R-08 | HVAC→Marine Transfer Risk：HVAC验证结论不可直接推断Marine场景 | 灵敏度排名、变量选择需重新验证 | High | 已标注，Validation C/D前不做推断 |
| R-09 | Baseline Management Risk：维护事件导致基线阶跃，长期趋势分析失效 | Residual baseline reset逻辑待设计 | High | 开放研究问题，HI_v0设计前需解决 |

# 11. 研究现状总结（2026-06-05，更新于2026-06-06）

## 当前证据地图

| 科学问题 | 状态 | 主要证据来源 |
| --- | --- | --- |
| Q1<br>Condition → Expected State | Strong Evidence | Validation B1（R²=0.970~0.993）<br>Validation B3A（采样频率鲁棒性） |
| Q2<br>Residual → Degradation | Strong Evidence | Validation B2.1（4/4严格单调，Spearman rho=1.0） |
| Q3<br>Residual → Health Indicator | Initial Evidence | HI_v0（Rolling RMS，4/4目标严格单调） |
| Q4a<br>Residual → Trend存在 | Initial Evidence | Validation B4（4/4目标，Spearman rho=1.0全20组，Cohen's d=1.84） |
| Q4b<br>Baseline Management | Open — Architecture Defined | 跨行业调研完成（2026-06-06）。<br>Multi-segment baseline + event-triggered re-baselining<br>确定为主路线（参考航空ETM、燃气轮机wash-cycle、旋转机械post-overhaul）。<br>缺失项：Marine真实维护记录验证。<br>公开数据集审计结论：N-CMAPSS等均无真实维护事件（高置信度负面结论）。 |
| Q5<br>Maintenance Guidance | Open | 依赖Q4b完成。<br>Marine-LLM定位为MD（Maintenance Decision）Layer工程入口。<br>分工如下：<br>Health Monitoring负责：Residual / HI / Trend计算<br>Marine-LLM负责：Trend解释 / 维护建议生成 / 知识库检索 / 工程交互 |

## 当前瓶颈

HVAC公开数据集验证已基本完成。

项目已验证：

Condition Variables

↓ Q1 Strong Evidence

Expected State Model

↓ Q2 Strong Evidence

Residual → Physical Degradation

↓ Q3 Initial Evidence

Health Indicator

↓ Q4a Initial Evidence

Trend Exists

↓ Q4b OPEN ← 当前瓶颈

Baseline Management

当前科学瓶颈：Q4b是当前主要研究风险。

Deep Research调研结论（2026-06-06）：

* 成熟PHM不是'一条baseline用到底'，而是：asset-specific baseline + event-triggered re-baselining + lifecycle history preservation

* 维护事件需按范围分类处理，不能统一归零

* 所有已知公开数据集（N-CMAPSS/CMAPSS/PRONOSTIA/XJTU-SY/IMS）均无真实维护事件——这是高置信度的负面结论

* N-CMAPSS可作为Surrogate验证分段逻辑，但不能关闭Q4b

* Q4b最终必须靠教学船真实维护记录

Q4b能否解决，将决定项目能否从Health Monitoring走向完整PHM。

推荐架构（来自跨行业调研）：

| 维护事件类型 | 典型Marine例子 | Baseline处理 | HI/Trend影响 |
| --- | --- | --- | --- |
| Major restorative | 大修、发动机翻修 | Full Reset：开新segment | 新segment独立计算HI，保留历史元数据 |
| Partial restorative | 换喷油嘴、换轴承 | Partial Reset：仅影响相关残差 | 不重置无关HI，保留未受影响趋势 |
| Recoverable fouling removal | 清洗涡轮增压器、换热器 | Cycle-local Reset：以清洗后状态为锚点 | 短期可恢复损失+长期不可逆退化双线并行 |
| Measurement-chain | 传感器校准/更换 | Sensor Reset：仅重置测量基线 | 先验证传感器一致性，再更新HI |
| Control/config change | 控制器参数调整 | Model Version Update | 新版本标签，重新归一化后继续趋势 |
| Operating-context shift | 季节变化、负荷模式变化 | No Reset（工况归一化处理） | Segment内继续，不触发重置 |

## 下一研究阶段

| 优先级 | 任务 | 目标 | 状态 |
| --- | --- | --- | --- |
| P1 | Baseline Management设计文档 | 设计event-aware multi-segment架构，覆盖六类维护事件的处理逻辑 | 进行中（docs/design/baseline_management_v0.1.md） |
| P2 | N-CMAPSS Surrogate验证 | 验证分段逻辑和趋势延续机制（Surrogate，不能关闭Q4b） | 数据下载中 |
| P3 | 教学船数据获取（Phase 0） | Marine域真实维护记录，Q4b真正的验证数据源 | 等待同学现场确认 |
| P4 | Validation D | Marine域全链路验证（教学船发电机） | 取决于P3进展 |

注：HVAC域公开数据集验证阶段已完成。Q4b的真正关闭依赖Marine域真实维护记录，公开数据集只能提供方法论脚手架。

本文档为内部讨论稿 v0.7 | 2026.06.05 | 下一步：Q4b Baseline Management数据集调研
