# YET ANOTHER DATASCIENCE COOKIECUTTER TEMPLATE

This is a modern Cookiecutter template that can be used to initiate a Python Data Science project with all the necessary tools for development, testing, and deployment. It supports the following features:

- [Poetry](https://python-poetry.org/) for dependency management
- CI/CD with GitHub Actions
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [Black](https://black.readthedocs.io/en/stable/index.html), [flake8](https://flake8.pycqa.org/en/latest/#), [isort](https://pycqa.github.io/isort/), [mypy](https://mypy.readthedocs.io/en/stable/),  and [pylint](https://pylint.readthedocs.io/en/stable/)
- A repository creation in GitHub if agreed by the user using [GitHub CLI](https://cli.github.com)
- Testing and coverage with [pytest](https://docs.pytest.org/en/8.3.x/) and [codecov](https://about.codecov.io/)
- Compatibility testing for multiple versions of Python with [Tox](https://tox.wiki/en/latest/)

---

## Quickstart

On your local machine, install `cookiecutter` and directly pass the URL to this
Github repository to the `cookiecutter` command:

```bash
pip install cookiecutter
cookiecutter https://github.com/fpgmaas/cookiecutter-poetry.git
```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

## Acknowledgements

This project is partially based on:
- [Audrey Feldroy](https://github.com/audreyfeldroy)\'s great [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) repository
- The [cookiecutter-datascience](https://github.com/drivendataorg/cookiecutter-data-science) repository
- [Florian Maas](https://github.com/fpgmaas)'s [cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry) repository
