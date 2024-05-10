trip_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_count = int(input())
minions_count = int(input())
trucks_count = int(input())

price_puzzle = puzzle_count * 2.6
price_dolls = dolls_count * 3
price_teddy = teddy_count * 4.10
price_minions = minions_count * 8.20
price_trucks = trucks_count * 2

total_price = price_puzzle + price_dolls + price_teddy + price_minions + price_trucks
total_toys = puzzle_count + dolls_count + teddy_count + minions_count + trucks_count
if total_toys >= 50:
    total_price = total_price * 0.75

total_price = total_price * 0.9

diff = abs(trip_price - total_price)
if trip_price <= total_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
