n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*", end="")

    for j in range(i-1):
        print(" *", end="")

    print()

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("*", end="")

    for j in range(i-1):
        print(" *", end="")

    print()