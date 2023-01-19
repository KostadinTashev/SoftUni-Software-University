food_in_kg = int(input())
food_in_grams = food_in_kg * 1000
command = input()
total_food = 0
while command != "Adopted":
    command = int(command)
    total_food += command
    command = input()
diff = abs(total_food - food_in_grams)
if total_food <= food_in_grams:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")