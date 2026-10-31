def fill_slot(minutes, target):
    seen = {}

    for i, value in enumerate(minutes):
        partner = target - value
        if partner in seen:
            return (seen[partner], i)

        seen[value] = i

    return None