# Python Setup Guide

## 1. What Python does
Python is a high-level programming language that is easy to read and write. It is the core language for our AI and Backend logic.

## 2. Why used in this project
We use Python because it has amazing libraries for AI (LangChain, OpenAI) and Web development (FastAPI/Flask).

## 3. Install Steps

### Windows:
1. Download from [python.org](https://www.python.org/downloads/).
2. **IMPORTANT**: Check the box that says "Add Python to PATH" during installation.

### Linux (Ubuntu):
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip -y
```

### Mac:
```bash
brew install python@3.11
```

## 4. Verify Install
Open your terminal/command prompt and type:
```bash
python --version
```
It should show `Python 3.11.x`.

## 5. Basic Commands
- `python main.py`: Runs a python script.
- `pip install <package>`: Installs a library.
- `python -m venv venv`: Creates a virtual environment.

## 6. Common Errors
**Error**: `'python' is not recognized as an internal or external command.`
**Reason**: Python was not added to your system's PATH.

## 7. Fix Steps
Re-run the installer and select "Modify" then ensure "Add to PATH" is checked. Or add it manually in Environment Variables.

## 8. Best Practices
- Always use a virtual environment for each project.
- Use a `requirements.txt` file to manage your libraries.
