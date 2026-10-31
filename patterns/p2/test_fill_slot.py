from fill_slot import fill_slot
import pytest

@pytest.mark.parametrize("minutes, target, expected", [
([20, 45, 15, 40], 60, (1,2)),
([30, 10, 30], 60, (0,2)),
([30], 60, None),
([10, 20], 100, None),
([], 60, None),
])
def test_fill_slot(minutes, target, expected):
    assert fill_slot(minutes, target) == expected