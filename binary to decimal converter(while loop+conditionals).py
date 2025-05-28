binary = int(input("Enter a binary number: "))
decimal = 0
base = 1

while binary > 0:
    last_digit = binary % 10
    if last_digit == 1:
        decimal += base
    base *= 2
    binary //= 10

print("Decimal:", decimal)