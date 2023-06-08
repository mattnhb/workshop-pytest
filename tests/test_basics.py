import sys

import pytest


def test_will_always_fail():
    assert False, "You can set messages to help debugging!"


@pytest.mark.skip(
    reason="This test cannot be implemented yet, this is a reminder though."
)
def test_will_always_skip():
    ...


@pytest.mark.skipif(
    sys.version_info != (3, 6),
    reason=f"This test requires python3.6, you're using {sys.version_info}",
)
def test_will_fail_if_not_using_py_36():
    ...
