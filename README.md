# **bdd-gherkin-api-test-automation-demo**


## Description:

Automated CRUD ( i.e., `POST`, `GET`, `UPDATE`, `DELETE` ) operations using `pytest` and `pytest-bdd`


## Prerequisites:

`requests` `pytest` `pytest-bdd`


## Installation Steps:

In order to get the tests to run locally, you need to install the following pieces of software.

###### NOTE: All commands shall be executed from Automation Project root directory: `../[PROJECT_DIR]/tests/`

#### MacOS

- Install Homebrew with `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
    - Fix commandline `sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /`
- Install Pyenv with `brew install pyenv`, This is a python version manager.
- Add the following to `~/.bash_profile`
```.env
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PATH="$PYENV_ROOT/shims:$PATH"
export PATH="$PYENV_ROOT/completions/pyenv.bash:$PATH"
```
- Install python 3.8.2 with `pyenv install 3.8.2`
- Set python version 3.8.2 to be used globally with `pyenv global 3.8.2`
- Install virtualenv with `python3 -m pip install --user virtualenv`
- Create new virtual env with `python3 -m virtualenv .venv`
- Activate new virtual env with `source ./.venv/bin/activate`
- Install all project dependencies with `pip install -r requirements.txt`
- Check python version used with `which python`, Shall be `[PROJECT_DIR]/tests/.venv/bin/python`.

#### Windows / Linux

- Install GitBash
- Uninstall any previous python version
- Install python 3.8.2 using official installation file
- Install all project dependencies with `pip install -r requirements.txt`


## Project Contents:

`tests/` directory contains `features/` and `step_definitions/` sub-directories.

`features/sample.feature` file contains BDD Scenarios ( i.e., BDD statements )

`step_definitions/test_sample.py` file contains corresponding step implementation of `sample.feature` file for each of the BDD statements.


## Test Execution:

- Fork the repo `bdd-gherkin-api-test-automation-demo`
- Clone the repo to your local
- Open Pycharm (or any IDE) > File > Open > Open the project where the repository is located ( i.e., `../bdd-gherkin-test-automation-demo/tests`)
- Run the command: `pytest -vv --gherkin-terminal-reporter --reruns 1 --reruns-delay 1 --tags="automated"`


## Pycharm Edit Configuration:

- Go to `Edit Configurations...`
- Add `New Configuration` ( `+` sign ) > `Python tests` > `pytest`
- Provide `Script path` and `Working directory`
- Select required `Python interpreter`
- And, `Additional Arguments`: `-vv --gherkin-terminal-reporter --reruns 1 --reruns-delay 1 --tags="automated"`


## Output:

`Sample Test Result`:

====================== test session starts ========================

platform darwin -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1 -- /Volumes/My_Volume/NewPage/Monday-KT/Ashik/BDD-Gherkin/bdd-gherkin-api-test-automation-demo/tests/.venv/bin/python

cachedir: .pytest_cache

rootdir: /Volumes/My_Volume/NewPage/Monday-KT/Ashik/BDD-Gherkin/bdd-gherkin-api-test-automation-demo/tests, inifile: pytest.ini

plugins: rerunfailures-9.0, bdd-3.4.0

collected 7 items / 2 deselected / 5 selected                                                                                                                                 

`Feature: Test CRUD methods in Sample REST API Testing Framework`

    Scenario: POST example
        Given I set sample REST API URL
        And I set header param request content type as "application/json"
        Given I set "POST" posts api endpoint
        When I send "POST" HTTP request with <payload>
        Then I receive valid HTTP response code "201" for "POST"
        And I expect response body "POST" is non-empty
    PASSED

`Feature: Test CRUD methods in Sample REST API Testing Framework`

    Scenario: POST example
        Given I set sample REST API URL
        And I set header param request content type as "application/json"
        Given I set "POST" posts api endpoint
        When I send "POST" HTTP request with <payload>
        Then I receive valid HTTP response code "201" for "POST"
        And I expect response body "POST" is non-empty
    PASSED

`Feature: Test CRUD methods in Sample REST API Testing Framework`

    Scenario: GET example
        Given I set sample REST API URL
        And I set header param request content type as "application/json"
        Given I set "GET" posts api endpoint
        When I send "GET" HTTP request
        Then I receive valid HTTP response code "200" for "GET"
        And I expect response body "GET" is non-empty
    PASSED

`Feature: Test CRUD methods in Sample REST API Testing Framework`

    Scenario: DELETE example
        Given I set sample REST API URL
        And I set header param request content type as "application/json"
        Given I set "DELETE" posts api endpoint for "1"
        When I send "DELETE" HTTP request with <payload>
        Then I receive valid HTTP response code "200" for "DELETE"
        And I expect response body "DELETE" is empty
    PASSED

`Feature: Test CRUD methods in Sample REST API Testing Framework`

    Scenario: DELETE example
        Given I set sample REST API URL
        And I set header param request content type as "application/json"
        Given I set "DELETE" posts api endpoint for "1"
        When I send "DELETE" HTTP request with <payload>
        Then I receive valid HTTP response code "200" for "DELETE"
        And I expect response body "DELETE" is empty
    PASSED


============================= warnings summary ==========================

.venv/lib/python3.8/site-packages/pytest_bdd/plugin.py:86

  /Volumes/My_Volume/NewPage/Monday-KT/Ashik/BDD-Gherkin/bdd-gherkin-api-test-automation-demo/tests/.venv/lib/python3.8/site-packages/pytest_bdd/plugin.py:86: PytestUnknownMarkWarning: Unknown pytest.mark.automated - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    
    mark = getattr(pytest.mark, tag)

.venv/lib/python3.8/site-packages/pytest_bdd/plugin.py:86

  /Volumes/My_Volume/NewPage/Monday-KT/Ashik/BDD-Gherkin/bdd-gherkin-api-test-automation-demo/tests/.venv/lib/python3.8/site-packages/pytest_bdd/plugin.py:86: PytestUnknownMarkWarning: Unknown pytest.mark.manual - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    
    mark = getattr(pytest.mark, tag)

-- Docs: https://docs.pytest.org/en/latest/warnings.html

=================== 5 passed, 2 deselected, 2 warnings in 2.66s ====================
