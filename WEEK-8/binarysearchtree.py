
# Binary Search Tree using Arrays - Menu Driven Program

tree = []


# Insert an element
def insert(value):
    global tree

    if len(tree) == 0:
        tree.append(value)
        print("Element inserted successfully")
        return

    i = 0

    while i < len(tree):
        if tree[i] is None:
            tree[i] = value
            print("Element inserted successfully")
            return

        elif value < tree[i]:
            i = 2 * i + 1

        elif value > tree[i]:
            i = 2 * i + 2

        else:
            print("Duplicate elements are not allowed")
            return

        while i >= len(tree):
            tree.append(None)


# Search an element
def search(value):
    i = 0

    while i < len(tree):
        if tree[i] is None:
            print("Element not found")
            return

        elif tree[i] == value:
            print("Element found")
            return

        elif value < tree[i]:
            i = 2 * i + 1

        else:
            i = 2 * i + 2

    print("Element not found")


# Inorder traversal
def inorder(i=0):
    if i < len(tree) and tree[i] is not None:
        inorder(2 * i + 1)
        print(tree[i], end=" ")
        inorder(2 * i + 2)


# Preorder traversal
def preorder(i=0):
    if i < len(tree) and tree[i] is not None:
        print(tree[i], end=" ")
        preorder(2 * i + 1)
        preorder(2 * i + 2)


# Postorder traversal
def postorder(i=0):
    if i < len(tree) and tree[i] is not None:
        postorder(2 * i + 1)
        postorder(2 * i + 2)
        print(tree[i], end=" ")


# Display the array
def display():
    if len(tree) == 0 or tree[0] is None:
        print("Tree is empty")
    else:
        print("Array representation:", tree)


# Delete an element
def delete(value):
    global tree

    def find_index(value):
        i = 0

        while i < len(tree):
            if tree[i] is None:
                return -1
            elif tree[i] == value:
                return i
            elif value < tree[i]:
                i = 2 * i + 1
            else:
                i = 2 * i + 2

        return -1

    index = find_index(value)

    if index == -1:
        print("Element not found")
        return

    # Collect all elements except the one to be deleted
    elements = [
        tree[i] for i in range(len(tree))
        if tree[i] is not None and i != index
    ]

    tree = []

    # Rebuild the BST
    for element in elements:
        insert(element)

    print("Element deleted successfully")


# Main menu
while True:
    print("\n\n--- BINARY SEARCH TREE MENU ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element to insert: "))
        insert(value)

    elif choice == 2:
        value = int(input("Enter element to search: "))
        search(value)

    elif choice == 3:
        value = int(input("Enter element to delete: "))
        delete(value)

    elif choice == 4:
        print("Inorder Traversal:", end=" ")
        inorder()
        print()

    elif choice == 5:
        print("Preorder Traversal:", end=" ")
        preorder()
        print()

    elif choice == 6:
        print("Postorder Traversal:", end=" ")
        postorder()
        print()

    elif choice == 7:
        display()

    elif choice == 8:
        print("Program terminated")
        break

    else:
        print("Invalid choice. Please try again.")
