w = float(input())
h = float(input())

w_cm = w * 100
h_cm = h * 100

rows = w_cm // 120
available_width = h_cm - 100
cols = available_width // 70

total_seats = rows * cols
final_seats = int(total_seats - 3)
print(final_seats)
