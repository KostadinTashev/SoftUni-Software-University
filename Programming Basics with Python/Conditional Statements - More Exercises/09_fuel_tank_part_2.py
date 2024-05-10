type_fuel = input()
fuel_liter = float(input())
card = input()
price = 0
if type_fuel == "Gasoline":
    if card == "Yes":
        price = fuel_liter * 2.04
        if 20 <= fuel_liter <= 25:
            price = price * 0.92
        elif fuel_liter > 25:
            price = price * 0.9
    elif card == "No":
        price = 2.22 * fuel_liter
        if 20 <= fuel_liter <= 25:
            price = price * 0.92
        elif fuel_liter > 25:
            price = price * 0.9

elif type_fuel == "Diesel":
    if card == "Yes":
        price = fuel_liter * 2.21
        if 20 <= fuel_liter <= 25:
            price = price * 0.92
        elif fuel_liter > 25:
            price = price * 0.9
    elif card == "No":
        price = 2.33 * fuel_liter
        if 20 <= fuel_liter <= 25:
            price = price * 0.92
        elif fuel_liter > 25:
            price = price * 0.9

elif type_fuel == "Gas":
    if card == "Yes":
        price = fuel_liter * 0.85
        if 20 <= fuel_liter <= 25:
            price = price * 0.92
        elif fuel_liter > 25:
            price = price * 0.9
    elif card == "No":
        price = fuel_liter * 0.93
        if 20 <= fuel_liter <= 25:
            price = price * 0.92
        elif fuel_liter > 25:
            price = price * 0.9

print(f"{price:.2f} lv.")
