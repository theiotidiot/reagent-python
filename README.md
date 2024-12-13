# reagent-python
Python wrapper for the Reagent Analytics API.

## Installing

Installing from GitHub is possible (public repository only):

```
pip install git+https://github.com/ReagentAnalytics/reagent-python
```

Installing locally:

```
pip install .
```

or from the build

```
pip install reagentpy-<version>-py3-none-any.whl
```

## Developing with `poetry`

**Installing**

You can install the dev build with [`poetry`](https://python-poetry.org/) by navigating to the root of this repo and running the following:

```
poetry install --with dev
```

**Testing**

Run a test with `pytest`:

```
poetry run python -m pytest tests/reagent-client-class.py
```

**Building**

New builds are determined by the version number dictated in `pyproject.toml`.

Build a new version with:

```
poetry build
```

