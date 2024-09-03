# MIT License
#
# Copyright (c) 2024, Cédrick-Armel Yebouet
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# flake8: noqa
# pylint: disable=all
# mypy: disable-error-code="import-untyped"

import json
import logging
import re
import subprocess
import sys

from cookiecutter.generate import generate_context

from yaccp.utils import get_logger

logger = get_logger(__name__)
logger.setLevel(logging.ERROR)


def is_git_installed() -> bool:
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        return True
    except Exception as e:
        return False


def is_gh_installed() -> bool:
    try:
        subprocess.run(["gh", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


def is_python_installed() -> bool:
    try:
        subprocess.run(["python", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


def is_poetry_installed() -> bool:
    try:
        subprocess.run(["poetry", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    pre_context = {
        "git_init": "y",
        "python_path": "y",
        "repo_vis": "y",
        "create_repo": "y",
        "manage_env": "y",
    }
    initial = generate_context()
    update = {}
    if is_git_installed():
        username = subprocess.run(
            ["git", "config", "--global", "user.name"], capture_output=True, check=True
        ).stdout.decode()
        email = subprocess.run(
            ["git", "config", "--global", "user.email"], capture_output=True, check=True
        ).stdout.decode()
        username, email = re.sub("\n", "", username), re.sub("\n", "", email)
        if username != "":
            initial["cookiecutter"].update(dict(author=username))
        if email != "":
            initial["cookiecutter"].update({"email": email})

        if not is_gh_installed():
            pre_context["create_repo"] = "n"
            pre_context["repo_vis"] = "n"

    else:
        pre_context["git_init"] = "n"
        pre_context["create_repo"] = "n"
        pre_context["repo_vis"] = "n"

    if is_poetry_installed() and is_python_installed():
        python_path = subprocess.run(
            ["which", "python"], capture_output=True, check=True
        ).stdout.decode()
        initial["cookiecutter"]["python_path"] = re.sub("\n", "", python_path)

    else:
        if not is_python_installed():
            logger.error("Python is not installed on your device. Stopping...")
            sys.exit(1)
        if not is_poetry_installed():
            logger.error("Python is not installed on your device. Stopping...")
            sys.exit(1)

    for key, value in pre_context.items():
        if value == "n":
            update[key] = value
            initial["cookiecutter"]["__" + key] = value

    for key in update.keys():
        initial["cookiecutter"] = initial["cookiecutter"].pop(key)

    with open("cookiecutter.json", "w") as f:
        json.dump(initial["cookiecutter"], f, indent=4)
