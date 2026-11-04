def first_one_time_caller(callers):
    counts = {}

    for caller in callers:
        if caller not in counts:
            counts[caller] = 1
        else:
            counts[caller] += 1

    for caller in counts:
        if counts[caller] == 1:
            return caller

    return None