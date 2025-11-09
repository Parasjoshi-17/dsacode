from collections import deque

event_queue = deque()

def add_event(name, date):
    event = {"name": name, "date": date}
    event_queue.append(event)
    print(f"event '{name}' added successfully!")

def process_next_event():
    if len(event_queue) == 0:
        print("No events to process!")
    else:
        event = event_queue.popleft()
        print(f"Processing Event: {event['name']} on {event['date']}")

def display_pending_events():
    if len(event_queue) == 0:
        print(" No pending events.")
    else:
        print("\n Pending Events:")
        for i, event in enumerate(event_queue, start=1):
            print(f"{i}. {event['name']} (Date: {event['date']})")

def cancel_event(name):
    found = False
    for event in list(event_queue):
        if event["name"].lower() == name.lower():
            event_queue.remove(event)
            print(f"❌ Event '{name}' has been canceled.")
            found = True
            break
    if not found:
        print(f" Event '{name}' not found or already processed.")

while True:
    print("\n===== Real-Time Event Processing System =====")
    print("1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel an Event")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Event Name: ")
        date = input("Enter Event Date (DD-MM-YYYY): ")
        add_event(name, date)
    elif choice == 2:
        process_next_event()
    elif choice == 3:
        display_pending_events()
    elif choice == 4:
        name = input("Enter Event Name to Cancel: ")
        cancel_event(name)
    elif choice == 5:
        print("Exiting... Thank you!")
        break
    else:
        print("❗ Invalid choice. Please try again.")