# 🚀 Naiba OpenAI Work Assistant

<div align="center">

**你的智能AI工作助手**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-blue)](https://claude.ai/claude-code)
[![Prompts](https://img.shields.io/badge/Prompts-230+-green)](#)
[![Roles](https://img.shields.io/badge/Roles-10-purple)](#)

**230+ 专业提示词 • 10个职业角色 • 智能推荐 • 双语支持**

[快速开始](#-快速开始) • [功能特性](#-功能特性) • [文档](#-文档) • [贡献](#-贡献)

</div>

---

## ✨ 这是什么？

**Naiba OpenAI Work Assistant** 是一个为 Claude Code 打造的强大插件，包含来自 OpenAI Academy 的 **230+ 个专业提示词**，覆盖 **10 个职场角色**。

它能自动检测你的角色和场景，推荐最佳提示词，并适应你的语言偏好（英文/中文）。

---

## 🎯 功能特性

### 🧠 智能角色检测
- 自动从上下文中识别你的职业角色
- 支持 10+ 个角色：销售、产品、工程、HR、IT、经理、高管等
- 从对话历史中学习

### 🔍 智能提示词匹配
- 在 230+ 个提示词中搜索完美匹配
- 基于相关性的排序算法
- Top 3 推荐并附带解释

### 🌐 双语支持
- **英文**和**中文**完全支持
- 自动检测你的语言偏好
- 动态调整引导语言

### 📂 三种使用模式
1. **智能模式**（默认）- 只需描述你的任务
2. **浏览模式** - 探索某个角色的所有提示词
3. **直接模式** - 通过名称使用特定提示词

### ⚡ 参数智能提取
- 从你的输入中推断参数
- 最小化来回询问
- 智能上下文理解

---

## 📊 支持的角色

| 角色 | 提示词数量 | 主要功能 |
|------|-----------|----------|
| 🔫 **销售 (Sales)** | 25+ | 外联、策略、竞品情报 |
| 🤝 **客户成功 (Customer Success)** | 25+ | 入职引导、QBR、续约、健康评分 |
| 📦 **产品 (Product)** | 25+ | 调研、路线图、PRD、A/B测试 |
| 💻 **工程师 (Engineers)** | 25+ | 调试、文档、基准测试、架构 |
| 👥 **人力 (HR)** | 25+ | 招聘、员工参与、合规、政策 |
| 🖥️ **IT** | 20+ | 云服务、安全、合规、事件管理 |
| 👔 **经理 (Managers)** | 20+ | 目标、1:1面谈、团队健康、教练 |
| 🏢 **高管 (Executives)** | 20+ | 战略、沟通、投资者更新 |
| 🏛️ **政府IT (Government IT)** | 20+ | 安全、漏洞管理、合规性 |
| 🌟 **通用 (Any Role)** | 20+ | 通用职场提示词 |

---

## 🚀 快速开始

### 安装步骤

1. 克隆或下载此仓库
2. 复制到 Claude Code 插件目录：
   ```bash
   cp -r naiba-openai-work-assistant ~/.claude/plugins/custom/
   ```
3. 重启 Claude Code（重要！）
4. 开始使用！

### 就这么简单！

当你开始对话时，skill会自动加载。

### 立即试用！

```
你：帮我写个冷邮件给CEO
Claude：[自动检测销售场景]
      [推荐最佳提示词]
      [引导你完成定制]
      [生成专业邮件]
```

---

## 💡 使用示例

### 中文示例

```
→ "帮我写个冷邮件"
→ "分析客户反馈"
→ "准备绩效考核"
→ "写个产品路线图"
```

### 浏览提示词

```
→ "看看产品经理提示词"
→ "列出所有HR提示词"
→ "浏览销售提示词"
```

---

## 📁 项目结构

```
naiba-openai-work-assistant/
├── skills/                              # 11个skill模块
│   ├── naiba-openai-work-assistant/     # 主入口
│   ├── naiba-openai-sales/              # 销售skill
│   ├── naiba-openai-product/            # 产品skill
│   └── ... (10个角色skills)
├── shared/                              # 共享工具和数据
│   ├── prompts_index.json               # 201个提示词索引
│   └── role_mapping.json                # 角色映射
├── README.md                            # 英文文档
├── README_CN.md                         # 中文文档（本文件）
└── LICENSE                              # MIT许可证
```

---

## 🎓 文档

- **[QUICKSTART.md](QUICKSTART.md)** - 3步快速入门 ⭐
- **[INSTALL.md](INSTALL.md)** - 详细安装指南
- **[TESTING.md](TESTING.md)** - 测试用例和示例
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - 项目完成总结

---

## 🛠️ 技术细节

### 架构

**设计模式：** 逻辑分离
- **单一包** - 易于安装
- **模块化设计** - 10个独立角色skills
- **共享工具** - 避免代码重复
- **智能路由** - 自动角色检测

### 技术栈

- **语言：** Markdown (skills)、JSON (数据)
- **平台：** Claude Code Plugin System
- **数据源：** OpenAI Academy Prompt Packs
- **算法：** 基于关键词的相关性评分

### 性能

- **加载时间：** < 1秒
- **匹配时间：** < 1.2秒
- **总响应时间：** < 3秒
- **内存占用：** ~500KB

---

## 🤝 贡献

欢迎各种形式的贡献！

**贡献方式：**
- 添加新提示词 - 编辑源数据并运行转换脚本
- 改进匹配 - 调整评分算法
- 支持更多语言 - 添加语言检测规则
- 增强文档 - 改进指南和示例
- 报告错误 - 创建issue并提供详情

### 开发设置

1. Fork 本仓库
2. 创建功能分支
3. 进行更改
4. 充分测试
5. 提交 Pull Request

---

## 📝 许可证

本项目采用 MIT 许可证 - 详情参见 [LICENSE](LICENSE) 文件。

**归属：**
提示词来源于 OpenAI Academy 的公开 Prompt Packs 集合，按照 OpenAI 的服务条款使用。

---

## 🙏 致谢

- **OpenAI Academy** - 提供精彩的 Prompt Packs 集合
- **Claude & Anthropic** - 创建 Claude Code
- **社区** - 反馈和改进

---

## 📞 支持

- 📖 **文档：** 查看[文档部分](#-文档)
- 🐛 **问题：** [在GitHub上创建issue](https://github.com/zstmfhy/naiba-openai-work-assistant/issues)
- 💬 **讨论：** [加入GitHub讨论](https://github.com/zstmfhy/naiba-openai-work-assistant/discussions)

---

## 🌟 给这个项目点星！

如果你觉得这个项目有帮助，请给它一个 ⭐ star！

---

<div align="center">

**由 [zstmfhy](https://github.com/zstmfhy) 用 ❤️ 制作**

**基于 OpenAI Academy Prompt Packs**

[⬆ 回到顶部](#-naiba-openai-work-assistant)

</div>
