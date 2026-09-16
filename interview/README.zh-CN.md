# AI 工程师面试准备

[English](README.md) · [简体中文](README.zh-CN.md) · [Study guide](../STUDY_GUIDE.zh-CN.md)

面向 Applied AI / AI Product / Full-stack AI Engineer。先用目标公司的 JD 与面试流程调整比例；偏模型训练的 MLE/Research 岗位需要额外的数学、ML 和训练准备。以下题目是本仓库原创练习，不是公司真题或命中率承诺。

## 怎么用

每周使用学习计划内的 1 小时：15 分钟脱稿答题、20 分钟编码或设计、15 分钟对照资料补漏、10 分钟记录失败与下次练习。先中文讲明白，再录一段 3 分钟英文解释。

统一评分（练习用，不是招聘标准）：0 = 不会；1 = 能定义；2 = 能比较方案及失败模式；3 = 能用代码/实验数据证明，并解释局限。核心主题连续两次达到 2，项目题达到 3，作为开始模拟面试的自测门槛。

## 准备哪些面试轮次

| 方向 | 练习 | 交付证据 |
|---|---|---|
| 编程 | 算法基础 + JSON 处理、异步超时、重试、检索评分 | 能运行的代码、边界测试、复杂度解释 |
| AI 基础与工程 | LLM、RAG、Tool Calling、Agent、Evals | 本页每周题目的解释及反例 |
| 系统设计 | 多租户客服 Agent、文档问答、代码修改服务 | 架构图、权限边界、SLO、成本与扩展取舍 |
| 项目与行为 | 一次失败、一次取舍、一次协作分歧 | 个人贡献、真实数据、复盘 |

<a id="resources"></a>
## 资源链接与使用顺序

先跟每周的主题资源学习；进入面试冲刺后，再按薄弱项使用 ML Interviews、System Design Primer 和 LeetCode，不需要一次读完所有资源。

