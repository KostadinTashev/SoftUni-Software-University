number = input()
m = sorted(number, reverse=True)
for d, digit in enumerate(m):
    print(digit, end="")