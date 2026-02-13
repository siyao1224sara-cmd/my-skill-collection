# Naiba OpenAI Work Assistant - Testing Guide

This guide provides test cases and examples to verify that the skill is working correctly.

## ✅ Pre-Flight Checklist

Before testing, verify:

- [ ] All 11 skill directories exist under `skills/`
- [ ] Each skill has a `SKILL.md` file
- [ ] `shared/prompts_index.json` exists and is valid JSON
- [ ] `shared/role_mapping.json` exists and is valid JSON
- [ ] Skill is installed in Claude Code plugins directory

## 🧪 Test Scenarios

### Test 1: Main Entry Point - Smart Mode (English)

**Input:**
```
Help me write a cold email to the CEO of Acme Corp about our SaaS product
```

**Expected Behavior:**
1. Detects Sales role
2. Detects English language
3. Recommends "Draft a personalized cold outreach email"
4. Asks for: company name, product value props
5. Generates email after receiving input

**Pass Criteria:**
- ✅ Role detection: Sales
- ✅ Language: English response
- ✅ Recommended prompt matches task
- ✅ Parameter collection works

---

### Test 2: Smart Mode (Chinese)

**Input:**
```
帮我分析客户反馈，找出主要问题
```

**Expected Behavior:**
1. 检测到Product或Customer Success角色
2. 检测到中文语言
3. 用中文引导
4. Recommends appropriate prompt (英文标题)
5. 用中文询问参数

**Pass Criteria:**
- ✅ 角色检测：Product或CS
- ✅ 语言：中文引导
- ✅ Prompt推荐准确
- ✅ 参数询问使用中文

---

### Test 3: Browse Mode

**Input:**
```
Show me all sales prompts
```

**Expected Behavior:**
1. Enters Browse Mode
2. Lists Sales categories:
   - Outreach & communication (5 prompts)
   - Sales strategy & planning (5 prompts)
   - Competitive intelligence (5 prompts)
   - Data analysis (5 prompts)
3. Shows prompt titles for each category

**Pass Criteria:**
- ✅ Lists all Sales categories
- ✅ Shows correct prompt count per category
- ✅ All prompts are Sales-related

---

### Test 4: Direct Mode

**Input:**
```
Use "Analyze product feedback themes"
```

**Expected Behavior:**
1. Directly loads specified prompt
2. Shows prompt template
3. Asks for required parameter: customer feedback data
4. Ready to execute after receiving data

**Pass Criteria:**
- ✅ Loads exact prompt by name
- ✅ Shows full prompt template
- ✅ Identifies required parameters
- ✅ Executes successfully

---

### Test 5: Role Detection - Product Manager

**Input:**
```
I'm a product manager and need to write a PRD for a new feature
```

**Expected Behavior:**
1. Explicit role detection: Product
2. Task detection: PRD creation
3. Recommends "Draft PRD for a new feature"
4. Asks for feature context, customer needs

**Pass Criteria:**
- ✅ Detects "product manager"
- ✅ Matches to Product role
- ✅ Recommends PRD-specific prompt
- ✅ Guidance in English

---

### Test 6: Role Detection - HR

**Input:**
```
I need to write a job description for a software engineer
```

**Expected Behavior:**
1. Keyword detection: "job description", "software engineer"
2. Role detection: HR (recruiting context)
3. Recommends "Write a job description draft"
4. Asks for job responsibilities, skills, team context

**Pass Criteria:**
- ✅ Detects HR role from keywords
- ✅ Recommends correct prompt
- ✅ Parameters match HR context

---

### Test 7: Language Switching

**Input:**
```
帮我写冷邮件
```

Then immediately:

**Input:**
```
Now help me in English - analyze this customer feedback
```

**Expected Behavior:**
1. First input: Chinese response
2. Second input: Switches to English
3. Adaptive language detection works

**Pass Criteria:**
- ✅ First response in 中文
- ✅ Second response in English
- ✅ No language confusion

---

### Test 8: Multi-Role Scenario

**Input:**
```
Create an onboarding plan for new sales hires
```

**Expected Behavior:**
1. Detects overlap: Sales + HR
2. May recommend prompts from both roles
3. Clarifies with user if needed

**Pass Criteria:**
- ✅ Recognizes multi-role context
- ✅ Provides relevant prompts
- ✅ Clarifies ambiguity if present

---

### Test 9: Error Handling - No Match

**Input:**
```
Help me with something completely unrelated like cooking recipes
```

**Expected Behavior:**
1. No matching prompts found
2. Graceful fallback message
3. Suggests browsing available roles
4. Offers to switch to general conversation

**Pass Criteria:**
- ✅ No crash or error
- ✅ Helpful fallback message
- ✅ Alternative suggestions provided

---

### Test 10: Parameter Extraction

**Input:**
```
Write a cold email to the CTO of TechCorp about our AI-powered customer service platform that reduces response time by 50%
```

