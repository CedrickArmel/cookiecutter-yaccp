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
# mypy: disable-error-code="import-untyped,call-overload"

import logging
import re
import sys

from yaccp.utils import get_logger

logger = get_logger(__name__)
logger.setLevel(logging.ERROR)

MODULE_REGEX = r"^[a-z]+(_[a-z]+)*$"
EMAIL = "{{cookiecutter.email}}"
PACKAGE_NAME = "{{cookiecutter.package_name}}"


def is_valide_package_name() -> bool:
    return True if re.fullmatch(MODULE_REGEX, PACKAGE_NAME) else False


# TODO: is_valide_email()

if __name__ == "__main__":
    if not is_valide_package_name():
        logger.error("Provided Package Name is invalid.")
        sys.exit(1)
