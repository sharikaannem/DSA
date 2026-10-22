
class BinaryTree:
    def __init__(self, size=100):
        self.tree = [None] * size
        self.size = size

    def insert_root(self, value):
        if self.tree[0] is not None:
            print("Root already exists!")
        else:
            self.tree[0] = value
            print("Root inserted successfully.")

    def insert_left(self, parent, value):
        if parent not in self.tree:
            print("Parent not found!")
            return

        i = self.tree.index(parent)
        left = 2 * i + 1

        if left >= self.size:
            print("Array capacity exceeded!")
        elif self.tree[left] is not None:
            print("Left child already exists!")
        else:
            self.tree[left] = value
            print("Left child inserted successfully.")

    def insert_right(self, parent, value):
        if parent not in self.tree:
            print("Parent not found!")
            return

        i = self.tree.index(parent)
        right = 2 * i + 2

        if right >= self.size:
            print("Array capacity exceeded!")
        elif self.tree[right] is not None:
            print("Right child already exists!")
        else:
            self.tree[right] = value
            print("Right child inserted successfully.")

    def search(self, value):
        if value in self.tree:
            print("Element found.")
        else:
            print("Element not found.")

    def display(self):
        if all(x is None for x in self.tree):
            print("Tree is empty.")
            return

        print("Array representation:")
        for i, value in enumerate(self.tree):
            if value is not None:
                print(f"Index {i}: {value}")

    def preorder(self, i=0):
        if i >= self.size or self.tree[i] is None:
            return
        print(self.tree[i], end=" ")
        self.preorder(2 * i + 1)
        self.preorder(2 * i + 2)

    def inorder(self, i=0):
        if i >= self.size or self.tree[i] is None:
            return
        self.inorder(2 * i + 1)
        print(self.tree[i], end=" ")
        self.inorder(2 * i + 2)

    def postorder(self, i=0):
        if i >= self.size or self.tree[i] is None:
            return
        self.postorder(2 * i + 1)
        self.postorder(2 * i + 2)
        print(self.tree[i], end=" ")

    def delete(self, value):
        if value not in self.tree:
            print("Element not found!")
            return

        i = self.tree.index(value)

        # A node can be deleted only if it has no children
        left = 2 * i + 1
        right = 2 * i + 2

        if ((left < self.size and self.tree[left] is not None)
                or (right < self.size and self.tree[right] is not None)):
            print("Delete its children first!")
        else:
            self.tree[i] = None
            print("Element deleted successfully.")


bt = BinaryTree()

while True:
    print("\n--- BINARY TREE MENU ---")
    print("1. Insert Root")
    print("2. Insert Left Child")
    print("3. Insert Right Child")
    print("4. Search Element")
    print("5. Display Tree")
    print("6. Preorder Traversal")
    print("7. Inorder Traversal")
    print("8. Postorder Traversal")
    print("9. Delete Element")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter root value: "))
        bt.insert_root(value)

    elif choice == 2:
        parent = int(input("Enter parent value: "))
        value = int(input("Enter left child value: "))
        bt.insert_left(parent, value)

    elif choice == 3:
        parent = int(input("Enter parent value: "))
        value = int(input("Enter right child value: "))
        bt.insert_right(parent, value)

    elif choice == 4:
        value = int(input("Enter element to search: "))
        bt.search(value)

    elif choice == 5:
        bt.display()

    elif choice == 6:
        print("Preorder:", end=" ")
        bt.preorder()
        print()

    elif choice == 7:
        print("Inorder:", end=" ")
        bt.inorder()
        print()

    elif choice == 8:
        print("Postorder:", end=" ")
        bt.postorder()
        print()

    elif choice == 9:
        value = int(input("Enter element to delete: "))
        bt.delete(value)

    elif choice == 10:
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Try again.")
