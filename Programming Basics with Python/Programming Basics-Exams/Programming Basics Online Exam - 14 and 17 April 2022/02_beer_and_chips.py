import math

name_football_fan = input()
budget = float(input())
beer_count = int(input())
packet_chips_count = int(input())
total_price_for_beer = beer_count * 1.20
price_for_one_packet_chips = total_price_for_beer * 0.45
total_price_for_chips = math.ceil(price_for_one_packet_chips * packet_chips_count)
total_price = total_price_for_beer + total_price_for_chips
diff = abs(total_price - budget)
if budget >= total_price:
    print(f"{name_football_fan} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name_football_fan} needs {diff:.2f} more leva!")
