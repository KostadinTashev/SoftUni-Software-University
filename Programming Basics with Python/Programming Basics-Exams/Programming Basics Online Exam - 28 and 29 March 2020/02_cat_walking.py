minutes_for_walking = int(input())
walking_count = int(input())
calories = int(input())
all_minutes = minutes_for_walking * walking_count
all_burned_calories = all_minutes * 5
if all_burned_calories >= 0.5 * calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {all_burned_calories}.")
else:
    print( f"No, the walk for your cat is not enough. Burned calories per day: {all_burned_calories}.")
