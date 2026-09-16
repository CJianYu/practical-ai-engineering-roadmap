# 按周学习指南

[English](STUDY_GUIDE.md) · [简体中文](STUDY_GUIDE.zh-CN.md) · [Interview](interview/README.zh-CN.md)

这是一条给已有开发经验者的默认路径。按顺序完成：**指定资料 → 最小实现 → 验收 → 面试讲解**。每周只用一份主资料，选修不阻塞进度。

## 时间与范围

12 周是阶段编号，不是就业承诺。原路线含 Week 0 共约 104 小时；完整课程、排障和面试练习可能超过这个预算。每周 8 小时时，建议按 16–20 个日历周安排：Week 0–2 用 4 周，Week 3–4 用 3 周，Week 5–6 用 3 周，Week 7–9 用 4 周，Week 10–12 用 4 周，共 18 周。可按已有经验压缩或延长。

每个 8 小时学习单元：2 小时看资料、4 小时开发与评测、1 小时面试练习、1 小时复盘。这里的阅读范围是选读任务，不是声称能在两小时内学完整门课程。专注投递时另留每周 2–3 小时，或延长周期。

**仓库现状：**已提供五个离线 Lab：结构化校验、词法检索、工具审批、状态恢复与固定样例评测。生产集成仍需你在自己的 Capstone 中完成，Capstone 目录是规格说明，不是完整产品。模型 API 可能收费；先运行离线 Lab，再为真实调用设置自己的预算。

## 今天先做什么

1. 使用 Python 3.11+（推荐 3.12），按 [README](README.zh-CN.md) 安装并运行 `make validate`。
2. 复制 [项目提案](templates/project-proposal.md) 和 [周进度表](templates/progress-tracker.md) 到自己的项目。
3. 做 Week 0；完成验收后按下面编号继续。卡住时缩小数据集/功能，不要跳过验收。

<a id="week-0"></a>
## Week 0 — 定位与准备

