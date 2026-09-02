class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # i. Create a linked list
    def create(self):
        n = int(input("Enter the number of nodes: "))

        if n <= 0:
            print("List cannot be created.")
            return

        for i in range(n):
            data = int(input(f"Enter data for node {i + 1}: "))
            self.insert_end(data)

        print("Circular linked list created successfully.")

    # ii. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

        print("Node inserted at beginning.")

    # iii. Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

        print("Node inserted at end.")

    # iv. Insert at specific index
    def insert_at_index(self, data, index):
        if index < 0:
            print("Invalid index.")
            return

        if index == 0:
            self.insert_beginning(data)
            return

        if self.head is None:
            print("List is empty.")
            return

        new_node = Node(data)
        current = self.head
        count = 0

        while count < index - 1 and current != self.tail:
            current = current.next
            count += 1

        if count != index - 1:
            print("Index out of range.")
            return

        new_node.next = current.next
        current.next = new_node

        if current == self.tail:
            self.tail = new_node

        print("Node inserted at index", index)

    # v. Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return

        # If head contains the value
        if self.head.data == value:

            # Only one node
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head

            print("Node deleted.")
            return

        current = self.head

        while current.next != self.head:
            if current.next.data == value:

                # If deleting tail
                if current.next == self.tail:
                    self.tail = current

                current.next = current.next.next
                self.tail.next = self.head

                print("Node deleted.")
                return

            current = current.next

        print("Value not found.")

    # vi. Delete at beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

        print("First node deleted.")

    # vii. Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty.")
            return

        # Only one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
            print("Last node deleted.")
            return

        current = self.head

        while current.next != self.tail:
            current = current.next

        current.next = self.head
        self.tail = current

        print("Last node deleted.")

    # viii. Count number of nodes
    def count_nodes(self):
        if self.head is None:
            return 0

        count = 1
        current = self.head.next

        while current != self.head:
            count += 1
            current = current.next

        return count

    # ix. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head

        print("Circular Linked List:")

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(HEAD)")

        print("Head:", self.head.data)
        print("Tail:", self.tail.data)
        print("Tail.next:", self.tail.next.data, "(Head)")


# Main program
cll = CircularLinkedList()

while True:

    print("\n========== CIRCULAR LINKED LIST ==========")
    print("1. Create a linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific index")
    print("5. Delete by value")
    print("6. Delete at beginning")
    print("7. Delete at the end")
    print("8. Count number of nodes")
    print("9. Display / Traverse")
    print("10. Display Head and Tail")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cll.create()

    elif choice == 2:
        data = int(input("Enter data: "))
        cll.insert_beginning(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        cll.insert_end(data)

    elif choice == 4:
        data = int(input("Enter data: "))
        index = int(input("Enter index: "))
        cll.insert_at_index(data, index)

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        cll.delete_by_value(value)

    elif choice == 6:
        cll.delete_beginning()

    elif choice == 7:
        cll.delete_end()

    elif choice == 8:
        print("Number of nodes:", cll.count_nodes())

    elif choice == 9:
        cll.display()

    elif choice == 10:
        if cll.head is None:
            print("List is empty.")
        else:
            print("Head:", cll.head.data)
            print("Tail:", cll.tail.data)
            print("Tail.next:", cll.tail.next.data, "(Head)")

    elif choice == 11:
        print("Program exited.")
        break

    else:
        print("Invalid choice. Please try again.")
