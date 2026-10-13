from pathlib import Path
from tickets_v3 import load_tickets, total_minutes, count_by_priority, high_priority_ids, slowest_ticket

CSV_FILE = Path(__file__).parent / "tickets.csv"

def test_load_tickets_returns_all_tickets():
    tickets = load_tickets(CSV_FILE)
    assert len(tickets) == 6

def test_load_tickets_returns_first_ticket():
    tickets = load_tickets(CSV_FILE)
    assert tickets[0] == {'id': 101, 'category': "network", 'priority': "high", "minutes": 45}

def test_load_tickets_returns_total_minutes():
    tickets = load_tickets(CSV_FILE)
    assert total_minutes(tickets) == 205