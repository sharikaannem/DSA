class AVLTree:
    def __init__(self):
        self.keys = []
        self.left = []
        self.right = []
        self.height = []
        self.root = -1

    # Create a new node
    def create_node(self, key):
        index = len(self.keys)
        self.keys.append(key)
        self.left.append(-1)
        self.right.append(-1)
        self.height.append(1)
        return index

    # Get height
    def get_height(self, index):
        if index == -1:
            return 0
        return self.height[index]

    # Update height
    def update_height(self, index):
        self.height[index] = 1 + max(
            self.get_height(self.left[index]),
            self.get_height(self.right[index])
        )

    # Get balance factor
    def balance(self, index):
        if index == -1:
            return 0
        return (self.get_height(self.left[index])
                - self.get_height(self.right[index]))

    # Right rotation
    def right_rotate(self, y):
        x = self.left[y]
        t2 = self.right[x]

        self.right[x] = y
        self.left[y] = t2

        self.update_height(y)
        self.update_height(x)

        return x

    # Left rotation
    def left_rotate(self, x):
        y = self.right[x]
        t2 = self.left[y]

        self.left[y] = x
        self.right[x] = t2

        self.update_height(x)
        self.update_height(y)

        return y

    # Insert
    def insert_node(self, index, key):
        if index == -1:
            return self.create_node(key)

        if key < self.keys[index]:
            self.left[index] = self.insert_node(
                self.left[index], key
            )
        elif key > self.keys[index]:
            self.right[index] = self.insert_node(
                self.right[index], key
            )
        else:
            print("Duplicate values are not allowed!")
            return index

        self.update_height(index)
        bf = self.balance(index)

        # LL case
        if bf > 1 and key < self.keys[self.left[index]]:
            return self.right_rotate(index)

        # RR case
        if bf < -1 and key > self.keys[self.right[index]]:
            return self.left_rotate(index)

        # LR case
        if bf > 1 and key > self.keys[self.left[index]]:
            self.left[index] = self.left_rotate(
                self.left[index]
            )
            return self.right_rotate(index)

        # RL case
        if bf < -1 and key < self.keys[self.right[index]]:
            self.right[index] = self.right_rotate(
                self.right[index]
            )
            return self.left_rotate(index)

        return index

    # Search
    def search(self, index, key):
        if index == -1:
            return False

        if self.keys[index] == key:
            return True

        if key < self.keys[index]:
            return self.search(self.left[index], key)

        return self.search(self.right[index], key)

    # Find minimum node
    def min_node(self, index):
        while self.left[index] != -1:
            index = self.left[index]
        return index

    # Delete
    def delete_node(self, index, key):
        if index == -1:
            return -1

        if key < self.keys[index]:
            self.left[index] = self.delete_node(
                self.left[index], key
            )

        elif key > self.keys[index]:
            self.right[index] = self.delete_node(
                self.right[index], key
            )

        else:
            # No left child
            if self.left[index] == -1:
                return self.right[index]

            # No right child
            if self.right[index] == -1:
                return self.left[index]

            # Two children
            temp = self.min_node(self.right[index])
            self.keys[index] = self.keys[temp]

            self.right[index] = self.delete_node(
                self.right[index], self.keys[temp]
            )

        self.update_height(index)
        bf = self.balance(index)

        # LL case
        if bf > 1 and self.balance(self.left[index]) >= 0:
            return self.right_rotate(index)

        # LR case
        if bf > 1 and self.balance(self.left[index]) < 0:
            self.left[index] = self.left_rotate(
                self.left[index]
            )
            return self.right_rotate(index)

        # RR case
        if bf < -1 and self.balance(self.right[index]) <= 0:
            return self.left_rotate(index)

        # RL case
        if bf < -1 and self.balance(self.right[index]) > 0:
            self.right[index] = self.right_rotate(
                self.right[index]
            )
            return self.left_rotate(index)

        return index

    # Inorder traversal
    def inorder(self, index):
        if index != -1:
            self.inorder(self.left[index])
            print(self.keys[index], end=" ")
            self.inorder(self.right[index])

    # Preorder traversal
    def preorder(self, index):
        if index != -1:
            print(self.keys[index], end=" ")
            self.preorder(self.left[index])
            self.preorder(self.right[index])

    # Postorder traversal
    def postorder(self, index):
        if index != -1:
            self.postorder(self.left[index])
            self.postorder(self.right[index])
            print(self.keys[index], end=" ")

    # Display tree
    def display(self, index, level=0):
        if index != -1:
            self.display(self.right[index], level + 1)
            print("    " * level + str(self.keys[index]))
            self.display(self.left[index], level + 1)


# Main program
avl = AVLTree()

while True:
    print("\n\n===== AVL TREE USING ARRAYS =====")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Display Tree")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter value to insert: "))
            avl.root = avl.insert_node(avl.root, key)
            print("Insertion completed.")

        elif choice == 2:
            key = int(input("Enter value to delete: "))

            if avl.search(avl.root, key):
                avl.root = avl.delete_node(avl.root, key)
                print("Node deleted successfully.")
            else:
                print("Value not found.")

        elif choice == 3:
            key = int(input("Enter value to search: "))

            if avl.search(avl.root, key):
                print("Value found.")
            else:
                print("Value not found.")

        elif choice == 4:
            print("Inorder:", end=" ")
            avl.inorder(avl.root)
            print()

        elif choice == 5:
            print("Preorder:", end=" ")
            avl.preorder(avl.root)
            print()

        elif choice == 6:
            print("Postorder:", end=" ")
            avl.postorder(avl.root)
            print()

        elif choice == 7:
            if avl.root == -1:
                print("Tree is empty.")
            else:
                avl.display(avl.root)

        elif choice == 8:
            print("Exiting program.")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid integer.")
