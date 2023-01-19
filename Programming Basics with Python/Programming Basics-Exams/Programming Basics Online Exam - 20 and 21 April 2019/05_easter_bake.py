import math

cake_count = int(input())
total_sugar = 0
total_flour = 0
sugar_list = []
flour_list = []
for current_cake in range(1, cake_count + 1):
    sugar = int(input())
    flour = int(input())
    sugar_list.append(sugar)
    flour_list.append(flour)

    total_sugar += sugar
    total_flour += flour
sugar_list.sort(reverse=True)
flour_list.sort(reverse=True)
packets_sugar = math.ceil(total_sugar / 950)
packets_flour = math.ceil(total_flour/ 750)
max_flour = flour_list.pop(0)
max_sugar = sugar_list.pop(0)

print(f"Sugar: {packets_sugar}")
print(f"Flour: {packets_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")