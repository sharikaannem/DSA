# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack class
class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

        print(data, "pushed into the stack.")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow. Stack is empty.")
        else:
            data = self.top.data
            self.top = self.top.next

            print(data, "popped from the stack.")

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print("Top element is:", self.top.data)

    # Display all elements
    def display(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print("Stack elements are:")

            current = self.top

            while current is not None:
                print(current.data)
                current = current.next

    # Count number of elements
    def count(self):
        count = 0
        current = self.top

        while current is not None:
            count += 1
            current = current.next

        print("Number of elements:", count)


# Main program
s = Stack()

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Count")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element: "))
        s.push(data)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        s.count()

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
