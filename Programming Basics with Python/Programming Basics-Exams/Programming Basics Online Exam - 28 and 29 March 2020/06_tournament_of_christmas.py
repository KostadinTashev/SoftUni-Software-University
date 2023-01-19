total_days = int(input())
total_money = 0
days_won = 0
days_lost = 0
for day in range(total_days):
    daily_won_games = 0
    daily_lost_games = 0
    daily_money = 0
    command = input()
    while command != "Finish":
        win_or_lose = input()
        if win_or_lose == "win":
            daily_money += 20
            daily_won_games += 1
        elif win_or_lose == "lose":#else
            daily_lost_games += 1
        command = input()
    if daily_won_games > daily_lost_games:
        daily_money *= 1.10
        days_won += 1
    else:
        days_lost += 1
    total_money += daily_money
if days_won > days_lost:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")