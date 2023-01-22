n = int(input())
balance = 0
for i in range(n):
    string = input()
    if string == "(":
        balance += 1
        if balance > 1:
            print("UNBALANCED")
            exit()
    elif string == ")":
        balance -= 1
if balance == 0:
    print("BALANCED")
else:
    print("UNBALANCED")
