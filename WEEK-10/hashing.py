SIZE = 11

# Separate Chaining
chaining = [[] for _ in range(SIZE)]

# Linear Probing and Quadratic Probing
linear = [None] * SIZE
quadratic = [None] * SIZE


def insert_chaining(key):
    index = key % SIZE
    chaining[index].append(key)
    print("Element inserted successfully.")


def search_chaining(key):
    index = key % SIZE
    if key in chaining[index]:
        print("Element found at index", index)
    else:
        print("Element not found.")


def display_chaining():
    print("\nHash Table using Separate Chaining:")
    for i in range(SIZE):
        print(i, ":", chaining[i])


def insert_linear(key):
    index = key % SIZE

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if linear[pos] is None:
            linear[pos] = key
            print("Element inserted at index", pos)
            return

    print("Hash table is full.")


def search_linear(key):
    index = key % SIZE

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if linear[pos] is None:
            break

        if linear[pos] == key:
            print("Element found at index", pos)
            return

    print("Element not found.")


def display_linear():
    print("\nHash Table using Linear Probing:")
    for i in range(SIZE):
        print(i, ":", linear[i])


def insert_quadratic(key):
    index = key % SIZE

    for i in range(SIZE):
        pos = (index + i * i) % SIZE

        if quadratic[pos] is None:
            quadratic[pos] = key
            print("Element inserted at index", pos)
            return

    print("No empty position found.")


def search_quadratic(key):
    index = key % SIZE

    for i in range(SIZE):
        pos = (index + i * i) % SIZE

        if quadratic[pos] is None:
            break

        if quadratic[pos] == key:
            print("Element found at index", pos)
            return

    print("Element not found.")


def display_quadratic():
    print("\nHash Table using Quadratic Probing:")
    for i in range(SIZE):
        print(i, ":", quadratic[i])


# Main Menu
while True:
    print("\n===== HASHING TECHNIQUES =====")
    print("1. Separate Chaining")
    print("2. Linear Probing")
    print("3. Quadratic Probing")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Program terminated.")
        break

    if choice not in [1, 2, 3]:
        print("Invalid choice.")
        continue

    while True:
        print("\n1. Insert")
        print("2. Search")
        print("3. Display")
        print("4. Back to Main Menu")

        operation = int(input("Enter your operation: "))

        if operation == 4:
            break

        if operation not in [1, 2, 3]:
            print("Invalid operation.")
            continue

        if operation in [1, 2]:
            key = int(input("Enter the element: "))

        if choice == 1:
            if operation == 1:
                insert_chaining(key)
            elif operation == 2:
                search_chaining(key)
            elif operation == 3:
                display_chaining()

        elif choice == 2:
            if operation == 1:
                insert_linear(key)
            elif operation == 2:
                search_linear(key)
            elif operation == 3:
                display_linear()

        elif choice == 3:
            if operation == 1:
                insert_quadratic(key)
            elif operation == 2:
                search_quadratic(key)
            elif operation == 3:
                display_quadratic()