1. **学:** [Chip Huyen — Introduction to Machine Learning Interviews](https://huyenchip.com/ml-interviews-book/) — 识别目标岗位，阅读仓库项目提案模板。
2. **做:** 收集 5 个目标岗位 JD；确定一个客服场景，写 20 条评测样例。
3. **验收:** 说清用户、输入、预期答案和禁止动作；不放私人数据。
4. **面试:** [Week 0](interview/README.zh-CN.md#week-0) — 先脱稿回答，再对照要点，关联自己的代码或评测。

<a id="week-1"></a>
## Week 1 — LLM 基础

1. **学:** [How Transformer LLMs Work](https://learn.deeplearning.ai/courses/how-transformer-llms-work/) — 依次学 Token → Embedding → Attention → 解码；能讲清生成过程即可。
2. **做:** 用 10 条样例比较两种 Prompt/上下文方案，记录模型、配置、用量和延迟。
3. **验收:** 解释上下文限制及一个失败案例，不把模型自报置信度当作校准概率。
4. **面试:** [Week 1](interview/README.zh-CN.md#week-1) — 先脱稿回答，再对照要点，关联自己的代码或评测。

<a id="week-2"></a>
## Week 2 — 结构化调用

1. **学:** [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/) — 依次看基础模型、额外字段、类型转换/严格模式、校验错误。
2. **做:** 运行 Lab 01；在自己的项目里接入一个真实模型适配器，增加有界重试和超时。
3. **验收:** 拒绝非法输出，把格式通过率与分类正确率分开统计。
4. **面试:** [Week 2](interview/README.zh-CN.md#week-2) — 先脱稿回答，再对照要点，关联自己的代码或评测。

<a id="week-3"></a>
## Week 3 — 检索基线

1. **学:** [DeepLearning.AI — Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation) — 先学文档摄取、切块与检索评测。
2. **做:** 运行 Lab 02；把 6 条玩具查询扩展到自己文档的 20 条标注查询，之后再加带引用的回答。
3. **验收:** 报告 Recall@k/MRR 并检查 3 个失败，区分检索错误与无依据回答。
4. **面试:** [Week 3](interview/README.zh-CN.md#week-3) — 先脱稿回答，再对照要点，关联自己的代码或评测。

<a id="week-4"></a>
## Week 4 — 检索改进

1. **学:** [DeepLearning.AI — Retrieval Augmented Generation](https://www.deeplearning.ai/courses/retrieval-augmented-generation) — 选学混合检索与重排，每次只改一个组件。
2. **做:** 比较词法基线和一个向量/混合/重排方案，预留不用于调参的测试查询。
3. **验收:** 固定数据和配置，即使新方案更差也记录质量与延迟，接受负结果。
4. **面试:** [Week 4](interview/README.zh-CN.md#week-4) — 先脱稿回答，再对照要点，关联自己的代码或评测。

<a id="week-5"></a>
## Week 5 — 工具工作流

**先运行:** [Lab 03](labs/lab03_tool_calling/README.zh-CN.md)

1. **学:** [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — 读 Workflow、路由和工具设计；可补 Agentic AI 工具调用内容。
2. **做:** 实现两个只读工具和一个 Issue 草稿工具，写入需要明确审批边界。
3. **验收:** 测试错误参数、工具失败和重复请求，讲清幂等性。
4. **面试:** [Week 5](interview/README.zh-CN.md#week-5) — 先脱稿回答，再对照要点，关联自己的代码或评测。

<a id="week-6"></a>
## Week 6 — 有状态 Agent

**先运行:** [Lab 04](labs/lab04_agent_state/README.zh-CN.md)

1. **学:** [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — 读 Agent Loop 与终止条件，可选学规划。
2. **做:** 加入步数/时间预算、持久化状态与审批，模拟工具调用后中断。
3. **验收:** 恢复时不重复写入，验证能终止且审批对应明确动作。
4. **面试:** [Week 6](interview/README.zh-CN.md#week-6) — 先脱稿回答，再对照要点，关联自己的代码或评测。

<a id="week-7"></a>
## Week 7 — 系统化评测

**先运行:** [Lab 05](labs/lab05_agent_evals/README.zh-CN.md)

1. **学:** [DeepLearning.AI — Evaluating AI Agents](https://www.deeplearning.ai/short-courses/evaluating-ai-agents/) — 优先学习组件评测、轨迹评测和 Judge 校准。
2. **做:** 扩展到至少 50 条样例，分开发/测试集，增加确定性评分与人工复核。
3. **验收:** 在保留集比较两版，报告样本数、分组结果和 Judge 与人工分歧。
4. **面试:** [Week 7](interview/README.zh-CN.md#week-7) — 先脱稿回答，再对照要点，关联自己的代码或评测。

<a id="week-8"></a>
## Week 8 — 权限边界

1. **学:** [OWASP — LLM Top 10](https://genai.owasp.org/llm-top-10/) — 读资源表指定的三类风险，映射到自己的工具。
2. **做:** 增加租户过滤和 10 条对抗样例，覆盖注入、泄露和绕过审批。
3. **验收:** 当前测试集无未授权写入，并说明覆盖局限，不宣称绝对安全。
4. **面试:** [Week 8](interview/README.zh-CN.md#week-8) — 先脱稿回答，再对照要点，关联自己的代码或评测。

<a id="week-9"></a>
## Week 9 — 生产化

1. **学:** [Google — Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/) — 选读三个 SRE 章节，应用到模型调用链。
2. **做:** 部署一个服务，加入 Trace ID、预算限制、超时和降级，做小规模负载实验。
3. **验收:** 报告 p95、每次成功任务成本、负载/样本数和回滚步骤。
4. **面试:** [Week 9](interview/README.zh-CN.md#week-9) — 先脱稿回答，再对照要点，关联自己的代码或评测。

<a id="week-10"></a>
## Week 10 — Coding Agent 工作流

1. **学:** [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — 回看 Coding Agent 与工具设计，结合执行环境的官方隔离文档。
2. **做:** 在限制凭据与网络的隔离临时环境生成小补丁，审查 Diff 和测试。
3. **验收:** 展示边界确实受限；临时目录或测试通过本身不等于沙箱/安全证明。
4. **面试:** [Week 10](interview/README.zh-CN.md#week-10) — 先脱稿回答，再对照要点，关联自己的代码或评测。

<a id="week-11"></a>
## Week 11 — 系统设计与产品取舍

1. **学:** [System Design Primer](https://github.com/donnemartin/system-design-primer) — 选读缓存、队列和存储取舍，围绕项目需求设计。
2. **做:** 写两篇 ADR，画数据/权限流，根据评测证据砍掉一个功能。
3. **验收:** 能比较更简单的方案，解释流量增加 10 倍后该改什么。
4. **面试:** [Week 11](interview/README.zh-CN.md#week-11) — 先脱稿回答，再对照要点，关联自己的代码或评测。

<a id="week-12"></a>
## Week 12 — 作品集与面试

1. **学:** [Chip Huyen — AI Engineering companion repository](https://github.com/chiphuyen/aie-book) — 复习自己的薄弱主题，再按面试指南做模拟。
2. **做:** 发布可复现步骤、评测报告、架构图和 3–5 分钟 Demo，完成两次模拟面试。
3. **验收:** 其他人能复现结果，每个简历数字都有来源与局限说明。
4. **面试:** [Week 12](interview/README.zh-CN.md#week-12) — 先脱稿回答，再对照要点，关联自己的代码或评测。

## 继续学习

达到本周验收标准后再继续；每周更新进度表中的面试复盘。完整主线仍见 [ROADMAP.md](ROADMAP.md)。课程访问与资料来源说明见 [面试资源表](interview/README.zh-CN.md#resources)。
