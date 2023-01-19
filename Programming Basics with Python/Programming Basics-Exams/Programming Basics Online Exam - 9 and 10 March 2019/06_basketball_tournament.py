tournament_name = input()
wins_count = 0
loses_count = 0
while tournament_name != "End of tournaments":
    match_count = int(input())
    for current_match in range(1, match_count + 1):
        points_for_team_dessy = int(input())
        points_for_opponents_team = int(input())
        diff = abs(points_for_team_dessy - points_for_opponents_team)
        if points_for_team_dessy > points_for_opponents_team:
            wins_count += 1
            print(f"Game {current_match} of tournament {tournament_name}: win with {diff} points.")
        else:
            loses_count += 1
            print(f"Game {current_match} of tournament {tournament_name}: lost with {diff} points.")
    tournament_name = input()
percentage_wins = wins_count / (wins_count + loses_count) * 100
percentage_loses = loses_count / (wins_count + loses_count) * 100
print(f"{percentage_wins:.2f}% matches win")
print(f"{percentage_loses:.2f}% matches lost")

