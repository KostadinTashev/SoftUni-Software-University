N = float(input())
M = float(input())
veg = int(input())
fr = int(input())
sum_veg = veg * N
sum_fr = fr * M
sum = (sum_veg + sum_fr) / 1.94
print(f"{sum:.2f}")