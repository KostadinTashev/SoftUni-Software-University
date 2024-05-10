x = float(input())
y = float(input())
h = float(input())

predna = x * x * 2 - (1.2 * 2)
stranichna = x * y * 2 - (1.5 * 1.5 * 2)
obshto = predna + stranichna
green_paint = obshto / 3.4

pokriv = x * y * 2
triagnle = 2 * (x * h / 2)
pokriv_obshto = pokriv + triagnle
red_paint = pokriv_obshto / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
