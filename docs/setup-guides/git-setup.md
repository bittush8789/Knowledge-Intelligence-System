# Git Setup

## Purpose
Version control for tracking changes in source code.

## Why chosen for this project
Standard version control for collaborative development and GitOps workflows.

## Install
- **Windows**: Download and install from [git-scm.com](https://git-scm.com/).
- **Linux**: `sudo apt update && sudo apt install git -y`
- **Mac**: `brew install git`

## Start service commands
N/A (CLI tool)

## Configure commands
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Verify commands
```bash
git --version
```

## Example usage
```bash
git status
git add .
git commit -m "feat: initial commit"
git push origin main
```

## Best practices
- Use descriptive commit messages.
- Commit early and often.
- Never push secrets to the repository.
