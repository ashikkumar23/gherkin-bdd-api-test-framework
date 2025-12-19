# **API Automation Framework**

[![Actions Status](https://github.com/ashikkumar23/gherkin-bdd-api-test-framework/workflows/Run%20pytest%20and%20upload%20HTML%20report/badge.svg)](https://github.com/ashikkumar23/gherkin-bdd-api-test-framework/actions/workflows/pytest-html-report.yml)

API Automation Framework using `pytest` and `pytest-bdd`

## 🚀 Description:

Automated CRUD (i.e., `POST`, `GET`, `PUT`, `DELETE`) operations using `pytest` and `pytest-bdd`

## 🚀 Prerequisites:

`requests` `pytest` `pytest-bdd`

## 🚀 Installation Steps:

In order to get the tests to run locally, you need to install the following pieces of software.

###### NOTE: All commands shall be executed from Automation Project root directory: `../[PROJECT_DIR]/tests/`

#### MacOS

- Install [Homebrew](https://brew.sh/) with `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- Install [Pyenv](https://formulae.brew.sh/formula/pyenv) with `brew install pyenv`, this is a python version manager.
- Add the following to `~/.bash_profile`

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PATH="$PYENV_ROOT/shims:$PATH"
export PATH="$PYENV_ROOT/completions/pyenv.bash:$PATH"
```

- Install python 3.8.13 with `pyenv install 3.8.13`
- Set python version 3.8.13 to be used globally with `pyenv global 3.8.13`
- Install [virtualenv](https://virtualenv.pypa.io/en/16.7.9/installation.html) with `python3 -m pip install --user virtualenv`
- Create new virtual env with `python3 -m virtualenv .venv`
- Activate new virtual env with `source ./.venv/bin/activate`
- Install all project dependencies with `pip install -r requirements.txt --use-pep517`
- Check the python version used with `which python`, which shall be `[PROJECT_DIR]/tests/.venv/bin/python`.

#### Windows / Linux

- Install [GitBash](https://git-scm.com/downloads)
- Uninstall any previous python version
- Install [python 3.8.13](https://www.python.org/downloads/release/python-3813/) using the official installation file
- Install all project dependencies with `pip install -r requirements.txt --use-pep517`

## 🚀 Project Structure:

```
bdd-gherkin-test-automation-framework/
├─ .github/
│  ├─ workflows/
│  │  ├─ ci.yml
├─ tests/
│  ├─ data/
│  │  ├─ post_payload_1.json
│  │  ├─ post_payload_2.json
│  │  ├─ put_payload_1.json
│  │  ├─ put_payload_2.json
│  ├─ features/
│  │  ├─ sample.feature
│  ├─ lib/
│  │  ├─ terminal_report.py
│  ├─ step_definitions/
│  │  ├─ test_assertions.py
│  │  ├─ test_common.py
│  │  ├─ test_sample.py
│  ├─ utils/
│  │  ├─ __init__.py
│  │  ├─ custom_exceptions.py
│  │  ├─ logger_config.py
│  │  ├─ utils.py
│  ├─ .env
│  ├─ .gitignore
│  ├─ conftest.py
│  ├─ pytest.ini
│  ├─ requirements.txt
├─ LICENSE
├─ README.md
```

## 🚀 Test Execution:

- [Fork](https://github.com/ashikkumar23/gherkin-bdd-api-test-framework/fork) the repository `bdd-gherkin-api-test-automation-framework`
- Clone the repository via HTTPS `git clone https://github.com/<your_github_username>/bdd-gherkin-api-test-automation-framework.git` or via SSH `git clone git@github.com:<your_github_username>/bdd-gherkin-api-test-automation-framework.git`
- Open [Pycharm](https://www.jetbrains.com/pycharm/) (or any IDE) > File > Open > Open the project where the repository is located (i.e., `../bdd-gherkin-test-automation-framework/tests`)
- Run the command: `python -m pytest -v --gherkin-terminal-reporter --reruns 1 --reruns-delay 1 --tags="automated" -s --color="yes"` in `Terminal`

## 🚀 Pycharm Edit Configuration:

- Go to `Edit Configurations...`
- Add `New Configuration` (`+` sign) > `Python tests` > `pytest`
- Provide `Target Script path` and `Working directory` (i.e., `../bdd-gherkin-test-automation-framework/tests`)
- Select the required `Python interpreter`
- And, `Additional Arguments`: `-v --gherkin-terminal-reporter --reruns 1 --reruns-delay 1 --tags="automated" --color="yes"`
