import math

average_speed = float(input())
liter_fuel_for_100_km = float(input())
all_distance = 384400 * 2
hour = math.ceil(all_distance / average_speed) + 3
all_fuel = liter_fuel_for_100_km * all_distance / 100
print(hour)
print(f"{all_fuel:.0f}")
