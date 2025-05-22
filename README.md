# RAG System

This repository contains the code and resources for building a Retrieval-Augmented Generation (RAG) system from scratch.

## Requirements 

- Python 3.8 or higher version

## Installation

## 1. **Create and activate a virtual environment**

```bash
python -m venv .venv

# Activate the environment (Windows)
.venv\Scripts\activate

# Or on macOS/Linux:
# source .venv/bin/activate

```
## 2. Install required packages
```bash
pip install -r requirements.txt
```

# Environment Variables
This project uses environment variables to manage sensitive keys securely (like API keys, secrets, etc.).

- How to use them:

    1- Create a file named .env in the root directory of the project.

    2- Add your secret environment variables inside this file.

- You can duplicate it and rename to .env:
```bash
cp .env.example .env
```

## Notes
Always make sure to activate the virtual environment before running your code.

Use the ".env.example" to guide team members or collaborators on what environment variables are needed.





