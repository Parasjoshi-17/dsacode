from datetime import datetime as dt

class Queue:
    def __init__(self, size=10):
        self.size = size
        self.front = -1
        self.rear = -1
        self.q = [None] * size

    def empty(self): return self.front == self.rear
    def full(self): return self.rear == self.size - 1

    def EnQue(self, data):
        if self.full():
            print("Queue Full!")
        else:
            self.rear += 1
            self.q[self.rear] = data
            print(f"Added: {data}")

    def DeQue(self):
        if self.empty():
            print("Queue Empty!")
        else:
            self.front += 1
            print(f"Removed: {self.q[self.front]}")
            self.q[self.front] = None

    def display(self):
        print("\nCurrent Queue:")
        q_data = [x for x in self.q if x]
        print(q_data if q_data else "(Empty Queue)")

def get_time():
    return dt.now().strftime("%H:%M:%S")

# ---------- Main Program ----------
callQ = Queue(10)
custId = 0

while True:
    print("\n1. Add Call  2. Answer Call  3. View Queue  4. Status  5. Exit")
    op = input("Choose option: ")

    if op == '1':
        custId += 1
        callQ.EnQue((custId, get_time()))
    elif op == '2':
        callQ.DeQue()
    elif op == '3':
        callQ.display()
    elif op == '4':
        print("Empty" if callQ.empty() else "Full" if callQ.full() else "Pending Calls Exist")
    elif op == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
