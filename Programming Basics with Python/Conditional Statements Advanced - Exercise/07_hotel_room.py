month = input()
days = int(input())
price_studio = 0
price_apart = 0
if month == "May" or month == "October":
    price_studio = 50 * days
    price_apart = 65 * days
    if 7 < days <= 14:
        price_studio = 0.95 * price_studio
    elif days > 14:
        price_studio = 0.70 * price_studio
        price_apart = 0.90 * price_apart

elif month == "June" or month == "September":
    price_studio = 75.20 * days
    price_apart = 68.70 * days
    if days > 14:
        price_studio = 0.8 * price_studio
        price_apart = 0.9 * price_apart

elif month == "July" or month == "August":
    price_studio = 76 * days
    price_apart = 77 * days
    if days > 14:
        price_apart = 0.9 * price_apart

print(f"Apartment: {price_apart:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
