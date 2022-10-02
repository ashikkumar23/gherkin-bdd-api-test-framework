import time
from functools import partial

import pytest
from _pytest.terminal import TerminalReporter

__all__ = ["pytest_terminal_summary"]


def _custom_short_summary(terminalreporter: TerminalReporter):
    """
    Args:
        terminalreporter: Instance of _pytest.terminal.TerminalReporter class

    Function:
        Modifies pytest report summary in the format:
        ```
            Total Test Duration: <total_duration> seconds
            Total Tests Collected: <total_count>
            Deselected Tests: <deselected_cases_count>
            Passed Count: <passed_cases_count>
            Failed Count: <failed_cases_count>
                <new-line-separated list of failing test cases>
        ```

    """
    total_count = sum(len(v) for k, v in terminalreporter.stats.items() if k)
    deselected_cases = terminalreporter.stats.get("deselected", [])
    failed_cases = terminalreporter.stats.get("failed", [])
    passed_cases = terminalreporter.stats.get("passed", [])
    total_duration = time.time() - terminalreporter._sessionstarttime

    terminalreporter.write_sep(
        "=",
        "Report Summary",
        red=bool(failed_cases),
        green=(not bool(failed_cases)),
        bold=True,
    )

    terminalreporter.write(f"Total Test Duration: {total_duration:.2f} seconds", bold=True)
    terminalreporter.write("\n")

    terminalreporter.write(f"Total Tests Collected: {total_count}", bold=True)
    terminalreporter.write("\n")

    terminalreporter.write(f"Deselected Tests: {len(deselected_cases)}", bold=True)
    terminalreporter.write("\n")

    terminalreporter.write(f"Passed Count: {len(passed_cases)}", bold=True)
    terminalreporter.write("\n")

    terminalreporter.write(f"Failed Count: {len(failed_cases)}", bold=True)
    terminalreporter.write("\n")

    for failed in failed_cases:
        terminalreporter.write("\t")
        terminalreporter.write(failed.nodeid, yellow=True)
        terminalreporter.write("\n")

    terminalreporter.write_sep(
        "=",
        "End of Report Summary",
        red=bool(failed_cases),
        green=(not bool(failed_cases)),
        bold=True,
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter: TerminalReporter):
    """
    Args:
        terminalreporter: Instance of _pytest.terminal.TerminalReporter

    Implementation:
        Create a `custom_short_summary` method, and short circuit to the terminal reporter's
        `short_test_summary` method.
    """
    yield
    # for details on `partial` implementation, please read
    # https://docs.python.org/3/library/functools.html#functools.partial
    custom_short_summary = partial(_custom_short_summary, terminalreporter)

    terminalreporter.short_test_summary = custom_short_summary
