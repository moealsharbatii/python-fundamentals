from tickets_v2 import count_by_priority, slowest_ticket, total_minutes, high_priority_ids
import pytest

# base case: test empty list -> return empty list
# normal case: different and normal amount of minutes -> return the correct sum
# case where there's only one dictionary -> return that time from that dictionary
# unexpected case: negative minutes -> return an error message
def test_total_minutes_empty_list():
    tickets = []
    assert total_minutes(tickets) == 0

def test_total_minutes_one_instance():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": 27}
    ]
    assert total_minutes(tickets) == 27

def test_total_minutes():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": 10},
        {"id": 2, "category": "printer", "priority": "high", "minutes": 5}
    ]
    assert total_minutes(tickets) == 15

def test_total_minutes_reject_negative_minutes():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": 10},
        {"id": 2, "category": "printer", "priority": "high", "minutes": -5}
    ]
    with pytest.raises(ValueError):
        total_minutes(tickets)

def test_total_minutes_rejects_negative_only_ticket():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": -45}
    ]
    with pytest.raises(ValueError, match="-45"):
        total_minutes(tickets)

# base case: empty list -> return empty list
# normal case: multiple 'high' priority ids -> return the list of those ids
# one case: only one priority 'high' -> return that id (although this is probably too simple?)
# no 'high' case: no priority 'high' exists -> return empty list

def test_high_priority_ids_empty_list():
    tickets = []
    assert high_priority_ids(tickets) == []

def test_high_priority_ids_no_high_ids():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": 10},
        {"id": 2, "category": "printer", "priority": "medium", "minutes": 5}
    ]
    assert high_priority_ids(tickets) == []

def test_high_priority_ids_only_one_high_id():
    tickets = [
        {"id": 2, "category": "printer", "priority": "high", "minutes": 5}
    ]
    assert high_priority_ids(tickets) == [2]

def test_high_priority_ids():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": 10},
        {"id": 2, "category": "printer", "priority": "high", "minutes": 5}
    ]
    assert high_priority_ids(tickets) == [2]

# base case: empty list -> return empty list
# normal case: normal data with 1 or more existing for each priority -> return the a dictionary with each count of priority
# one case: only exists in the list -> return the proper key, value pair
# unexpected case: priority is set to a number -> return an error message

def test_count_by_priority_empty_list():
    tickets = []
    assert count_by_priority(tickets) == {}

def test_count_by_priorty_one_dict():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": 10}
    ]
    assert count_by_priority(tickets) == {'low': 1}

def test_count_by_priority_rejects_invalid_priority():
    tickets = [
        {"id": 1, "category": "network", "priority": 5, "minutes": 10},
        {"id": 2, "category": "printer", "priority": "high", "minutes": 5}
    ]
    with pytest.raises(ValueError):
        count_by_priority(tickets)

def test_count_by_priority():
    tickets = [
    {"id": 1, "category": "network", "priority": "low", "minutes": 10},
    {"id": 2, "category": "printer", "priority": "high", "minutes": 5}
    ]
    assert count_by_priority(tickets) == {'low': 1, 'high': 1}

# base case: empty list -> return empty list
# normal case: multiple varying minutes -> find the one that took the longest
# tie case: 2 or more have the same amount of minutes -> should return those ones as they are all a tie
# one case: if there's only one in the list -> return that dict

def test_slowest_ticket_empty_list():
    tickets = []
    assert slowest_ticket(tickets) is None

def test_slowest_ticket_one_ticket():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": 10}
    ]
    assert slowest_ticket(tickets) == tickets[0]

def test_slowest_ticket_two_tickets_tied():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": 10},
        {"id": 2, "category": "printer", "priority": "high", "minutes": 10}
    ]
    assert slowest_ticket(tickets) == tickets[0]

def test_slowest_ticket():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": 10},
        {"id": 2, "category": "printer", "priority": "high", "minutes": 5}
        ]
    assert slowest_ticket(tickets) == tickets[0]

def test_slowest_ticket_in_middle():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": 10},
        {"id": 2, "category": "printer", "priority": "high", "minutes": 25},
        {"id": 3, "category": "printer", "priority": "high", "minutes": 5}
        ]
    assert slowest_ticket(tickets) == tickets[1]

def test_slowest_ticket_at_end():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": 10},
        {"id": 2, "category": "printer", "priority": "high", "minutes": 5},
        {"id": 3, "category": "printer", "priority": "high", "minutes": 25}
    ]
    assert slowest_ticket(tickets) == tickets[2]