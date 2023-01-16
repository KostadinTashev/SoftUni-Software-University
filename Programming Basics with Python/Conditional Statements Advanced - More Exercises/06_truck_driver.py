season = input()
kilometer_month = float(input())
salary = 0
if kilometer_month <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = kilometer_month * 0.75 * 4
    elif season == "Summer":
        salary = kilometer_month * 0.9 * 4
    elif season == "Winter":
        salary = kilometer_month * 1.05 * 4
elif 5000 < kilometer_month <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = kilometer_month * 0.95 * 4
    elif season == "Summer":
        salary = kilometer_month * 1.10 * 4
    elif season == "Winter":
        salary = kilometer_month * 1.25 * 4
elif 10000 < kilometer_month <= 20000:
    salary = kilometer_month * 1.45 * 4

salary = salary * 0.9
print(f"{salary:.2f}")
