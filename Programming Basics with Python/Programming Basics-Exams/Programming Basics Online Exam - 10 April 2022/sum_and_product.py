n = int(input())
is_found = False
count = 0
for a in range(1, 9 + 1):
    for b in range(9, a, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c, -1):
                sum = a + b + c + d
                mult = a * b * c * d
                if sum == mult and n % 10 == 5:
                    count += 1
                    print(str(a) + str(b) + str(c) + str(d))
                    is_found = True
                    break
                elif mult // sum == 3 and n % 3 == 0:
                    count += 1
                    print(str(d) + str(c) + str(b) + str(a))
                    is_found = True
                    break
            if is_found:
                break
        if is_found:
            break
    if is_found:
        break
if count == 0:
    print("Nothing found")