def first_duplicate(ticket_ids):
    """
    Return the first ticket id that appears a second time,
    reading the list from left to right.
    Return None if no id repeats.
    """
    seen = set()

    for ticket_id in ticket_ids:
        if ticket_id in seen:
            return ticket_id
        
        seen.add(ticket_id)

    return None