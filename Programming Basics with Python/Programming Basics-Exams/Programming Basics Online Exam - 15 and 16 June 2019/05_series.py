budget = float(input())
serial_count = int(input())
total_price = 0
for n in range(serial_count):
    serial_name = input()
    price_serial = float(input())
    if serial_name == "Thrones":
        total_price += price_serial * 0.5
    elif serial_name == "Lucifer":
        total_price += price_serial * 0.6
    elif serial_name == "Protector":
        total_price += price_serial * 0.7
    elif serial_name == "TotalDrama":
        total_price += price_serial * 0.8
    elif serial_name == "Area":
        total_price += price_serial * 0.9
    else:
        total_price += price_serial
diff = abs(total_price - budget)
if budget >= total_price:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")