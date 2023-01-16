budget = float(input())
season = input()
clas = ""
type_car = ""
price = 0
if budget <= 100:
    clas = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    clas = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        price = budget * 0.8
elif budget > 500:
    clas = "Luxury class"
    type_car = "Jeep"
    price = budget * 0.9
print(f"{clas}")
print(f"{type_car} - {price:.2f}")