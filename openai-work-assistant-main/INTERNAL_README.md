# Naiba OpenAI Work Assistant

An intelligent AI work companion with **230+ professional prompts** across **10 professional roles**, sourced from OpenAI Academy Prompt Packs.

## 📁 Structure

```
naiba-openai-work-assistant/
├── skills/                          # Skill definitions (Claude Code format)
│   ├── naiba-openai-work-assistant/ # Main entry point skill
│   │   └── SKILL.md
│   ├── naiba-openai-sales/          # Sales-specific skill
│   │   └── SKILL.md
│   ├── naiba-openai-product/        # Product-specific skill
│   │   └── SKILL.md
│   ├── naiba-openai-engineers/      # Engineering-specific skill
│   │   └── SKILL.md
│   ├── naiba-openai-hr/             # HR-specific skill
│   │   └── SKILL.md
│   ├── naiba-openai-it/             # IT-specific skill
│   │   └── SKILL.md
│   ├── naiba-openai-managers/       # Manager-specific skill
│   │   └── SKILL.md
│   ├── naiba-openai-executives/     # Executive-specific skill
│   │   └── SKILL.md
│   ├── naiba-openai-customer-success/ # Customer Success skill
│   │   └── SKILL.md
│   ├── naiba-openai-government-it-staff/ # Government IT skill
│   │   └── SKILL.md
│   └── naiba-openai-any-role/       # Universal prompts
│       └── SKILL.md
│
├── shared/                          # Shared utilities and data
│   ├── utils.md                     # Utility functions documentation
│   ├── prompts_index.json           # Complete prompt index
│   └── role_mapping.json            # Role aliases and metadata
│
├── roles/                           # Generated role files (intermediate)
│   ├── sales.md
│   ├── product.md
│   └── ...
│
├── openai_prompt_packs/             # Source data
│   ├── all_prompt_packs.json        # Original JSON from website
│   └── convert_to_skill_format.py   # Conversion script
│
└── README.md                        # This file
```

## 🎯 Architecture

### Design Pattern: Logical Separation (方案C-2)

This skill uses a **logical separation architecture**:
- **Physically**: One skill package (`naiba-openai-work-assistant`)
- **Logically**: 11 independent skill modules (1 main + 10 role-specific)
- **Shared**: Common utilities and data across all modules

### How It Works

1. **Main Entry Point** (`naiba-openai-work-assistant`)
   - Receives all user requests
   - Detects role and language
   - Routes to appropriate role-specific skill
   - Orchestrates the response

2. **Role-Specific Skills** (`naiba-openai-{role}`)
   - Contain prompts for one role only
   - Can be used independently if needed
   - Share common utilities

3. **Shared Layer**
   - Language detection & adaptation
   - Prompt matching algorithm
   - Role detection logic
   - Error handling patterns

## 🚀 Usage

### Installation

Copy the entire `naiba-openai-work-assistant` folder to:

```
~/.claude/plugins/custom/naiba-openai-work-assistant/
```

### Basic Usage

Just start using it in Claude Code:

```
You: Help me write a cold email to a CEO
Claude: [Automatically loads naiba-openai-work-assistant]
       [Detects Sales scenario]
       [Recommends "Draft a personalized cold outreach email"]
       [Guides you through customization]
```

### Advanced Usage

#### Browse All Sales Prompts
```
You: Show me sales prompts
Claude: [Lists all 25+ sales prompts organized by category]
```

#### Use a Specific Prompt
```
You: Use "Analyze product feedback themes"
Claude: [Loads that specific prompt]
       [Asks for required parameters]
       [Executes with your data]
```

#### Chinese Language Support
```
You: 帮我分析客户反馈
Claude: [检测到中文，用中文引导]
       [Recommended: "Analyze product feedback themes"]
       [请提供：客户反馈数据...]
```

## 📊 Statistics

| Metric | Count |
|--------|-------|
| **Total Skills** | 11 (1 main + 10 roles) |
| **Total Prompts** | 230+ |
| **Roles Covered** | 10 |
| **Languages** | English, 中文 |
| **Categories** | 50+ |
| **Source** | OpenAI Academy Prompt Packs |

## 🛠️ Development

### Adding New Prompts

1. Edit `openai_prompt_packs/all_prompt_packs.json`
2. Run the conversion script:
   ```bash
   cd openai_prompt_packs
   python3 convert_to_skill_format.py
   ```
3. Copy generated files to skill directories
4. Test with Claude Code

### Updating Role Aliases

Edit `shared/role_mapping.json` to add new aliases:
```json
{
  "sales": {
    "aliases": ["sales", "business development", "bd", "ae", "account executive"]
  }
}
```

### Tuning Matching Algorithm

Edit scoring weights in `shared/utils.md` under "Prompt Matching Algorithm".

## 📖 Skills Reference

### Main Skills

| Skill | Prompts | Description |
|-------|---------|-------------|
| **naiba-openai-work-assistant** | All | Main entry point, auto-detects role and routes |
| **naiba-openai-any-role** | 20+ | Universal prompts for any role |

### Role-Specific Skills

| Skill | Prompts | Key Areas |
|-------|---------|-----------|
| **naiba-openai-sales** | 25+ | Outreach, strategy, competitive intel, analysis |
| **naiba-openai-customer-success** | 25+ | Onboarding, QBRs, renewal, health scoring |
| **naiba-openai-product** | 25+ | Research, roadmapping, PRDs, A/B testing |
| **naiba-openai-engineers** | 25+ | Debugging, docs, benchmarks, architecture |
| **naiba-openai-hr** | 25+ | Recruiting, engagement, compliance, policies |
| **naiba-openai-it** | 20+ | Cloud, security, compliance, incident mgmt |
| **naiba-openai-managers** | 20+ | Goals, 1:1s, team health, coaching |
| **naiba-openai-executives** | 20+ | Strategy, communications, investor updates |
| **naiba-openai-government-it-staff** | 20+ | Security, vulnerabilities, compliance |

## 🌐 Language Support

- **English**: Full support (primary)
- **中文**: Full support (auto-detected)
- **Others**: Prompts work, but guidance is English/中文 only

Language detection is automatic based on your input language.

## 🔒 Privacy & Data

- **No external API calls** - All prompts are local
- **No telemetry** - Nothing is sent back
- **Open source** - Fully transparent and auditable
- **Source attribution** - All prompts from OpenAI Academy

## 📜 License

These prompts are sourced from OpenAI Academy's public Prompt Packs collection.
Please refer to OpenAI's terms of service for usage guidelines.

## 🤝 Contributing

To contribute improvements:

1. Test the skills thoroughly
2. Document issues or suggestions
3. Submit pull requests with clear descriptions
4. Maintain the existing structure and format

## 📞 Support

For issues or questions:
1. Check this README first
2. Review `shared/utils.md` for technical details
3. Examine individual skill SKILL.md files

---

**Version**: 1.0.0
**Last Updated**: January 2026
**Created by**: Naiba (based on OpenAI Academy content)
