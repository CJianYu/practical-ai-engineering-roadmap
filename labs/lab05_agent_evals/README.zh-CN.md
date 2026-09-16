# Lab 05 — Agent 评测与回归门禁

[English](README.md) · [简体中文](README.zh-CN.md)

把八条固定工具调用样例送入 Lab 03，比较基线/候选的工具选择、执行状态、最终 Issue 数量、安全违规与错误分组。这里测的是固定样例行为，不是在线模型智能。

## 运行

在仓库根目录，完成依赖安装后运行（Python 3.11+，推荐 3.12）：

```bash
python -m labs.lab05_agent_evals.evals
python -m pytest tests/test_agent_evals.py -q
```

无需 API Key 或网络。演示使用临时目录并在结束后清理，不修改你的项目文件。

## 跟着做

1. 读 `data/cases.jsonl`：每行包含可信预期结果和固定的 baseline/candidate/regressed 提议。审批由评测器设置，不能来自模型输出。
2. 运行默认比较：基线通过 7/8，候选通过 8/8，双方均无未授权写入。这是特意构造的教学结果。
3. 查看 JSON 中逐条结果和分组；只有预期就是拒绝时，非法调用被拦截才算成功。
4. 运行 `--candidate regressed`：总通过率仍为 7/8，但 `lookup` 退步，进程退出码为 1。门禁通过不等于达到生产要求。

## 练习

1. 使用 `--output /tmp/agent-eval-report.json` 保存报告，定位失败样例并提出修复。
2. 添加 10 条保留样例，标明预期副作用与信任边界，开发集与测试集分离；样例 ID 和标签不送入模型。
3. 把固定调用换成两个冻结模型/Prompt 版本的输出，另行记录模型配置、重复运行、真实用量和延迟；只有确定性检查无法判断时，才增加经过人工校准的 Judge。

```bash
python -m labs.lab05_agent_evals.evals --output /tmp/agent-eval-report.json
# Expected exit code: 1 (intentional regression)
python -m labs.lab05_agent_evals.evals --candidate regressed
```

## 边界与局限

八条数据是小型合成样例，不声称具有统计显著性或代表真实生产分布。未包含真实模型、LLM Judge、校准质量分数、成本或延迟基准。门禁拒绝逐条回归、总体质量下降或任何未授权写入，但没有统一最低质量门槛；生产阈值应由任务风险与真实负载确定。

## 验收与面试

- [ ] 运行默认演示及测试，解释输出。
- [ ] 完成一个变更实验，记录预期与实际结果。
- [ ] 脱稿解释一次失败与一个生产环境差异。

[Week 7 学习任务](../../STUDY_GUIDE.zh-CN.md#week-7) · [Interview](../../interview/README.zh-CN.md#week-7)
