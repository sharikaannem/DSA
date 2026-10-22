class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Enqueue operation
    def enqueue(self, data):
        # Check if queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow. Queue is full.")
            return

        # First element
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = data
        print(data, "inserted into the circular queue.")

    # Dequeue operation
    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow. Queue is empty.")
            return

        data = self.queue[self.front]

        # Only one element is present
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(data, "deleted from the circular queue.")

    # Peek operation
    def peek(self):
        if self.front == -1:
            print("Queue is empty.")
        else:
            print("Front element is:", self.queue[self.front])

    # Display operation
    def display(self):
        if self.front == -1:
            print("Queue is empty.")
        else:
            print("The elements of the queue are:")

            i = self.front

            while True:
                print(self.queue[i])

                if i == self.rear:
                    break

                i = (i + 1) % self.size

    # Count operation
    def count(self):
        if self.front == -1:
            print("Number of elements: 0")
        else:
            count = 0
            i = self.front

            while True:
                count += 1

                if i == self.rear:
                    break

                i = (i + 1) % self.size

            print("Number of elements:", count)


# Main program
size = int(input("Enter the size of the circular queue: "))

q = CircularQueue(size)

while True:
    print("\n--- CIRCULAR QUEUE MENU ---")
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
