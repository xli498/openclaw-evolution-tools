# OpenClaw 记忆与任务演进工具集

面向 OpenClaw 的记忆治理、经验沉淀和任务可靠性参考。它不是 OpenClaw 官方组件，不是“一键变聪明”安装包，也不会自动替换当前实例的记忆、Skill、模型或 cron。

## 先看结论

- 已有结构化记忆或召回插件时，先确认唯一写入源，默认不要叠加第二套长期写入链。
- 文件存在、Skill 已扫描或提案处于 pending，都不能单独证明功能已生效。
- 任何记忆、自进化或自动化改动，都要经过运行态验证、新会话回归和实际任务验收。
- 生产配置、凭据、用户数据、私有 Prompt 和敏感 payload 不进入仓库。

## 解决什么问题

| 能力 | 目标 | 验收重点 |
|:--|:--|:--|
| 记忆治理 | 让跨会话信息可检索、可追溯、可淘汰 | 写入、检索、冲突和唯一写入源 |
| 经验闭环 | 将错误、纠正和最佳实践变成可审查候选 | 事件记录、修复证据、人工批准和 promotion |
| Skill 演进 | 把稳定的可复用流程沉淀为技能 | 正式扫描路径、新会话召回和实际遵循 |
| 任务可靠性 | 建立首选路由、失败降级、结果验收和复用 | 按任务类型的真实输出验收 |

## 工具与现有运行时的关系

本仓库只提供选型、边界和集成参考，不自动安装组件，也不假定某个第三方记忆系统适合所有实例。使用前先确认：

1. 当前 OpenClaw 版本和正式配置路径；
2. 已启用的 memory、Skill、cron 和插件；
3. 谁是唯一长期记忆写入源；
4. 是否会联网、外发、写配置或消耗模型额度；
5. 如何停止、回滚和验证。

## 推荐工作流

```text
只读盘点 → 选择单一路由 → 最小变更 → 本地验证
       → 运行态复核 → 新会话回归 → 实际任务验收
       → 记录可复用规则
```

### 记忆验收

不要只检查 `MEMORY.md` 或数据库文件是否存在。至少分别验证：

- 新事实是否确实写入目标存储；
- 关键词/语义检索是否能召回；
- 新会话是否能召回；
- 冲突和过期信息是否有处理规则；
- 实际任务是否遵循了记忆中的约束。

### 经验与 Skill 验收

- `open`：记录错误、纠正、知识缺口或最佳实践；
- `resolved`：写明修复方案和最小验证证据；
- `pending`：只表示候选提案，不能表述为已生效；
- `promoted`：必须有人工批准和目标文件/提案引用；
- 新 Skill：必须通过正式扫描，并在新会话和真实任务中回归。

## 安全边界

- 不绕过受保护配置、审批、验证器或平台安全边界；
- 不把归档脚本未经审查挂回生产 cron；
- 不用一次子代理成功证明主会话、全新会话或长期运行已稳定；
- 不自动发布、外发、删除或覆盖外部数据；
- 不提交凭据、私有 Prompt、用户数据、私有 endpoint 或敏感日志。

## 适用与不适用

**适用：** OpenClaw 记忆架构评估、Skill 选型、错误经验闭环、任务验收和迁移前审查。

**不适用：** 把示例当作通用安装命令、同时启用多个长期写入链、未经确认修改生产配置，或替代当前版本的官方文档。

## 相关参考

- [OpenClaw 官方文档](https://docs.openclaw.ai/)
- [OpenClaw](https://github.com/openclaw/openclaw)
- [Agent Skills 规范参考](https://github.com/anthropics/skills)
- [OpenClaw Skills 社区索引](https://github.com/VoltAgent/awesome-openclaw-skills)
- [Claude Mem：跨会话记忆实践](https://github.com/thedotmack/claude-mem)
- [GBrain：常驻记忆服务实践](https://github.com/garrytan/gbrain)

## Skill 清单

仓库中的 Skill 全部是受控评估或治理参考：`async-artifact-delivery-state-machine`、`evomap-evolver`、`gep-evolution-flow`、`github-repo-quality-gate`、`memos-local`、`multi-provider-config-safety`、`scheduled-model-failure-recovery`、`self-improving-agent`、`selflearn-experience-closure`。它们不构成安装指令，也不会自动创建、应用或发布 Skill。

## 许可证

MIT
