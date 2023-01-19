drink = input()
sugar = input()
drink_count = int(input())
total_price = 0
if drink == "Espresso":
    if sugar == "Without":
        total_price = drink_count * 0.90 * 0.65
    elif sugar == "Normal":
        total_price = drink_count * 1.00
    elif sugar == "Extra":
        total_price = drink_count * 1.20
    if drink_count >= 5:
        total_price = total_price * 0.75
elif drink == "Cappuccino":
    if sugar == "Without":
        total_price = drink_count * 1 * 0.65
    elif sugar == "Normal":
        total_price = drink_count * 1.20
    elif sugar == "Extra":
        total_price = drink_count * 1.60
elif drink == "Tea":
    if sugar == "Without":
        total_price = drink_count * 0.50 * 0.65
    elif sugar == "Normal":
        total_price = drink_count * 0.60
    elif sugar == "Extra":
        total_price = drink_count * 0.70
if total_price > 15:
    total_price *= 0.8
print(f"You bought {drink_count} cups of {drink} for {total_price:.2f} lv.")