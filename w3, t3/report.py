from tickets_v4 import load_tickets, count_by_priority, total_minutes, slowest_ticket, high_priority_ids


def main(filename):
    try:
        tickets = load_tickets(filename)
        print("File loaded", len(tickets), "tickets")
    except ValueError as error:
        print(f"There's a problem with file: {error}")
        return 1
    except FileNotFoundError:
        print("Could not find the file.")
        return 1
    

    print("Report details:\n")
    print("--- Counts of Priority ---")
    print(count_by_priority(tickets))

    print("--- Total Minutes ---")
    print(total_minutes(tickets))

    print("--- Slowest Ticket ---")
    print(slowest_ticket(tickets))

    print("--- High Priority IDs ---")
    print(high_priority_ids(tickets))

    return 0

if __name__ == "__main__":
    main("tickets.csv")