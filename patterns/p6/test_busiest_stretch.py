from busiest_stretch import busiest_stretch
import pytest

@pytest.mark.parametrize("tickets, k, expected", [
    ([3, 1, 4, 1, 5, 9, 2], 3, 16),
    ([3, 1, 4, 1, 5, 9, 2], 1, 9),
    ([2, 2, 2], 3, 6),
    ([5, 1], 3, 0),
    ([1], 1, 1),
    ([1], 0, 0)
])
def test_busiest_stretch(tickets, k, expected):
    assert busiest_stretch(tickets, k) == expected