from first_duplicate import first_duplicate
import pytest

@pytest.mark.parametrize("ticket_ids, expected", [
    ([101, 102, 103, 102, 101], 102),
    ([5, 6, 7], None),
    ([], None),
    ([1, 2, 3, 1], 1),
    ([7, 7], 7),
    ([1, 2, 3, 1, 2, 1, 3], 1),
    ([1], None),
])
def test_first_duplicate(ticket_ids, expected):
    assert first_duplicate(ticket_ids) == expected