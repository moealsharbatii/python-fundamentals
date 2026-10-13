from pathlib import Path
from tickets_v3 import load_tickets, total_minutes, count_by_priority, high_priority_ids, slowest_ticket
import pytest
CSV_FILE = Path(__file__).parent / "tickets.csv"

def test_load_tickets_skips_blank_items(tmp_path):
    csv_file = tmp_path / "tickets.csv"
    csv_file.write_text(
        "id,category,priority,minutes\n"
        "101,network,high,45\n"
        "\n"
        "102,printer,low,10\n"
    )
    tickets = load_tickets(csv_file)
    assert len(tickets) == 2

def test_load_tickets_rejects_wrong_number_of_fields(tmp_path):
    csv_file = tmp_path / "tickets.csv"
    csv_file.write_text(
        "id,category,priority,minutes\n"
        "101,network,high,45\n"
        "\n"
        "102,printer,low,10\n"
        "103,password,low,minutes,hours,seconds"
    )
    with pytest.raises(ValueError):
        load_tickets(csv_file)

def test_load_tickets_returns_all_tickets():
    tickets = load_tickets(CSV_FILE)
    assert len(tickets) == 6

def test_load_tickets_returns_first_ticket():
    tickets = load_tickets(CSV_FILE)
    assert tickets[0] == {'id': 101, 'category': "network", 'priority': "high", "minutes": 45}

def test_load_tickets_returns_total_minutes():
    tickets = load_tickets(CSV_FILE)
    assert total_minutes(tickets) == 205

# if a line is blank -> it can thrown an error OR ignore the line and move to the next line
# any of the data can be invalid (i.e. misspelling of any of keys OR wrong values) -> can stll ignore that line and move to the next
# if the data is incomplete (i.e. category is missing 'network' in id 101) -> can ignore that line or raise an error
# it's not a proper .csv, where a comma is missing in between keys -> raise an error