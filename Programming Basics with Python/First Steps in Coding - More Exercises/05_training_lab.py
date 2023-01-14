w = float(input())
h = float(input())

h_seats = (h-1) // 0.7
w_seats = w / 1.2
work_places = w_seats * h_seats - 3
num = int(work_places)
print(num)

