import time
from functools import partial

import pytest
from _pytest.terminal import TerminalReporter

__all__ = ["pytest_terminal_summary"]


def _custom_short_summary(terminalreporter: TerminalReporter):
    """Create a custom short summary for the test report."""
    stats = terminalreporter.stats
    total_count = sum(len(value) for value in stats.values())
    deselected_cases = stats.get("deselected", [])
    failed_cases = stats.get("failed", [])
    passed_cases = stats.get("passed", [])
    total_duration = time.time() - terminalreporter._sessionstarttime

    failed = bool(failed_cases)

    write_sep = terminalreporter.write_sep
    write = terminalreporter.write

    write_sep("=", "Test Report Summary", red=failed, green=(not failed), bold=True)

    write(f"Total Test Duration: {total_duration:.2f} seconds", bold=True)
    write(f"\nTotal Tests Collected: {total_count}", bold=True)
    write(f"\nDeselected Tests: {len(deselected_cases)}", bold=True)
    write(f"\nPassed Count: {len(passed_cases)}", bold=True)
    write(f"\nFailed Count: {len(failed_cases)}", bold=True)
    write("\n")

    for failed_test in failed_cases:
        write(f"\tFailed test: {failed_test.nodeid}\n", yellow=True)

    write_sep(
        "=", "End of Test Report Summary", red=failed, green=(not failed), bold=True
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter: TerminalReporter):
    """Pytest hook implementation to add custom short summary to the report."""
    yield
    terminalreporter.short_test_summary = partial(
        _custom_short_summary, terminalreporter
    )
