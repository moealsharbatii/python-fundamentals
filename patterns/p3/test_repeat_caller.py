from repeat_caller import repeat_caller
import pytest

@pytest.mark.parametrize("callers, k, expected", [
(["amy", "bob", "amy"], 2, True),                   # True: positions 0 and 2, 2 apart
(["amy", "bob", "amy"], 1, False),                       # False: 2 apart, but k is 1
(["amy", "bob", "cat", "amy", "dan", "amy"], 2, True),  # True: positions 3 and 5
(["amy", "bob", "cat"], 5, False),                       # False: nobody repeats
([], 3, False),                                          # False
])
def test_repeat_caller(callers, k, expected):
    assert repeat_caller(callers, k) == expected