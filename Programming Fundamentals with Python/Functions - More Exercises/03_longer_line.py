from math import floor


def center_point(x1, y1, x2, y2, x3, y3, x4, y4):

    x1_y1 = abs(x1) + abs(y1)
    x2_y2 = abs(x2) + abs(y2)
    x3_y3 = abs(x3) + abs(y3)
    x4_y4 = abs(x4) + abs(y4)
    first_2_point_sum = x1_y1 + x2_y2
    second_2_point_sum = x3_y3 + x4_y4

    if first_2_point_sum >= second_2_point_sum:
        if x2_y2 < x1_y1:
            print(f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})')
        else:
            print(f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})')
    else:
        if x4_y4 < x3_y3:
            print(f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})')
        else:
            print(f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})')

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())
center_point(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4)