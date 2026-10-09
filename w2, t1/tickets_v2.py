tickets = [
    {"id": 101, "category": "network", "priority": "high", "minutes": 45},
    {"id": 102, "category": "printer", "priority": "low", "minutes": 10},
    {"id": 103, "category": "password", "priority": "low", "minutes": 5},
    {"id": 104, "category": "network", "priority": "high", "minutes": 90},
    {"id": 105, "category": "software", "priority": "medium", "minutes": 30},
    {"id": 106, "category": "network", "priority": "medium", "minutes": 25},
]

# for ticket in tickets:          # ticket is one whole dictionary
#     print(ticket["priority"])   # look up one field in it

# ids = []                        # an empty list
# ids.append(101)                 # add an item to the end

# def name(parameter):        # define a function
#     for item in some_list:  # loop over each item
#         if item > 5:        # condition
#             ...
#     return result

# counts = {}                 # empty dictionary
# counts["hi"] = 1            # store a value under a key
# counts["hi"] += 1           # add to it
# "hi" in counts              # True or False: is the key there?
# "hi hi there".split()       # gives ["hi", "hi", "there"]

def count_by_priority(tickets):
    priority_count = {}
    for ticket in tickets:
        priority = ticket["priority"]
        if priority not in priority_count:
            priority_count[priority] = 1
        else:
            priority_count[priority] += 1

    return priority_count


print(count_by_priority(tickets))
