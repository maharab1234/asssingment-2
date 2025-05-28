n = int(input("Enter number of rows: "))
symbol = input("Enter the symbol: ")

# Hollow pyramid pattern
for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")

    # Print symbols and spaces
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print(symbol, end="")
        else:
            print(" ", end="")

    print()  # Move to next line