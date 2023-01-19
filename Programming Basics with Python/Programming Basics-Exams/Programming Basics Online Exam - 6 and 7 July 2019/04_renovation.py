import math

height = int(input())
width = int(input())
percent_no_boil = int(input())
walls = height * width * 4
area = int(math.ceil(walls - (walls * percent_no_boil / 100)))
command = input()
while command != "Tired!":
    area -= int(command)
    if area <= 0:
        break
    command = input()
if area > 0:
    print(f"{area} quadratic m left.")
elif area == 0:
    print(f"All walls are painted! Great job, Pesho!")
else:
    print(f"All walls are painted and you have {abs(area)} l paint left!")
