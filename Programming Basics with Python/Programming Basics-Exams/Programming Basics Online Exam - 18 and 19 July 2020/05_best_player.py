import sys

player_name = input()
best_goals = - sys.maxsize
best_player = ""

while player_name != "END":

    goals = int(input())
    if goals > best_goals:
        best_goals = goals
        best_player = player_name
    if best_goals >= 10:
        break
    player_name = input()

print(f"{best_player} is the best player!")
if best_goals >= 3:
    print(f"He has scored {best_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_goals} goals.")
