import math

hours = int(input())
day = int(input())
workers_overwork = int(input())

work = ((day * 0.9) * 8)
hours_overwork = workers_overwork * (2 * day)
all_hours = work + hours_overwork
diff = abs(all_hours - hours)
if all_hours >= hours:
    print(f"Yes!{math.floor(diff)} hours left.")
else:
    print(f"Not enough time!{math.ceil(diff)} hours needed.")
