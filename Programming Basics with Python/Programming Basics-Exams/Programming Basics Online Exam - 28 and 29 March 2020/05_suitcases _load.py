plane_capacity = float(input())
no_more_free_place = False
suitcases_counter = 0
iterations_counter = 0
command = input()
while command != "End":
    current_suitcase_volume = float(command)
    iterations_counter += 1
    if iterations_counter % 3 == 0:
        current_suitcase_volume *= 1.1
    if plane_capacity - current_suitcase_volume < 0: # if current_suitcase_volume > plane_capacity
        no_more_free_place = True
        break
    plane_capacity -= current_suitcase_volume
    suitcases_counter += 1
    command = input()
if no_more_free_place: # if no_more_free_place == True
    print("No more space!")
else:
    print(f"Congratulations! All suitcases are loaded!")
print(f"Statistic: {suitcases_counter} suitcases loaded.")