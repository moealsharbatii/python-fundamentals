from within_hours import is_within_hours
import pytest

@pytest.mark.parametrize("hour, minute, expected", [
    (0, 0, False),
    (8, 30, False),
    (9, 0, True),
    (9, 30, True),
    (12, 30, True),
    (16, 0, True),
    (16, 30, True),
    (17, 0, False),
    (23, 30, False),
])
def test_is_within_hours(hour, minute, expected):
    assert is_within_hours(hour, minute) is expected

@pytest.mark.parametrize("hour, minute", [
    (24, 0),
    (-1, 0),
    (12, 16),
    (10, -15),
])
def test_is_within_hours_invalid_hours_minutes(hour, minute):
    with pytest.raises(ValueError):
        is_within_hours(hour, minute)