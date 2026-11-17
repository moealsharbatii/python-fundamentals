def busiest_start(tickets, k):
    if len(tickets) < k:
        return -1

    total = sum(tickets[:k])
    start_index = 0
    best = total

    for i in range(len(tickets) - k):
        total = total - tickets[i] + tickets[i + k]

        if total > best:
            best = total
            start_index = i + 1

    return start_index