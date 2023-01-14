import math

magnoliq = int(input())
zumbul = int(input())
roza = int(input())
kaktus = int(input())
cena_gift = float(input())

price_magnoiliq = magnoliq * 3.25
price_zumbul = zumbul * 4
price_roza = roza * 3.50
price_kaktus = kaktus * 8
all_price = price_magnoiliq + price_zumbul + price_kaktus + price_roza
total_price = all_price * 0.95
diff = abs(total_price - cena_gift)
if total_price >= cena_gift:
    print(f"She is left with {math.floor(diff)} leva.")
else:
    print(f"She will have to borrow {math.ceil(diff)} leva.")