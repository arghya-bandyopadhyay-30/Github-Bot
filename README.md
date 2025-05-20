# 🕓 Automated Historical Commit Project

This project simulates a realistic Git commit history by generating backdated commits with randomized timestamps. It's ideal for developers who want to enhance the visual contribution graph, demo workflows, or experiment with Git automation.

---

## 🚀 Features

* ✅ **Randomized Historical Commits**
  Generates a series of Git commits on random dates between a given start date and today.

* 🕰️ **Custom Commit Timestamps**
  Each commit uses a custom `author_date` and `commit_date` to appear historically accurate.

* 🔄 **Push to Remote**
  Automatically commits and pushes to the `main` branch.

* 🛡️ **Safe and Controlled**
  Clean error handling and optional customization of start date.

---

## 📆 Setup

### ✅ Prerequisites

* Python 3.7+
* Git installed and configured
* [`GitPython`](https://gitpython.readthedocs.io/) library

### 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/arghya-bandyopadhyay-30/github-bot.git
   cd github-bot
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Usage

To generate and push commits:

```bash
python src/main.py
```
By default, this generates random commits starting from **January 1, 2025**.

You can also specify a custom start date for commit generation:

```bash
python src/main.py --start-date 2025-01-01
```

This will:

* Generate N random dates between `--start-date` and today.
* Create a commit for each with a custom timestamp.
* Push all commits to the remote `main` branch.

---

## 📝 Configuration

| Parameter      | Description                                            | Default      |
| -------------- | ------------------------------------------------------ | ------------ |
| `--start-date` | (Optional) ISO format date to begin historical commits | `2025-1-04` |

> **Note:** All commits are made to the branch `main`. Ensure your repo uses this as the default or adjust accordingly.

---

## 🔐 Authentication

* For private repositories, ensure you're authenticated using:

  * SSH (recommended)
  * GitHub CLI (`gh auth login`)
  * Git Credential Helper

Avoid using raw tokens or embedding secrets in URLs.

---

## 💡 Example Use Cases

* 🧪 **Git Practice**: Simulate version control workflows.
* 🎓 **Learning**: Understand Git commit internals like `author_date`.
* 📊 **Demo Repos**: Enhance the GitHub contribution graph for presentation.
* 🛠️ **Dev Tooling**: Test CI/CD behavior against backdated commits.

---

## ⚠️ Warnings

* **Avoid Abuse**: Do not use this to falsify contributions for unethical purposes.
* **Use With Caution**: This tool rewrites commit timestamps and could alter commit history if misused.

---

## 👥 Contributing

Contributions are welcome!
To propose improvements:

* Open an [Issue](https://github.com/arghya-bandyopadhyay-30/github-bot/issues)
* Submit a Pull Request

---

## 📄 License

MIT License.
See [LICENSE](LICENSE) for details.

---

## 📬 Contact

For support or questions, raise an issue on GitHub.

---
