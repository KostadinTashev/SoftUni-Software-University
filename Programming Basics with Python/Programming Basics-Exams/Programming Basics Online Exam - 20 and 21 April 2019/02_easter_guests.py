import math

guests_count = int(input())
budget = int(input())
cake_count = guests_count / 3
cake_count = math.ceil(cake_count)
eggs_count = guests_count * 2
cake_price = cake_count * 4
eggs_price = eggs_count * 0.45
total_price = eggs_price + cake_price
diff = abs(budget - total_price)
if budget >= total_price:
    print(f"Lyubo bought {cake_count} Easter bread and {eggs_count} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")
