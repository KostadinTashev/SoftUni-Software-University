import math

x = int(input())
y = float(input())
z = int(input())
workers = int(input())

grapes_kg = x * y
vino = (grapes_kg * 0.4) / 2.5
diff = abs(vino - z)
liter_person = diff / workers

if vino < z:
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(vino)} liters.")
    print(f"{math.ceil(diff)} liters left -> {math.ceil(liter_person)} liters per person.")
