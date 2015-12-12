#!/usr/bin/env bash
IFS=$'\n\t'; echo
set -xeuo pipefail

# Make a git repository for the project and make the initial commit.

git init
git add .
git commit -m "Initial commit."

# Create a virtual environment and install the game in it.

virtualenv -p python3 --system-site-packages env
env/bin/pip install -e .


