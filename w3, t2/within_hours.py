def is_within_hours(hour, minute):
    """
    Appointments may start from 9:00 up to and including 16:30.
    hour is 0-23. minute 0 or 30.
    Return True if the start time is allowed. otherwise False.
    If hour is outside of the range of 0-23 OR the minute is not 0 or 30, then raise a ValueError
    """
    if hour > 23 or hour < 0:
            raise ValueError(f"Invalid time for appointment: {hour}, {minute}")
    
    if minute != 0 and minute != 30:
            raise ValueError(f"Invalid time for appointment: {hour}, {minute}")
    
    return hour >= 9 and hour <= 16

