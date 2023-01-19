import math

people_count = int(input())
input_price = float(input())
sunbed_price = float(input())
umbrella_price = float(input())
price_for_tax = people_count * input_price
price_for_sunbed = math.ceil(people_count * 0.75) * sunbed_price
price_for_umbrella = math.ceil(people_count * 0.5) * umbrella_price
total_price = price_for_tax + price_for_sunbed + price_for_umbrella
print(f"{total_price:.2f} lv.")
