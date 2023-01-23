from math import floor


def center_point(x1, y1, x2, y2):
    first_point_sum = abs(x1) + abs(y1)
    second_point_sum = abs(x2) + abs(y2)

    if first_point_sum <= second_point_sum:
        print(f'({floor(x1)}, {floor(y1)})')
    else:
        print(f'({floor(x2)}, {floor(y2)})')


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
center_point(x_1, y_1, x_2, y_2)