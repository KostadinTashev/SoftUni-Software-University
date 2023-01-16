age = int(input())
price_laundry = float(input())
price_for_one_toy = int(input())

toys_count = 0
money = 0
brother = 0
even_birthdays = 0

for year in range(1, age + 1):
    if year % 2 != 0:
        toys_count += 1
    else:
        even_birthdays += 1
        brother += 1
        if year != 2:
            money += 10 * even_birthdays
        else:
            money += 10

savings = toys_count * price_for_one_toy + money - brother
diff = abs(savings - price_laundry)

if savings >= price_laundry:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
