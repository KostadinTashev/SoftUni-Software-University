price_voucher = int(input())
all_price = 0
film = 0
others = 0
command = input()
while command != "End":

    if len(command) > 8:
        all_price += ord(command[0]) + ord(command[1])
        film += 1
        if all_price > price_voucher:
            film -= 1
    elif len(command) <= 8:
        all_price += ord(command[0])
        others += 1
        if all_price > price_voucher:
            others -= 1
    if all_price > price_voucher:
        break
    command = input()

print(film)
print(others)
