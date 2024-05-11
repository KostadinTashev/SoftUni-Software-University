city = input()
qty_sold = float(input())
com = 0
city_check = 0
if city == "Sofia":
    if 0 <= qty_sold <= 500:
        com = qty_sold * 0.05
    elif 500 < qty_sold <= 1000:
        com = qty_sold * 0.07
    elif 1000 < qty_sold <= 10000:
        com = qty_sold * 0.08
    elif qty_sold > 10000:
        com = qty_sold * 0.12
    else:
        com = "invalid"
elif city == "Varna":
    if 0 <= qty_sold <= 500:
        com = qty_sold * 0.045
    elif 500 < qty_sold <= 1000:
        com = qty_sold * 0.075
    elif 1000 < qty_sold <= 10000:
        com = qty_sold * 0.10
    elif qty_sold > 10000:
        com = qty_sold * 0.13
    else:
        com = "invalid"
elif city == "Plovdiv":
    if 0 <= qty_sold <= 500:
        com = qty_sold * 0.055
    elif 500 < qty_sold <= 1000:
        com = qty_sold * 0.08
    elif 1000 < qty_sold <= 10000:
        com = qty_sold * 0.12
    elif qty_sold > 10000:
        com = qty_sold * 0.145
    else:
        com = "invalid"
else:
    city_check = "invalid"

if com != "invalid" and city_check != "invalid":
    print(f"{com:.2f}")
else:
    print("error")
