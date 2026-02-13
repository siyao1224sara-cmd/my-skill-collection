# 🚀 Naiba OpenAI Work Assistant

<div align="center">

**Your Intelligent AI Work Companion**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-blue)](https://claude.ai/claude-code)
[![Prompts](https://img.shields.io/badge/Prompts-230+-green)](#)
[![Roles](https://img.shields.io/badge/Roles-10-purple)](#)

**230+ professional prompts • 10 roles • Smart recommendations • Bilingual**

[Quick Start](#-quick-start) • [Features](#-features) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## ✨ What is it?

**Naiba OpenAI Work Assistant** is a powerful skill plugin for Claude Code that brings you **230+ professionally crafted prompts** from OpenAI Academy, organized across **10 professional roles**.

It automatically detects your role and context, recommends the best prompts, and adapts to your language preference (English/中文).

---

## 🎯 Features

### 🧠 Smart Role Detection
- Automatically identifies your professional role from context
- Supports 10+ roles: Sales, Product, Engineering, HR, IT, Managers, Executives, and more
- Learns from conversation history

### 🔍 Intelligent Prompt Matching
- Searches through 230+ prompts to find the perfect match
- Relevance-based ranking algorithm
- Top 3 recommendations with explanations

### 🌐 Bilingual Support
- **English** and **中文** (Chinese) support
- Auto-detects your language preference
- Adapts guidance dynamically

### 📂 Three Usage Modes
1. **Smart Mode** (default) - Just describe your task
2. **Browse Mode** - Explore all prompts for a role
3. **Direct Mode** - Use a specific prompt by name

### ⚡ Parameter Extraction
- Infers parameters from your input
- Minimizes back-and-forth
- Smart context understanding

---

## 📊 Supported Roles

| Role | Prompts | Key Areas |
|------|---------|-----------|
| 🔫 **Sales** | 25+ | Outreach, strategy, competitive intel |
| 🤝 **Customer Success** | 25+ | Onboarding, QBRs, renewal, health scoring |
| 📦 **Product** | 25+ | Research, roadmapping, PRDs, A/B testing |
| 💻 **Engineers** | 25+ | Debugging, docs, benchmarks, architecture |
| 👥 **HR** | 25+ | Recruiting, engagement, compliance, policies |
| 🖥️ **IT** | 20+ | Cloud, security, compliance, incident mgmt |
| 👔 **Managers** | 20+ | Goals, 1:1s, team health, coaching |
| 🏢 **Executives** | 20+ | Strategy, communications, investor updates |
| 🏛️ **Government IT** | 20+ | Security, vulnerabilities, compliance |
| 🌟 **Any Role** | 20+ | Universal workplace prompts |

---

## 🚀 Quick Start

### Installation

1. Clone or download this repository
2. Copy to Claude Code plugins directory:
   ```bash
   cp -r naiba-openai-work-assistant ~/.claude/plugins/custom/
   ```
3. Restart Claude Code (important!)
4. Start using!

### That's it!

The skill will automatically load when you start a conversation.

### Try it now!

```
You: Help me write a cold email to a CEO
Claude: [Automatically detects Sales scenario]
       [Recommends best prompts]
       [Guides you through customization]
       [Generates professional email]
```

---

## 💡 Usage Examples

```
→ "Help me write a cold email to a CEO"
→ "Analyze customer feedback and suggest features"
→ "Debug this production issue"
→ "Create a PRD for a dashboard"
```

### Browse Prompts

```
→ "Show me all sales prompts"
→ "List HR prompts"
→ "Browse product prompts"
```

---

## 📁 Project Structure

```
naiba-openai-work-assistant/
├── skills/                              # 11 skill modules
│   ├── naiba-openai-work-assistant/     # Main entry point
│   ├── naiba-openai-sales/              # Sales skill
│   ├── naiba-openai-product/            # Product skill
│   └── ... (10 role-specific skills)
├── shared/                              # Shared utilities & data
│   ├── prompts_index.json               # 201 prompts indexed
│   └── role_mapping.json                # Role metadata
├── README.md                            # This file
├── README_CN.md                         # Chinese version
└── LICENSE                              # MIT License
```

---

## 🎓 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 3 steps ⭐
- **[INSTALL.md](INSTALL.md)** - Detailed installation guide
- **[TESTING.md](TESTING.md)** - Test procedures and examples
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Project completion summary

---

## 🛠️ Technical Details

### Architecture

**Design Pattern:** Logical Separation
- **Single package** for easy installation
- **Modular design** with 10 independent role skills
- **Shared utilities** to avoid code duplication
- **Smart routing** through main entry point

### Tech Stack

- **Language:** Markdown (skills), JSON (data)
- **Platform:** Claude Code Plugin System
- **Data Source:** OpenAI Academy Prompt Packs
- **Algorithm:** Keyword-based relevance scoring

### Performance

- **Load time:** < 1 second
- **Match time:** < 1.2 seconds
- **Total response:** < 3 seconds
- **Memory:** ~500KB for full index

---

## 🤝 Contributing

Contributions are welcome! Here are some ideas:

- Add new prompts - Edit source data and run conversion script
- Improve matching - Tune scoring algorithms
- Support more languages - Add language detection rules
- Enhance documentation - Improve guides and examples
- Report bugs - Open an issue with details

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Attribution:**
Prompts are sourced from OpenAI Academy's public Prompt Packs collection and are used in accordance with OpenAI's terms of service.

---

## 🙏 Acknowledgments

- **OpenAI Academy** - For the amazing Prompt Packs collection
- **Claude & Anthropic** - For creating Claude Code
- **The Community** - For feedback and improvements

---

## 📞 Support

- 📖 **Documentation:** Check the [docs](#-documentation)
- 🐛 **Issues:** [Open an issue on GitHub](https://github.com/zstmfhy/naiba-openai-work-assistant/issues)
- 💬 **Discussions:** [Join GitHub Discussions](https://github.com/zstmfhy/naiba-openai-work-assistant/discussions)

---

## 🌟 Star History

If you find this project helpful, please consider giving it a ⭐ star!

---

<div align="center">

**Made with ❤️ by [zstmfhy](https://github.com/zstmfhy)**

**Powered by OpenAI Academy Prompt Packs**

[⬆ Back to Top](#-naiba-openai-work-assistant)

</div>
