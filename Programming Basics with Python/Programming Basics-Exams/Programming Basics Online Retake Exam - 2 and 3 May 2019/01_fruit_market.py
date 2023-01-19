price_strawberry = float(input())
banana_kg = float(input())
orange_kg = float(input())
raspberry_kg = float(input())
strawberry_kg = float(input())
price_raspberry = price_strawberry * 0.5
price_orange = price_raspberry * 0.6
price_banana = price_raspberry * 0.2
sum_raspberry = price_raspberry * raspberry_kg
sum_orange = price_orange * orange_kg
sum_banana = price_banana * banana_kg
sum_strawberry = price_strawberry * strawberry_kg
total_sum = sum_strawberry + sum_raspberry + sum_orange + sum_banana
print(f"{total_sum:.2f}")