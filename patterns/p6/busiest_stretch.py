def busiest_stretch(tickets , k):

    if len(tickets) < k:
        return 0

    total = sum(tickets[:k])
    best = total
    for i in range(len(tickets) - k):
        total = total - tickets[i] + tickets[i + k]

        if total > best:
            best = total
        
    return best