guests_count = int(input())
covert_price = float(input())
budget = float(input())

if 10 <= guests_count <= 15:
    covert_price = covert_price * 0.85
elif 15 < guests_count <= 20:
    covert_price = covert_price * 0.80
elif guests_count > 20:
    covert_price = covert_price * 0.75
covert_price = covert_price * guests_count
cake = budget * 0.1
budget = budget - (covert_price + cake)
diff = abs(budget)
if budget >= 0:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")