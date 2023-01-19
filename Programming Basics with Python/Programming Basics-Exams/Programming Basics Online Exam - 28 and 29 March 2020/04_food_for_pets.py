days = int(input())
total_food = float(input())
biscuits = 0
total_eaten_food = 0
total_eaten_by_dog = 0
total_eaten_by_cat = 0
for current_day in range(1, days + 1):
    food_eaten_by_dog = int(input())
    food_eaten_by_cat = int(input())
    total_eaten_by_cat += food_eaten_by_cat
    total_eaten_by_dog += food_eaten_by_dog
    total_eaten_food += food_eaten_by_cat + food_eaten_by_dog
    if current_day % 3 == 0:
        biscuits += abs((food_eaten_by_cat + food_eaten_by_dog) * 0.1)
percent_eaten_food = total_eaten_food / total_food * 100
percent_eaten_food_by_dog = total_eaten_by_dog / total_eaten_food * 100
percent_eaten_food_by_cat = total_eaten_by_cat / total_eaten_food * 100
print(f"Total eaten biscuits: {biscuits:.0f}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_eaten_food_by_dog:.2f}% eaten from the dog.")
print(f"{percent_eaten_food_by_cat:.2f}% eaten from the cat.")
