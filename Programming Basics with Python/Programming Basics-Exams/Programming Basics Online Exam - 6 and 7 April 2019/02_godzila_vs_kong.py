budget_film = float(input())
workers_count = int(input())
price_for_clothes = float(input())
decor = budget_film * 0.1
price_clothes = workers_count * price_for_clothes
if workers_count > 150:
    price_clothes *= 0.9
all_price = decor + price_clothes
diff = abs(budget_film - all_price)
if all_price > budget_film:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")