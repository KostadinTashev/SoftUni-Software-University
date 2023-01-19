price_flour = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egg_shell = int(input())
yeast = int(input())
total_price_flour = price_flour * flour_kg
price_sugar = price_flour * 0.75
price_eggs = price_flour * 1.1
price_yeast = price_sugar * 0.2
total_price_sugar = price_sugar * sugar_kg
total_price_eggs = egg_shell * price_eggs
total_price_yeast = yeast * price_yeast
total_sum_of_all = total_price_flour + total_price_sugar + total_price_eggs + total_price_yeast
print(f"{total_sum_of_all:.2f}")