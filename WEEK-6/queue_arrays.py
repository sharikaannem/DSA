class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    # Enqueue operation
    def enqueue(self, data):
        self.queue.append(data)
        self.rear += 1

        if self.front == -1:
            self.front = 0

        print(data, "inserted into the queue.")

    # Dequeue operation
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow. Queue is empty.")
        else:
            data = self.queue[self.front]
            self.front += 1
            print(data, "deleted from the queue.")

    # Peek operation
    def peek(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty.")
        else:
            print("Front element is:", self.queue[self.front])

    # Display all elements
    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty.")
        else:
            print("Queue elements are:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])

    # Count number of elements
    def count(self):
        if self.front == -1 or self.front > self.rear:
            print("Number of elements: 0")
        else:
            print("Number of elements:", self.rear - self.front + 1)


# Main program
q = Queue()

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Count")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element: "))
        q.enqueue(data)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.peek()

    elif choice == 4:
        q.display()

    elif choice == 5:
        q.count()

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
