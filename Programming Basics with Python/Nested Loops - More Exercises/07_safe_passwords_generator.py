a = int(input())
b = int(input())
max_cnt = int(input())
flag = False
cnt = 0

for A in range(35, 55):
    for B in range(64, 96):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                cnt += 1

                if cnt > max_cnt:
                    flag = True
                    break
                print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end='|')
                if x == a and y == b:
                    flag = True
                    break
                A += 1
                if A > 55:
                    A = 35
                B += 1
                if B > 96:
                    B = 64

            if flag:
                break
        if flag:
            break
    if flag:
        break
