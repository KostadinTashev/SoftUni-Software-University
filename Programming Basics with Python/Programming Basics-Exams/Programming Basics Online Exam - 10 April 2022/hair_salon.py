goal_for_day = int(input())
command = input()
earn_money = 0
while command != "closed":
    if command == "haircut":
        command = input()
        if command == "mens":
            earn_money += 15
        elif command == "ladies":
            earn_money += 20
        elif command == "kids":
            earn_money += 10
    elif command == "color":
        command = input()
        if command == "touch up":
            earn_money += 20
        elif command == "full color":
            earn_money += 30
    if earn_money >= goal_for_day:
        break
    command = input()
diff = (goal_for_day - earn_money)
if earn_money >= goal_for_day:
    print(f"You have reached your target for the day!")
    print(f"Earned money: {earn_money}lv.")
else:
    print(f"Target not reached! You need {diff}lv. more.")
    print(f"Earned money: {earn_money}lv.")
