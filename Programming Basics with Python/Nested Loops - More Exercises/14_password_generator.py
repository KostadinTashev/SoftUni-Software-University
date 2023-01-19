number_n = int(input())
number_l = int(input())
for a in range(1, number_n):
    for b in range(1, number_n):
        for c in range(ord('a'), ord('a') + number_l):
            for d in range(ord('a'), ord('a') + number_l):
                for e in range(2, number_n + 1):
                    if e > a and e > b:
                        print(f'{a}{b}{chr(c)}{chr(d)}{e}', end=" ")
