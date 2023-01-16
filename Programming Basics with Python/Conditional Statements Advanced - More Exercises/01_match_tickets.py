budget = float(input())
category = input()
people = int(input())
price = 0
if 1 <= people <= 4:
    transport = 0.75 * budget
    if category == "VIP":
        price = 499.99 * people + transport
    elif category == "Normal":
        price = 249.99 * people + transport

elif 5 <= people <= 9:
    transport = 0.60 * budget
    if category == "VIP":
        price = 499.99 * people + transport
    elif category == "Normal":
        price = 249.99 * people + transport

elif 10 <= people <= 24:
    transport = 0.50 * budget
    if category == "VIP":
        price = 499.99 * people + transport
    elif category == "Normal":
        price = 249.99 * people + transport

elif 25 <= people <= 49:
    transport = 0.40 * budget
    if category == "VIP":
        price = 499.99 * people + transport
    elif category == "Normal":
        price = 249.99 * people + transport

elif people >= 50:
    transport = 0.25 * budget
    if category == "VIP":
        price = 499.99 * people + transport
    elif category == "Normal":
        price = 249.99 * people + transport

diff = abs(budget - price)

if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