| 资源 | 用法 |
|---|---|
| [How Transformer LLMs Work](https://learn.deeplearning.ai/courses/how-transformer-llms-work/) | Token、Embedding、Attention、生成过程。 |
| [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/) | 模型校验、额外字段、类型转换与严格模式。 |
| [DeepLearning.AI — Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation) | 检索、切块与评测；按主题选学，不要求两小时学完整门课。 |
| [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | Workflow 与 Agent 的取舍、路由、循环和工具设计；学习架构思想，不照搬旧 SDK 示例。 |
| [DeepLearning.AI — Agentic AI](https://learn.deeplearning.ai/courses/agentic-ai) | 选修进阶课：选择工具调用、规划和评测相关内容。 |
| [DeepLearning.AI — Evaluating AI Agents](https://www.deeplearning.ai/short-courses/evaluating-ai-agents/) | Tracing、组件与轨迹评测、改进 Judge。 |
| [OWASP — LLM Top 10](https://genai.owasp.org/llm-top-10/) | 重点看 Prompt Injection、敏感信息泄露和过度代理权限。 |
| [Google — Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/) | 选读 Service Level Objectives、Monitoring Distributed Systems、Handling Overload。 |
| [Chip Huyen — AI Engineering companion repository](https://github.com/chiphuyen/aie-book) | 评测、RAG、Agent 与应用架构参考资料；不是面试题库。 |
| [Chip Huyen — Introduction to Machine Learning Interviews](https://huyenchip.com/ml-interviews-book/) | 岗位识别、ML 基础和评测；内容较早、范围偏 ML，训练类内容按 JD 选学。 |
| [System Design Primer](https://github.com/donnemartin/system-design-primer) | 缓存、队列、存储、扩展与系统设计练习；自己补上 AI 评测和权限约束。 |
| [LeetCode — Top Interview 150](https://leetcode.com/studyplan/top-interview-150/) | 根据摸底选择数组、哈希表、双指针、区间、树和堆；不要求刷完 150 题。 |
| [Python — Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html) | 练习取消、超时和并发任务，使用与你 Python 版本一致的文档。 |
| [Stanford CS329Z — Engineering AI Agents](https://cs329z.stanford.edu/) | 相关公开材料可用时作为选修主线；不要等待课程发布才开始项目。 |

资源核查：2026-09-16。已读取作者/官方页面核对用途。DeepLearning.AI 部分课程详情页对自动访问返回 403 或访问限制，课程名称和主题参考官方课程目录及可读取页面，未验证完整登录后课程内容。课程、练习平台可能要求账号或付费，证书和订阅不是本路线的完成条件；本表不承诺永久免费。AI Engineering 的 GitHub 仓库是配套资料，不是免费书籍全文。

## 每周题目与答题要点

<a id="week-0"></a>
### Week 0

**你在准备哪类 AI 岗位？这个场景为什么需要 AI？**

答题要点: 把五份 JD 映射到编程、AI 系统、ML 深度与产品能力；给出一个确定性替代方案和可测量用户结果。

配套学习: [Week 0](../STUDY_GUIDE.zh-CN.md#week-0) · [Chip Huyen — Introduction to Machine Learning Interviews](https://huyenchip.com/ml-interviews-book/)

<a id="week-1"></a>
### Week 1

**解释逐 Token 生成。更长的上下文能解决所有知识问题吗？**

答题要点: 覆盖 Token、Attention 和解码；区分上下文容量与证据相关性、新鲜度、成本和可靠性。

配套学习: [Week 1](../STUDY_GUIDE.zh-CN.md#week-1) · [How Transformer LLMs Work](https://learn.deeplearning.ai/courses/how-transformer-llms-work/)

<a id="week-2"></a>
### Week 2

**输出通过 Schema 但内容错误，怎么测？什么时候可以安全重试？**

答题要点: 区分格式/类型、语义正确性和授权；处理拒答/截断与有界重试，有副作用的操作需幂等。

配套学习: [Week 2](../STUDY_GUIDE.zh-CN.md#week-2) · [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/)

<a id="week-3"></a>
### Week 3

**RAG 回答错误，如何定位故障环节？**

答题要点: 沿摄取 → 检索 → 上下文 → 生成排查，查看标注证据、Recall@k 和引用；测试缺证据与拒答。

配套学习: [Week 3](../STUDY_GUIDE.zh-CN.md#week-3) · [DeepLearning.AI — Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation)

<a id="week-4"></a>
### Week 4

**何时需要混合检索和重排？如何证明改进有效？**

答题要点: 比较精确词与语义检索的失败；固定数据、保留测试查询，衡量延迟/成本，报告样本量和负结果。

配套学习: [Week 4](../STUDY_GUIDE.zh-CN.md#week-4) · [DeepLearning.AI — Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation)

<a id="week-5"></a>
### Week 5

**创建 Issue 后工具超时，Agent 应直接重试吗？**

答题要点: 超时表示结果不确定，先用操作 ID、去重与状态核对，再决定重试；参数和权限在模型外校验。

配套学习: [Week 5](../STUDY_GUIDE.zh-CN.md#week-5) · [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

<a id="week-6"></a>
### Week 6

**崩溃后应保留什么状态？如何防止重复动作和无限循环？**

答题要点: 持久化操作结果与检查点版本；审批绑定具体参数，限制步数/时间/成本，说明 Memory 不提供授权。

配套学习: [Week 6](../STUDY_GUIDE.zh-CN.md#week-6) · [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

<a id="week-7"></a>
### Week 7

**LLM Judge 认为新版更好，就可以上线吗？**

答题要点: 使用有代表性的保留集、人工校准、确定性检查和错误分组，检查评分偏差、不确定性及回归。

配套学习: [Week 7](../STUDY_GUIDE.zh-CN.md#week-7) · [DeepLearning.AI — Evaluating AI Agents](https://www.deeplearning.ai/short-courses/evaluating-ai-agents/)

<a id="week-8"></a>
### Week 8

**检索文档要求上传客户数据，由什么阻止它？**

答题要点: 文档文本是数据；服务端强制授权、租户隔离、工具/网络限制与限定范围审批，单靠 System Prompt 不够。

配套学习: [Week 8](../STUDY_GUIDE.zh-CN.md#week-8) · [OWASP — LLM Top 10](https://genai.owasp.org/llm-top-10/)

<a id="week-9"></a>
### Week 9

**质量稳定但 p95 翻倍，如何定位并降低延迟？**

答题要点: 拆解排队/检索/模型/工具耗时；检查负载和 Token 增长、缓存正确性、并发限制、降级与质量成本取舍。

配套学习: [Week 9](../STUDY_GUIDE.zh-CN.md#week-9) · [Google — Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/)

<a id="week-10"></a>
### Week 10

**生成补丁通过测试后，还需要检查什么？**

答题要点: 检查改动范围、测试覆盖与测试本身的改动、依赖、密钥和执行隔离；区分生成、审查、合并与部署权限。

配套学习: [Week 10](../STUDY_GUIDE.zh-CN.md#week-10) · [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

<a id="week-11"></a>
### Week 11

**为多个客户设计客服 Agent，最小可行架构是什么？**

答题要点: 明确负载/SLO，画摄取、租户隔离检索、模型网关、工具审批、异步任务和评测，解释一个弃选方案与扩展瓶颈。

配套学习: [Week 11](../STUDY_GUIDE.zh-CN.md#week-11) · [System Design Primer](https://github.com/donnemartin/system-design-primer)

<a id="week-12"></a>
### Week 12

**讲一次项目中最大的失败，以及一个真正可量化的改进。**

答题要点: 按背景 → 自己的决策 → 实现 → 测量结果 → 局限讲述；关联提交/报告，区分个人、AI 生成及团队贡献。

配套学习: [Week 12](../STUDY_GUIDE.zh-CN.md#week-12) · [Chip Huyen — AI Engineering companion repository](https://github.com/chiphuyen/aie-book)

## 编程与系统设计实战

1. **30 分钟编码：**实现有并发上限、单次超时和最多两次重试的批量调用器。先澄清哪些错误可重试；覆盖取消、部分失败和结果顺序，使用 Mock，不需要付费 API。
2. **30 分钟编码：**从查询/文档分数生成 Top-k 并计算 Recall@k 与 MRR；测试无相关文档、重复 ID、空集和相同分数，说明约定。
3. **45 分钟系统设计：**设计多租户客服 Agent。前 5 分钟确认用户、流量和成功指标，10 分钟画数据流，15 分钟深入检索/权限，10 分钟分析失效与成本，最后 5 分钟讲取舍。
4. **15 分钟项目追问：**让同伴追问“基线是什么、为什么选这个方案、谁标注数据、测试集是否泄漏、成本怎么算、你亲自做了什么”。

## 投递前四周冲刺

每周额外 2–3 小时；如果总预算仍是 8 小时，延长学习周期。

| 周 | 重点 | 验收 |
|---|---|
| 1 | 用 5 份 JD 做能力差距表；复习 LLM/RAG；做 2 道编码诊断题 | 确定最薄弱的两个主题 |
| 2 | 完成一个系统设计模拟；复习 Agent/Evals/Safety；做一次限时编码 | 留下评分和改进项 |
| 3 | 一次 60 分钟模拟（20 编码 + 25 设计 + 15 项目）；修复暴露的问题 | 提供修复后的答案/代码 |
| 4 | 再做一次同规格模拟；录英文 Demo；核对简历指标 | 每个项目数字都可追溯 |

简历写法：在 **[场景与样本量]** 上，通过 **[具体改动]**，把 **[指标]** 从 **[基线]** 改进为 **[结果]**，代价为 **[成本/延迟变化]**。只填写自己测过的数据。
