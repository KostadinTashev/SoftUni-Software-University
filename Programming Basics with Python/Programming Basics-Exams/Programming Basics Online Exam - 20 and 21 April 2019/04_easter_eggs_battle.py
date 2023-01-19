first_player_eggs = int(input())
second_player_eggs = int(input())
first_win = 0
second_win = 0
winner = input()
while winner != "End":
    if winner == "one":
        first_win += 1
        second_player_eggs -= 1
    elif winner == "two":
        second_win += 1
        first_player_eggs -= 1
    if first_player_eggs == 0 or second_player_eggs == 0:
        break
    winner = input()
if first_player_eggs == 0:
    print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
elif second_player_eggs == 0:
    print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
if winner == "End":
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")