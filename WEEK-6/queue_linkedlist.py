class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into the queue.")

    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow. Queue is empty.")
        else:
            data = self.front.data
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            print(data, "deleted from the queue.")

    # Peek operation
    def peek(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            print("Front element is:", self.front.data)

    # Display all elements
    def display(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            print("Queue elements are:")

            temp = self.front

            while temp is not None:
                print(temp.data)
                temp = temp.next

    # Count number of elements
    def count(self):
        count = 0
        temp = self.front

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of elements:", count)


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
