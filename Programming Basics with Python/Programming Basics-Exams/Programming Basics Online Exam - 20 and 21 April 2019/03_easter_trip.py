destination = input()
date = input()
overnights = int(input())
total_price = 0
if destination == "France":
    if date == "21-23":
        total_price = overnights * 30
    elif date == "24-27":
        total_price = overnights * 35
    elif date == "28-31":
        total_price = overnights * 40
elif destination == "Italy":
    if date == "21-23":
        total_price = overnights * 28
    elif date == "24-27":
        total_price = overnights * 32
    elif date == "28-31":
        total_price = overnights * 39
elif destination == "Germany":
    if date == "21-23":
        total_price = overnights * 32
    elif date == "24-27":
        total_price = overnights * 37
    elif date == "28-31":
        total_price = overnights * 43
print(f"Easter trip to {destination} : {total_price:.2f} leva.")
