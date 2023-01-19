import math

tour_count = int(input())
start_points = int(input())
total_points = start_points
win_points = 0
win_tour = 0
for tour in range (tour_count):
    stage = input()
    if stage == "W":
        total_points += 2000
        win_points += 2000
        win_tour += 1
    elif stage == "F":
        total_points += 1200
        win_points += 1200
    elif stage == "SF":
        total_points += 720
        win_points += 720
average_points = win_points / tour_count
percentage_win_tour = win_tour / tour_count * 100
print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percentage_win_tour:.2f}%")
