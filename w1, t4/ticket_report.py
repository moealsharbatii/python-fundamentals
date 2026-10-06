tickets = ["network", "printer", "password", "network", "printer", "network", "software"]

def count_by_category(tickets):
    count = {}
    for ticket in tickets:
        if ticket not in count:
            count[ticket] = 1
        else:
            count[ticket] += 1

    return count

def most_common(counts):
    highest = 0
    highest_category = None
    for category in counts:
        if counts[category] > highest:
            highest = counts[category]
            highest_category = category
            
    return highest_category

def print_reports(counts):
    for category in counts:
        print(f"{category}: {counts[category]}")


counts = count_by_category(tickets)
print(counts)
print(most_common(counts))
print_reports(counts)