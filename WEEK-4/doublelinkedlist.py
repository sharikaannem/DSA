class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None

    # a. Create Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter data: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head

                while temp.next is not None:
                    temp = temp.next

                temp.next = new_node
                new_node.prev = temp

        print("Double Linked List created successfully.")

    # b. Insert at Beginning
    def insert_beginning(self):
        data = int(input("Enter data: "))

        new_node = Node(data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

        print(f"Inserted {data} at the beginning.")

    # c. Insert at End
    def insert_end(self):
        data = int(input("Enter data: "))

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

        print(f"Inserted {data} at the end.")

    # d. Insert at Specific Index
    def insert_at_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))

        if index < 0:
            print("Invalid index.")
            return

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node

            print(f"Inserted {data} at index {index}.")
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Index out of range.")
                return

            temp = temp.next

        if temp is None:
            print("Index out of range.")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

        print(f"Inserted {data} at index {index}.")

    # e. Delete by Value
    def delete_by_value(self):
        value = int(input("Enter value to delete: "))

        if self.head is None:
            print("Doubly Linked List is empty.")
            return

        temp = self.head

        while temp is not None:
            if temp.data == value:
                break
            temp = temp.next

        if temp is None:
            print(f"{value} not found in the Linked List.")
            return

        if temp.prev is None:
            self.head = temp.next

            if self.head is not None:
                self.head.prev = None

        else:
            temp.prev.next = temp.next

            if temp.next is not None:
                temp.next.prev = temp.prev

        print(f"Deleted {value}.")

    # f. Delete First Node
    def delete_first(self):
        if self.head is None:
            print("Doubly Linked List is empty.")
            return

        deleted = self.head.data

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        print(f"Deleted first node: {deleted}")

    # g. Delete Last Node
    def delete_last(self):
        if self.head is None:
            print("Doubly Linked List is empty.")
            return

        temp = self.head
        
        if temp.next is None:
            deleted = temp.data
            self.head = None
            print(f"Deleted last node: {deleted}")
            return
        
        while temp.next is not None:
            temp = temp.next

        deleted = temp.data

        temp.prev.next = None

        print(f"Deleted last node: {deleted}")

    # h. Count Number of Nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # i. Display
    def display(self):
        if self.head is None:
            print("Doubly Linked List is empty.")
            return

        temp = self.head

        print("Doubly Linked List:", end=" ")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Main Program
dll = DoubleLinkedList()

while True:

    print("\n----- DOUBLE LINKED LIST -----")
    print("1. Create Linked List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Specific Index")
    print("5. Delete by Value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count Number of Nodes")
    print("9. Display")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        dll.create()

    elif choice == 2:
        dll.insert_beginning()

    elif choice == 3:
        dll.insert_end()

    elif choice == 4:
        dll.insert_at_index()

    elif choice == 5:
        dll.delete_by_value()

    elif choice == 6:
        dll.delete_first()

    elif choice == 7:
        dll.delete_last()

    elif choice == 8:
        dll.count_nodes()

    elif choice == 9:
        dll.display()

    elif choice == 10:
        print("Exiting Program...")
        break

    else:
        print("Invalid choice. Please try again.")
