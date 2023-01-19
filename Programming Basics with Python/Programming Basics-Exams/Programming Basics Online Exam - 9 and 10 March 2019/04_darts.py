player_name = input()
command = input()
start_points = 301
new_points = 0
successful_shots = 0
bad_shots = 0
while command != "Retire":
    field = command
    points = int(input())
    if field == "Single":
        start_points -= points
        successful_shots += 1
    elif field == "Double":
        start_points -= points * 2
        successful_shots += 1
    elif field == "Triple":
        start_points -= points * 3
        successful_shots += 1
    if start_points < 0:
        if field == "Single":
            start_points += points
        elif field == "Double":
            start_points += points * 2
        elif field == "Triple":
            start_points += points * 3
        bad_shots += 1
        successful_shots -= 1
    if start_points == 0:
        break
    command = input()
if start_points == 0:
    print(f"{player_name} won the leg with {successful_shots} shots.")
if command == "Retire":
    print(f"{player_name} retired after {bad_shots} unsuccessful shots.")