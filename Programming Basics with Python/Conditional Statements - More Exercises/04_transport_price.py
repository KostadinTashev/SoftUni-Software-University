n_kilometers = int(input())
day_night = input()
price = 0
if day_night == "day":
    if n_kilometers < 20:
        price = 0.7 + (n_kilometers * 0.79)
    elif 20 <= n_kilometers < 100:
        price = 0.09 * n_kilometers
    elif n_kilometers >= 100:
        price = 0.06 * n_kilometers
if day_night == "night":
    if n_kilometers < 20:
        price = 0.7 + (n_kilometers * 0.9)
    elif 20 <= n_kilometers < 100:
        price = 0.09 * n_kilometers
    elif n_kilometers >= 100:
        price = 0.06 * n_kilometers

print(f"{price:.2f}")