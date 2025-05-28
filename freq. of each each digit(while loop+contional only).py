num = int(input("Enter a number: "))
freq0 = freq1 = freq2 = freq3 = freq4 = 0
freq5 = freq6 = freq7 = freq8 = freq9 = 0

while num > 0:
    digit = num % 10
    if digit == 0:
        freq0 += 1
    elif digit == 1:
        freq1 += 1
    elif digit == 2:
        freq2 += 1
    elif digit == 3:
        freq3 += 1
    elif digit == 4:
        freq4 += 1
    elif digit == 5:
        freq5 += 1
    elif digit == 6:
        freq6 += 1
    elif digit == 7:
        freq7 += 1
    elif digit == 8:
        freq8 += 1
    elif digit == 9:
        freq9 += 1
    num //= 10

if freq0 > 0:
    print("0:", freq0)
if freq1 > 0:
    print("1:", freq1)
if freq2 > 0:
    print("2:", freq2)
if freq3 > 0:
    print("3:", freq3)
if freq4 > 0:
    print("4:", freq4)
if freq5 > 0:
    print("5:", freq5)
if freq6 > 0:
    print("6:", freq6)
if freq7 > 0:
    print("7:", freq7)
if freq8 > 0:
    print("8:", freq8)
if freq9 > 0:
    print("9:", freq9)