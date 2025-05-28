num = int(input("Enter a number: "))
original = num
sum_fact = 0

while num > 0:
    digit = num % 10
    fact = 1
    i = 1
    while i <= digit:
        fact *= i
        i += 1
    sum_fact += fact
    num //= 10

if sum_fact == original:
    print("Strong Number")
else:
    print("Not a Strong Number")