from busiest_start import busiest_start
import pytest

@pytest.mark.parametrize("tickets, k, expected", [
    ([3, 1, 4, 1, 5, 9, 2], 3, 4),
    ([9, 1, 1, 1], 1, 0),
    ([2, 2, 2], 3, 0),
    ([5, 1], 3, -1),
    ([1, 1, 1, 9], 1, 3),
    ([3, 1, 3, 1], 1, 0)
])
def test_busiest_start(tickets, k, expected):
    assert busiest_start(tickets, k) == expected