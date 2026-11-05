from one_time_callers import one_time_callers
import pytest

@pytest.mark.parametrize("callers, expected", [
(["amy", "bob", "amy", "cat"], ["bob", "cat"]),
(["cat", "amy", "bob", "amy"], ["cat", "bob"]),
(["amy", "amy", "bob", "bob"], []),
(["amy"], ["amy"]),
([], []),
])
def test_one_time_caller(callers, expected):
    assert one_time_callers(callers) == expected