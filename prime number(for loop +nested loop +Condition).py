a = int(input("Enter start of range: "))
b = int(input("Enter end of range: "))

for num in range(a, b + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)