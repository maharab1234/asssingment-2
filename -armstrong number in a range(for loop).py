a = int(input("Enter start of range: "))
b = int(input("Enter end of range: "))

for num in range(a, b + 1):
    temp = num
    sum_pow = 0
    count = 0


    t = temp
    while t > 0:
        count += 1
        t //= 10


    t = temp
    while t > 0:
        digit = t % 10
        power = 1
        for i in range(count):
            power *= digit
        sum_pow += power
        t //= 10

    if sum_pow == num:
        print(num)