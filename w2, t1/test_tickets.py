from tickets_v2 import total_minutes, high_priority_ids

def test_total_minutes():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": 10},
        {"id": 2, "category": "printer", "priority": "high", "minutes": 5}
    ]
    assert total_minutes(tickets) == 15

def test_high_priority_ids():
    tickets = [
        {"id": 1, "category": "network", "priority": "low", "minutes": 10},
        {"id": 2, "category": "printer", "priority": "high", "minutes": 5}
    ]
    assert high_priority_ids(tickets) == [2]