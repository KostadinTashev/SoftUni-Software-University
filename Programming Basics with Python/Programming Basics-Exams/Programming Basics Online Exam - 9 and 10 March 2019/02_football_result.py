first_team_wins = 0
first_team_draws = 0
first_team_loses = 0
for result in range(3): #range(1, 3+1)
    current_result = (input())
    first_team_result = int(current_result[0])
    second_team_result = int(current_result[2])
    if first_team_result > second_team_result:
        first_team_wins += 1
    elif first_team_result == second_team_result:
        first_team_draws += 1
    else:
        first_team_loses += 1
print(f"Team won {first_team_wins} games.")
print(f"Team lost {first_team_loses} games.")
print(f"Drawn games: {first_team_draws}")
