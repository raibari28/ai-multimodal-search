## 🔐 Environment Setup & Security

This project uses the OpenAI API and other integrations that require secrets (like API keys). To ensure security and prevent accidental exposure, follow these guidelines:

---

### 📁 `.env` File (Never Commit This)

Your real secrets should live in a `.env` file located at the root of the project:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

This file **must not** be committed to GitHub. It is listed in `.gitignore` to prevent accidental uploads.

---

### 🧪 `.env.example` (Safe Template)

A safe `.env.example` file is provided. It contains the structure but no secrets:

```
OPENAI_API_KEY=your-api-key-here
```

Share this file with your team so they know what variables they need to set locally.

---

### 🤖 GitHub Actions: Secret Scanner

This repo includes a GitHub Actions workflow that uses [`detect-secrets`](https://github.com/Yelp/detect-secrets) to prevent accidental commits of secrets.

It runs automatically on:
- Every push to `main`
- Every pull request

If any secret patterns are detected, GitHub will block the merge and warn the developer.

---

### ✅ Summary

| File             | Purpose                          | Committed to GitHub? |
|------------------|----------------------------------|----------------------|
| `.env`           | Your real API keys (keep private)| ❌ **NO**            |
| `.env.example`   | Safe config template             | ✅ **YES**           |
| `.gitignore`     | Prevents secrets/garbage in repo | ✅ **YES**           |
| `.github/workflows/secret-scan.yml` | Secret scan automation         | ✅ **YES**           |

For any new developer:  
> Copy `.env.example` → `.env` and add your actual API key.

Stay secure, commit smart. 🔐✨
