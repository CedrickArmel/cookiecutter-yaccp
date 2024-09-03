# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Installation for developpement

To install this project you need these dependencies installed:

- Python `{{ cookiecutter.python_version }}`
- [Poetry](https://python-poetry.org/docs/)

### Clone the project

```sh
git clone <repository>
```

### Install the dependencies

```sh
poetry shell && poetry instal
```

## Project Organization

```md

├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for
│                         {{ cookiecutter.package_name }} and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── poetry.lock   <- resolves and locks all dependencies and their sub-dependencies in the pyproject.toml file.
│
│
└── {{ cookiecutter.package_name }}   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes {{ cookiecutter.package_name }} a Python module
```

--------
