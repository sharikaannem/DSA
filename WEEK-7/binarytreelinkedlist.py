
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, value):
        if self.root is None:
            self.root = Node(value)
            print("Root inserted successfully.")
        else:
            print("Root already exists!")

    def find(self, value):
        if self.root is None:
            return None

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.data == value:
                return current

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return None

    def insert_left(self, parent, value):
        node = self.find(parent)

        if node is None:
            print("Parent not found!")
        elif node.left is not None:
            print("Left child already exists!")
        else:
            node.left = Node(value)
            print("Left child inserted successfully.")

    def insert_right(self, parent, value):
        node = self.find(parent)

        if node is None:
            print("Parent not found!")
        elif node.right is not None:
            print("Right child already exists!")
        else:
            node.right = Node(value)
            print("Right child inserted successfully.")

    def search(self, value):
        if self.find(value):
            print("Element found.")
        else:
            print("Element not found.")

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def display(self):
        if self.root is None:
            print("Tree is empty.")
            return

        print("Level-order display:")
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        print()

    def delete(self, value):
        if self.root is None:
            print("Tree is empty.")
            return

        if self.root.data == value:
            if self.root.left is None and self.root.right is None:
                self.root = None
                print("Element deleted successfully.")
            else:
                print("Delete its children first!")
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left:
                if current.left.data == value:
                    if (current.left.left is None and
                            current.left.right is None):
                        current.left = None
                        print("Element deleted successfully.")
                    else:
                        print("Delete its children first!")
                    return

                queue.append(current.left)

            if current.right:
                if current.right.data == value:
                    if (current.right.left is None and
                            current.right.right is None):
                        current.right = None
                        print("Element deleted successfully.")
                    else:
                        print("Delete its children first!")
                    return

                queue.append(current.right)

        print("Element not found!")


bt = BinaryTree()

while True:
    print("\n--- BINARY TREE USING LINKED LIST ---")
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
        bt.preorder(bt.root)
        print()

    elif choice == 7:
        print("Inorder:", end=" ")
        bt.inorder(bt.root)
        print()

    elif choice == 8:
        print("Postorder:", end=" ")
        bt.postorder(bt.root)
        print()

    elif choice == 9:
        value = int(input("Enter element to delete: "))
        bt.delete(value)

    elif choice == 10:
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Try again.")
