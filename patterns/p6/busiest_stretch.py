def busiest_stretch(tickets , k):
    best = 0
    for i in range(len(tickets) - k + 1):
        next_sum = sum(tickets[i:i + k])

        if next_sum > best:
            best = next_sum
        
    return best