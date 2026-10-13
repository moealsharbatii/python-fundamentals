def load_tickets(filename):
    with open(filename) as file:
        lines = file.readlines()

    tickets = []
    for line in lines[1:]:
        clean = line.strip()
        parts = clean.split(",")
        ticket = {
                "id": int(parts[0]),
                "category": parts[1],
                "priority": parts[2],
                "minutes": int(parts[3])
        }
        tickets.append(ticket)

    return tickets


def count_by_priority(tickets):
    priority_count = {}
    valid_priorities = ["high", "medium", "low"]

    for ticket in tickets:        
        priority = ticket["priority"]

        if priority not in valid_priorities:
            raise ValueError(f"Invalid priority: {priority}")

        if priority not in priority_count:
            priority_count[priority] = 1
        else:
            priority_count[priority] += 1

    return priority_count

def high_priority_ids(tickets):
    high_ids = []
    for ticket in tickets:
        priority = ticket["priority"]
        if priority == "high":
            high_ids.append(ticket["id"])

    return high_ids

def total_minutes(tickets):
    total_min = 0
    for ticket in tickets:
        
        minutes = ticket["minutes"]
        if minutes < 0:
            raise ValueError(f"Cannot have negative minutes: {minutes}")
        total_min += minutes

    return total_min

def slowest_ticket(tickets):
     if tickets == []:
         return None
    
     slowest = tickets[0]
     for ticket in tickets:
        minutes = ticket["minutes"]
        if slowest["minutes"] < minutes: # would be better with minutes on left-hand side for easier readability
            slowest = ticket

     return slowest
       
if __name__ == "__main__":
    tickets = load_tickets("tickets.csv")
    print(count_by_priority(tickets))
    print(high_priority_ids(tickets))
    print(total_minutes(tickets))
    print(slowest_ticket(tickets))