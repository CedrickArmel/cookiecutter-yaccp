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
# mypy: disable-error-code="import-untyped,name-defined"

import logging
import subprocess

from .utils import get_logger

logger = get_logger(__name__)
logger.setLevel(logging.ERROR)


def setup_poetry_env() -> bool:
    if ("{{cookiecutter.__manage_env}}" == "Poetry") and ("{{cookiecutter.__python_path}}" != ""):  # type: ignore[comparison-overlap]
        try:
            subprocess.run(
                ["poetry", "env", "use", "{{ cookiecutter.__python_path }}"],
                capture_output=True,
                check=True,
            )
            subprocess.run(
                ["poetry", "update", "--sync"],
                capture_output=True,
                check=True,
            )
            return True
        except Exception as e:
            logger.warning("%s", str(e))
            return False
    else:
        return True


def git_init() -> bool:
    if {{cookiecutter.__git_init}}:
        try:
            subprocess.run(["git", "init"])
            return True
        except Exception as e:
            logger.warning("%s", str(e))
            return False
    else:
        return True


def create_repo() -> bool:
    if {{cookiecutter.__create_repo}} and {{cookiecutter.__git_init}}:
        try:
            subprocess.run(
                [
                    "gh",
                    "repo",
                    "create",
                    "{{ cookiecutter.repo_name }}",
                    "-s",
                    ".",
                    "--" + "{{ cookiecutter.__repo_vis }}",
                ],
                capture_output=True,
                check=True,
            )
            return True
        except Exception as e:
            logger.warning("%s", str(e))
            return False
    else:
        return True


if __name__ == "__main__":
    setup_poetry_env()
    git_init()
    create_repo()
