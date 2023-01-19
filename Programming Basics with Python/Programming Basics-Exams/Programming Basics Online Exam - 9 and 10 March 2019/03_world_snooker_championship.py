game_type = input()
ticket_type = input()
ticket_amnt = int(input())
trophy = input()

trophy_pic_price = 40
total_amnt = 0

if game_type == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90

elif game_type == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40

elif game_type == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400

total_amnt = ticket_amnt * ticket_price

# print(ticket_price, total_amnt)

if total_amnt > 2500 and total_amnt <= 4000:
    discount = 0.1
elif total_amnt > 4000:
    discount = 0.25
    trophy_pic_price = 0
else:
    discount = 0

total_pay = total_amnt - (total_amnt * discount)

# print(total_pay)

if trophy == "N":
    trophy_pic_price = 0
elif trophy == "Y":
    trophy_pic_price = trophy_pic_price * ticket_amnt
elif trophy == "Y" and total_amnt > 4000:
    trophy_pic_price = 0

# print(trophy_pic_price)
total_pay = total_pay + trophy_pic_price
print("{:.2f}".format(total_pay))