# Naiba OpenAI Work Assistant - Shared Utilities

This directory contains shared utility functions and data used by all role-specific skills.

## Files

### prompts_index.json
Complete index of all 230+ prompts with role assignments, categories, and keyword mappings.

### role_mapping.json
Mapping of role IDs to role names, aliases, and descriptions.

### language_detection.md
Language detection and adaptation logic for English/中文 support.

### prompt_matcher.md
Prompt matching and ranking algorithm for smart recommendations.

---

## Language Detection Logic

### Detection Rules

1. **Explicit Language Declaration**
   - "用中文" / "in English"
   - "中文回复" / "respond in Chinese"

2. **Input Language Detection**
   - Check first 100 characters of user input
   - Count Chinese characters vs English words
   - If Chinese characters > 30% → Chinese
   - Otherwise → English

3. **Session Preference Memory**
   - Remember user's language choice during session
   - Adapt future responses accordingly

### Response Language Rules

| Input Language | Guidance Language | Prompt Titles |
|----------------|-------------------|---------------|
| Chinese | Chinese (中文) | English (original) |
| English | English | English |
| Mixed | Follow dominant (60%+) | English |

### Implementation Example

```
User: "帮我写个冷邮件"
→ Detection: 100% Chinese characters
→ Response: Chinese guidance
→ Prompt Title: "Draft a personalized cold outreach email" (保持英文)
→ Parameters: 用中文引导填写

User: "Help me write a cold email"
→ Detection: 100% English
→ Response: English guidance
→ Prompt Title: "Draft a personalized cold outreach email"
→ Parameters: Guide in English
```

---

## Prompt Matching Algorithm

### Scoring System

For each prompt in the database, calculate relevance score:

```python
score = 0

# Title match (highest weight)
if user_keyword in prompt_title:
    score += 10

# Category/Description match
if user_keyword in prompt_description:
    score += 5

# Prompt template match
if user_keyword in prompt_template:
    score += 3

# Role match bonus
if detected_role == prompt_role:
    score += 2
```

### Ranking & Selection

1. Calculate scores for all relevant prompts
2. Sort by score (descending)
3. Return Top 3 recommendations
4. If top score > 80% confidence, auto-select
5. Otherwise, present choices to user

### Example

```
User Input: "cold email to CEO"

Keywords: ['cold', 'email', 'ceo']

Prompt A: "Draft a personalized cold outreach email"
  - Title matches: 'cold', 'email' → 10 + 10 = 20
  - Category: "Outreach & communication" → 0
  - Role: Sales → 2
  - Total: 22

Prompt B: "Rework demo follow-up email"
  - Title matches: 'email' → 10
  - Total: 12

Result: Prompt A ranked #1 (recommended)
```

---

## Role Detection Logic

### Detection Methods

#### Method 1: Explicit Statement
- "I'm a product manager"
- "我是销售" / "作为工程师"
- "As a sales rep..."

#### Method 2: Keyword Matching

| Keywords | Detected Role |
|----------|--------------|
| cold email, pipeline, deal, demo, close, outreach | Sales |
| churn, QBR, onboarding, retention, account health | Customer Success |
| PRD, roadmap, feature, monetization, A/B test | Product |
| bug, API, deploy, code, log, debug | Engineering/IT |
| recruiting, JD, performance, employee, hiring | HR |
| 1:1, team, goals, feedback, direct report | Manager |
| strategy, board, investor, M&A, KPI | Executive |
| compliance, SLA, incident, security, policy | IT/Gov |

#### Method 3: Context Inference
- Previous conversation history
- File attachments (code → engineer, resume → HR)
- Task descriptions

### Confidence Levels

- **High (80%+)**: Auto-select role, proceed with prompt matching
- **Medium (50-79%)**: Ask confirmation
- **Low (<50%)**: Present role options or ask user

---

## Error Handling

### No Match Found

If no prompt achieves minimum score threshold:

1. **Show closest alternatives**
   ```
   No exact match found. Did you mean:
   - [Similar prompt 1]
   - [Similar prompt 2]
   ```

2. **Ask clarifying questions**
   ```
   Could you provide more details about:
   - What role are you in?
   - What's the specific task?
   - What outcome are you looking for?
   ```

3. **Fallback to browse mode**
   ```
   Would you like to browse all prompts for [detected role]?
   ```

### Parameter Extraction Failures

If user doesn't provide required parameters:

1. **Smart inference** from context
2. **Guided questions** in detected language
3. **Example suggestions** to help user understand

---

## Data Structures

### Prompt Entry Structure

```json
{
  "id": "sales-outreach-01",
  "role_id": "sales",
  "role_name": "Sales",
  "category": "Outreach & communication",
  "title": "Draft a personalized cold outreach email",
  "prompt": "Write a short, compelling cold email...",
  "keywords": ["email", "outreach", "cold", "prospecting"],
  "parameters": [
    {"name": "job_title", "type": "string", "required": true},
    {"name": "company_name", "type": "string", "required": true},
    {"name": "value_props", "type": "text", "required": true}
  ]
}
```

### Role Entry Structure

```json
{
  "id": "sales",
  "name": "Sales",
  "aliases": ["sales", "business development", "bd", "revenue"],
  "description": "Prompts for sales teams",
  "categories": [
    {
      "name": "Outreach & communication",
      "prompt_count": 5,
      "prompts": ["sales-outreach-01", "sales-outreach-02", ...]
    }
  ],
  "total_prompts": 25
}
```

---

## Integration Guide

### For Role-Specific Skills

Each role skill should:

1. **Load shared index** at initialization
2. **Filter by role_id** for prompt listings
3. **Use shared matcher** for recommendations
4. **Apply language rules** for responses
5. **Handle errors** per shared guidelines

### Example Usage

```markdown
<!-- In sales-specific SKILL.md -->

## Load Shared Utils

Load the shared prompts index and filter for sales role:

```json
{
  "load": "shared/prompts_index.json",
  "filter": {"role_id": "sales"}
}
```

## Browse Sales Prompts

Iterate through sales categories and display prompts...

## Smart Recommendation

Use shared matcher with user input:
1. Detect language
2. Extract keywords
3. Calculate scores (use shared algorithm)
4. Return Top 3 sales prompts
```

---

## Maintenance

### Adding New Prompts

1. Add to `all_prompt_packs.json`
2. Run conversion script
3. Regenerate `prompts_index.json`
4. Update role-specific skills (if automated)

### Updating Role Aliases

Edit `role_mapping.json` with new aliases:
```json
{
  "sales": {
    "aliases": ["sales", "business development", "bd", "revenue", "account executive"]
  }
}
```

### Tuning Matching Algorithm

Adjust scoring weights in `prompt_matcher.md`:
- Title match weight (default: 10)
- Description match weight (default: 5)
- Template match weight (default: 3)

---

## Performance Notes

- **Total prompts indexed**: 230+
- **Average lookup time**: < 100ms
- **Memory footprint**: ~500KB for full index
- **Recommended**: Load index once per session

---

**Last Updated**: January 2026
**Version**: 1.0.0
