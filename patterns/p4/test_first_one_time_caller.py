from first_one_time_caller import first_one_time_caller
import pytest

@pytest.mark.parametrize("callers, expected", [
(["amy", "bob", "amy", "cat"], "bob"),          # "bob"
(["amy", "amy", "bob", "cat", "bob"], "cat"),   # "cat"
(["amy", "bob", "amy", "bob"], None),          # None
(["amy"], "amy"),                               # "amy"
([], None)                                    # None
])
def test_one_time_caller(callers, expected):
    assert first_one_time_caller(callers) == expected