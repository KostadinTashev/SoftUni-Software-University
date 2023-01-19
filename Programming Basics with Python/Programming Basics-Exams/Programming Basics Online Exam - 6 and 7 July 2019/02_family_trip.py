budget = float(input())
overnights = int(input())
price_for_one_overnight = float(input())
percentage_for_add = int(input())
total_price = overnights * price_for_one_overnight
if overnights > 7:
    total_price = (0.95 * price_for_one_overnight) * overnights
total_price += percentage_for_add / 100 * budget
diff = abs(total_price - budget)
if budget >= total_price:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation. ")
else:
    print(f"{diff:.2f} leva needed.")