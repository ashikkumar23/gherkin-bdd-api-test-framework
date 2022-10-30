# pylint: disable=invalid-name
# pylint: disable=protected-access
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import

from collections import defaultdict

from cucumber_tag_expressions import parse

from step_definitions.test_common import *
from step_definitions.test_assertions import *

from lib.terminal_report import pytest_terminal_summary


def pytest_configure(config):
    config.option.keyword = "automated"
    config.option.markexpr = "not not_in_scope"
    pytest.globalDict = defaultdict()


def pytest_addoption(parser):
    parser.addoption("--tags", metavar="str", help="Will filter tests by given tags")


def pytest_collection_modifyitems(config, items):
    raw_tags = config.option.tags
    if raw_tags is not None:
        for item in items:
            item_tags = [marker.name for marker in item.own_markers]
            if not parse(raw_tags).evaluate(item_tags):
                item.add_marker(pytest.mark.not_in_scope)
