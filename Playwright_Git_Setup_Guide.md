# Playwright Testing Project: Setup and GitHub Guide

## Overview

This guide organises the commands used to set up a Python test environment with pytest and Playwright, and to publish the project to GitHub. The work happens in three stages: create an isolated Python environment and install the test tools, upload the first version of the project to GitHub, then add a second commit and push it.

## Part 1: Python Environment and Test Tools

This part creates a virtual environment so the project's packages stay separate from the rest of the system, then installs pytest, the Playwright plugin, and a plugin for rerunning flaky tests.

| No. | Command | What it does |
|-----|---------|--------------|
| 1 | `python -m venv .venv` | Creates a virtual environment named .venv in the project folder. |
| 2 | `.venv\Scripts\Activate.ps1` | Activates the environment in PowerShell. Commands now use this environment's Python. Note the single dot before venv. |
| 3 | `python -m pip install pytest pytest-playwright` | Installs the pytest test runner and the plugin that connects it to Playwright browser automation. |
| 4 | `python -m playwright install` | Downloads the browser binaries (Chromium, Firefox, WebKit) that Playwright drives. |
| 5 | `pytest --version` | Checks that pytest is installed and prints its version. |
| 6 | `python -m pip install pytest-rerunfailures` | Installs a plugin that reruns failed tests, useful for intermittent failures. |
| 7 | `python -m pip freeze > requirements.txt` | Writes every installed package and version to requirements.txt so others can recreate the environment. |

## Part 2: GitHub Repository with README

This part turns the project folder into a Git repository and connects it to the GitHub repository, which already contains a README. Because the local and GitHub histories were created separately, Git needs the `--allow-unrelated-histories` flag when pulling.

| No. | Command | What it does |
|-----|---------|--------------|
| 1 | `git init` | Creates a local Git repository in the current folder. |
| 2 | `git status` | Lists files that are new, modified, or staged. Use it to check before and after each step. |
| 3 | `git add .` | Stages every file in the folder (the . means current folder) for the next commit. |
| 4 | `git commit -m "Initial commit"` | Saves the staged files as a snapshot with a descriptive message. |
| 5 | `git branch -M main` | Renames the current branch to main, the default branch name on GitHub. |
| 6 | `git remote add origin <URL>` | Links the local repository to the GitHub repository under the name origin. |
| 7 | `git remote -v` | Shows the linked URLs to confirm the connection is correct. |
| 8 | `git pull origin main --allow-unrelated-histories` | Downloads the README from GitHub and merges it with the local history. Opens a text editor for the merge message. |

**Closing the merge editor (Vim):**

1. Press `Esc` to leave insert mode.
2. Type `:wq` (write and quit).
3. Press `Enter`. The default merge message is saved and the merge completes.

## Part 3: Empty GitHub Repository

This part saves the merged project and uploads it to GitHub. The corrected commands are shown in the table below; the notes that follow explain the differences from the original list.

| No. | Command | What it does |
|-----|---------|--------------|
| 1 | `git init` | Safe to run again. It reports that the repository already exists and changes nothing. |
| 2 | `git status` | Confirms which files are new or changed since the last commit. |
| 3 | `git add .` | Stages all changes. |
| 4 | `git commit -m "Initialised"` | Saves the changes with a message. Consider "Initialized" for US spelling. |
| 5 | `git branch -M main` | Corrected from `git commit -M main`. Ensures the branch is named main. |
| 6 | `git remote add origin <URL>` | Only needed if the remote was not added in Part 2. Otherwise Git reports that origin already exists. |
| 7 | `git remote -v` | Confirms the remote URL. |
| 8 | `git push -u origin main` | Uploads the commits to GitHub's main branch. The `-u` flag links the local branch to the remote so later pushes can use `git push` alone. |

## Corrections to the Original Notes

Several lines in the original notes would fail as written. The corrected versions are used in this guide.

- **Activation path:** `..venv\Scripts\Activate.ps1` has an extra dot. The correct path is `.venv\Scripts\Activate.ps1`.
- **Branch rename:** `git commit -M main` is not a valid command. The correct command is `git branch -M main`.
- **Remote URL:** replace the `<URL>` placeholder with your repository's HTTPS address from GitHub. The repository address is listed in the Repository section at the end of this guide.
- **Repeated remote setup:** `git remote add origin` fails if the remote already exists. Use `git remote set-url origin <URL>` to change an existing remote.

## Quick Reference: Git Workflow

For day-to-day work after setup, the cycle is: edit files, run `git status` to review changes, run `git add .` to stage them, run `git commit -m "message"` to save them, and run `git push` to upload them to GitHub. Running `git pull` before starting work pulls any changes made on GitHub into the local copy.

## Repository

GitHub repository: https://github.com/VikasPaspula/Playwright_Testing

Remote URL for `git remote add origin`: https://github.com/VikasPaspula/Playwright_Testing.git
