price_for_over_20_kg = float(input())
baggage_kg = float(input())
days_before_trip = int(input())
baggage_count = int(input())
price = 0
if baggage_kg <= 10:
    price = price_for_over_20_kg * 0.2
elif 10 < baggage_kg <= 20:
    price = price_for_over_20_kg * 0.5
else:
    price = price_for_over_20_kg
if days_before_trip > 30:
    price = price * 1.1
elif 7 <= days_before_trip <= 30:
    price = price * 1.15
else:
    price = price * 1.4
total_price = price * baggage_count
print(f" The total price of bags is: {total_price:.2f} lv. ")