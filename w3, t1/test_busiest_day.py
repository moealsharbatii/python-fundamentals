from busiest_day import busiest_day
import pytest

def test_busiest_day_no_appointments():
    appointments = []
    assert busiest_day(appointments) is None

def test_busiest_day_one_appointment():
    appointments = [{"patient": "Moe A.", "day": "Friday", "status": "booked"}]
    assert busiest_day(appointments) == "Friday"

def test_busiest_day_multiple_appointments():
    appointments = [
        {"patient": "Moe A.", "day": "Monday", "status": "booked"},
        {"patient": "Moe A.", "day": "Tuesday", "status": "booked"},
        {"patient": "Moe A.", "day": "Tuesday", "status": "booked"},
        {"patient": "Moe A.", "day": "Friday", "status": "booked"}
    ]
    assert busiest_day(appointments) == "Tuesday"

def test_busiest_day_appointment_cancelled():
    appointments = [
        {"patient": "Moe A.", "day": "Monday", "status": "cancelled"},
        {"patient": "Moe A.", "day": "Monday", "status": "cancelled"},
        {"patient": "Moe A.", "day": "Monday", "status": "booked"},
        {"patient": "Moe A.", "day": "Tuesday", "status": "booked"},
        {"patient": "Moe A.", "day": "Tuesday", "status": "booked"}
    ]
    assert busiest_day(appointments) == "Tuesday"

def test_busiest_day_missing_value_on_day():
    appointments = [
        {"patient": "Moe A.", "day": "", "status": "booked"},
        {"patient": "Moe A.", "day": "Monday", "status": "booked"},
        {"patient": "Moe A.", "day": "Monday", "status": "booked"},
        {"patient": "Moe A.", "day": "", "status": "booked"},
        {"patient": "Moe A.", "day": "", "status": "booked"}
    ]
    with pytest.raises(ValueError):
        busiest_day(appointments)

def test_busiest_day_rejects_lowercase_day():
    appointments = [
        {"patient": "Moe A.", "day": "friday", "status": "booked"},
        {"patient": "Moe A.", "day": "Monday", "status": "booked"},
        {"patient": "Moe A.", "day": "Monday", "status": "booked"}
    ]
    with pytest.raises(ValueError):
        busiest_day(appointments)

def test_busiest_day_rejects_invalid_status():
    appointments = [
        {"patient": "Moe A.", "day": "Monday", "status": "Cancelled"},
        {"patient": "Moe A.", "day": "Monday", "status": "booked"},
        {"patient": "Moe A.", "day": "Monday", "status": "booked"}
    ]
    with pytest.raises(ValueError):
        busiest_day(appointments)

def test_busiest_day_rejects_invalid_inputs():
    appointments = [
        {"patient": "Moe A.", "day": "monday", "status": "Cancelled"},
        {"patient": "Moe A.", "day": "Monday", "status": "booked"},
        {"patient": "Moe A.", "day": "Monday", "status": "booked"}
    ]
    with pytest.raises(ValueError):
        busiest_day(appointments)

def test_busiest_day_all_appointments_cancelled():
    appointments = [
        {"patient": "Moe A.", "day": "Monday", "status": "cancelled"},
        {"patient": "Moe A.", "day": "Monday", "status": "cancelled"},
        {"patient": "Moe A.", "day": "Monday", "status": "cancelled"}
    ]
    assert busiest_day(appointments) is None

def test_busiest_day_missing_day():
    appointments = [
        {"patient": "Moe A.", "status": "cancelled"},
        {"patient": "Moe A.", "day": "Monday", "status": "booked"},
        {"patient": "Moe A.", "day": "Monday", "status": "booked"}
    ]
    with pytest.raises(ValueError):
        busiest_day(appointments)

def test_busiest_day_missing_status():
    appointments = [
        {"patient": "Moe A.", "day": "Monday"},
        {"patient": "Moe A.", "day": "Monday", "status": "booked"},
        {"patient": "Moe A.", "day": "Monday", "status": "booked"}
    ]
    with pytest.raises(ValueError):
        busiest_day(appointments)
    
