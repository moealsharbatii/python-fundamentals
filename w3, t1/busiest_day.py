def busiest_day(appointments):
    """
    appointments is a list of dictionaries
    like:
            {"patient": "A. Smith", "day": "Monday", "status": "booked"}
        status can be "booked" or "cancelled".
    
    "day" must have a value, and it must be one of the seven day names, spelled exactly.
    Spelling is with the first letter capitalized only (i.e. Monday). Otherwise, anything else is invalid
    and raises a ValueError.
    "status" must be exactly "booked" or "cancelled", anything else like "canceled" or "Booked", raises a ValueError
    if "day" or "status" are missing in the dictionary, raise a ValueError
    Only "booked" appointments are counted.
    Return the busiest day with the most "booked" appointments.
    """
    counts = {}
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    valid_statuses = ["booked", "cancelled"]

    for appt in appointments:
        if "day" not in appt or "status" not in appt:
            raise ValueError(f"Missing field in appointment: {appt}")
        
        day = appt["day"]
        status = appt["status"]

        if day not in valid_days:
            raise ValueError(f"Invalid day: {day}")
        if status not in valid_statuses:
            raise ValueError(f"Invalid status: {status}")

        if status != "booked":
            continue
        
        if day not in counts:
            counts[day] = 1
        else:
            counts[day] += 1

    busiest = None
    highest = 0
    for day in counts:
        if counts[day] > highest:
            highest = counts[day]
            busiest = day

    return busiest
        