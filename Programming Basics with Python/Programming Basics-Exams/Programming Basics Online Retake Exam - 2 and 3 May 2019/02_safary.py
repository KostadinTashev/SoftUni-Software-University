budget = float(input())
fuel_liter = float(input())
day_of_week = input()
price_fuel = fuel_liter * 2.10
guide = 100
total_price = price_fuel + guide
if day_of_week == "Saturday":
    total_price *=  0.9
elif day_of_week == "Sunday":
    total_price *= 0.8
diff = abs(total_price - budget)
if budget >= total_price:
    print(f"Safari time! Money left: {diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")