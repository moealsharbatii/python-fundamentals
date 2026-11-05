def one_time_callers(callers):
    counts = {}

    for caller in callers:
        if caller not in counts:
            counts[caller] = 1

        else:
            counts[caller] += 1

    one_time_caller = []

    for caller in counts:
        if counts[caller] == 1:
            one_time_caller.append(caller)

    return one_time_caller