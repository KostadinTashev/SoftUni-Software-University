day = int(input())
room = input()
grade = input()
price = 0

if day < 10:
    if room == "room for one person":
        price = 18 * (day - 1)
    elif room == "apartment":
        price = (25 * (day - 1)) * 0.7
    elif room == "president apartment":
        price = ((35 * (day - 1)) * 0.9)

elif 10 <= day <= 15:
    if room == "room for one person":
        price = 18 * (day - 1)
    elif room == "apartment":
        price = (25 * (day - 1) * 0.65)
    elif room == "president apartment":
        price = (35 * (day - 1) * 0.85)
elif day > 15:
    if room == "room for one person":
        price = 18 * (day - 1)
    elif room == "apartment":
        price = (25 * (day - 1) * 0.5)
    elif room == "president apartment":
        price = (35 * (day - 1) * 0.8)

if grade == "positive":
    price = price * 1.25
elif grade == "negative":
    price = price * 0.9

print(f"{price:.2f}")