**Expected Behavior:**
1. Detects Sales scenario
2. Extracts parameters from input:
   - Job title: CTO
   - Company: TechCorp
   - Value props: AI-powered customer service, 50% faster response
3. Pre-fills prompt with extracted info
4. Generates email with minimal additional questions

**Pass Criteria:**
- ✅ Extracts all 3 parameters correctly
- ✅ Pre-fills prompt template
- ✅ Generates complete email
- ✅ Minimal back-and-forth

---

## 🔍 Debug Mode

To enable detailed logging of role detection, language detection, and prompt matching:

Add to user input:
```
[debug mode] Help me write a cold email
```

Expected output:
```
[DEBUG] Language detected: English
[DEBUG] Keywords extracted: ['help', 'write', 'cold', 'email']
[DEBUG] Role detection: Sales (confidence: 85%)
[DEBUG] Prompt matching:
  - "Draft a personalized cold outreach email": score 22
  - "Rework demo follow-up email": score 12
[DEBUG] Top match: Draft a personalized cold outreach email
```

---

## 📊 Performance Benchmarks

### Expected Response Times

| Operation | Target | Max |
|-----------|--------|-----|
| Load skill | < 1s | 2s |
| Detect language | < 0.5s | 1s |
| Detect role | < 1s | 2s |
| Match prompts | < 1s | 2s |
| Generate response | < 3s | 5s |

### Load Testing

- Test with 10 consecutive queries
- Monitor memory usage
- Check for memory leaks
- Verify consistent performance

---

## 🐛 Common Issues & Fixes

### Issue 1: Skill Not Loading

**Symptom:** Claude doesn't recognize the skill

**Diagnosis:**
```bash
# Check if files exist
ls ~/.claude/plugins/custom/naiba-openai-work-assistant/skills/*/

# Verify SKILL.md format
head -5 ~/.claude/plugins/custom/naiba-openai-work-assistant/skills/naiba-openai-work-assistant/SKILL.md
```

**Fix:**
- Ensure `SKILL.md` has proper frontmatter
- Check file permissions
- Restart Claude Code

---

### Issue 2: JSON Parsing Errors

**Symptom:** "Error loading prompts index"

**Diagnosis:**
```bash
# Validate JSON
python3 -m json.tool ~/.claude/plugins/custom/naiba-openai-work-assistant/shared/prompts_index.json
```

**Fix:**
- Re-run conversion script
- Check for malformed JSON
- Verify file encoding is UTF-8

---

### Issue 3: Wrong Language Response

**Symptom:** Chinese input gets English response or vice versa

**Diagnosis:**
- Check language detection rules in `shared/utils.md`
- Verify character counting logic

**Fix:**
- Adjust language detection threshold
- Update keyword lists for better detection

---

### Issue 4: Poor Prompt Recommendations

**Symptom:** Recommended prompts don't match user intent

**Diagnosis:**
- Review prompt matching algorithm
- Check keyword extraction
- Verify scoring weights

**Fix:**
- Adjust scoring weights in `shared/utils.md`
- Add more aliases to `role_mapping.json`
- Improve prompt titles/descriptions

---

## ✅ Test Results Template

Use this template to document your test results:

```markdown
## Test Results - [Date]

### Environment
- Claude Code Version: [version]
- OS: [operating system]
- Skill Version: 1.0.0

### Test Cases
| Test | Pass/Fail | Notes |
|------|-----------|-------|
| Test 1 - Smart Mode English | ⬜ | |
| Test 2 - Smart Mode Chinese | ⬜ | |
| Test 3 - Browse Mode | ⬜ | |
| Test 4 - Direct Mode | ⬜ | |
| Test 5 - Role Detection PM | ⬜ | |
| Test 6 - Role Detection HR | ⬜ | |
| Test 7 - Language Switching | ⬜ | |
| Test 8 - Multi-Role Scenario | ⬜ | |
| Test 9 - Error Handling | ⬜ | |
| Test 10 - Parameter Extraction | ⬜ | |

### Performance
- Average load time: [ ]s
- Average response time: [ ]s
- Memory usage: [ ]MB

### Issues Found
1. [Description]

### Overall Status
⬜ Pass (10/10)
⬜ Pass with minor issues (8-9/10)
⬜ Needs work (6-7/10)
⬜ Failing (0-5/10)
```

---

## 🚀 Next Steps After Testing

1. **If all tests pass:**
   - Document any edge cases
   - Create user guide
   - Prepare for release

2. **If issues found:**
   - Prioritize by severity
   - Fix in order: Critical → Major → Minor
   - Re-test after each fix

3. **Performance optimization:**
   - Profile slow operations
   - Cache frequently accessed data
   - Optimize search algorithms

---

**Happy Testing! 🎯**

Remember: The goal is a seamless, intelligent experience where users forget they're using a "skill" - it should just feel like having a helpful AI assistant.
