holiday_days = int(input())
holiday_minutes = holiday_days * 127
working_days = ((365 - holiday_days) * 63)
game_minutes = working_days + holiday_minutes
norma = abs(30000 - game_minutes)
h = norma // 60
m = norma % 60
if game_minutes > 30000:
    print("Tom will run away")
    print(f"{h} hours and {m} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")