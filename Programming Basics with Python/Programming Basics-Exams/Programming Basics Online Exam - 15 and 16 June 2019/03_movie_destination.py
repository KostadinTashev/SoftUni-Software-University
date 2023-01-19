film_budget = float(input())
destination = input()
season = input()
days_count = int(input())
total_price = 0
if season == "Winter":
    if destination == "Dubai":
        total_price = days_count * 45000
        total_price *= 0.7
    elif destination == "Sofia":
        total_price = days_count * 17000
        total_price *= 1.25
    elif destination == "London":
        total_price = days_count * 24000
elif season == "Summer":
    if destination == "Dubai":
        total_price = days_count * 40000
        total_price *= 0.7
    elif destination == "Sofia":
        total_price = days_count * 12500
        total_price *= 1.25
    elif destination == "London":
        total_price = days_count * 20250
diff = abs(total_price - film_budget)
if film_budget > total_price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")

