from within_hours import is_within_hours
import pytest

# Opening time
def test_is_within_hours_start_of_day():
    assert is_within_hours(9, 0) is True

# Just before opening time
def test_is_within_hours_before_start():
    assert is_within_hours(8, 30) is False

# Just before closing time
def test_is_within_hours_before_close():
    assert is_within_hours(16, 0) is True

# Closing time
def test_is_within_hours_end_of_day():
    assert is_within_hours(16, 30) is True

# After closing time
def test_is_within_hours_after_end():
    assert is_within_hours(17, 0) is False

# Middle of the day time
def test_is_within_hours_middle_of_day():
    assert is_within_hours(12, 30) is True

# Testing at 9:30 clock time
def test_is_within_hours_nine_thirty():
    assert is_within_hours(9, 30) is True

# Invalid input on hour
def test_is_within_hours_invalid_hour():
    with pytest.raises(ValueError):
        is_within_hours(24, 0)

def test_is_within_hours_invalid_negative_hour():
    with pytest.raises(ValueError):
        is_within_hours(-1, 0)

# Invalid input on minute
def test_is_within_hour_invalid_minute():
    with pytest.raises(ValueError):
        is_within_hours(12, 16)
