team_name = input()
games_count = int(input())
total_points = 0
wins_count = 0
draws_count = 0
lose_count = 0
for current_game in range(games_count):
    result = input()
    if result == "W":
        total_points += 3
        wins_count += 1
    elif result == "D":
        total_points += 1
        draws_count += 1
    else:
        total_points = total_points
        lose_count += 1
    wins_percent = wins_count / games_count * 100
if games_count == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    print(f"{team_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins_count}")
    print(f"## D: {draws_count}")
    print(f"## L: {lose_count}")
    print(f"Win rate: {wins_percent:.2f}%")
