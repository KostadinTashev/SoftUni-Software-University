import math

days = int(input())
food = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_kg = float(input())

dog_food = days * dog_food_kg
cat_food = days * cat_food_kg
turtle_food = days * turtle_food_kg / 1000
all_food = dog_food + cat_food + turtle_food
diff = abs(food - all_food)

if all_food <= food:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")