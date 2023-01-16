juniors = int(input())
seniors = int(input())
route = input()
price = 0
all_bikers = juniors + seniors

if route == "trail":
    price = juniors * 5.50 + (seniors * 7)
elif route == "cross-country":
    if all_bikers >= 50:
        price = ((juniors * 8) + (seniors * 9.50)) * 0.75
    else:
        price = (juniors * 8) + (seniors * 9.50)
elif route == "downhill":
    price = juniors * 12.25 + (seniors * 13.75)
elif route == "road":
    price = juniors * 20 + (seniors * 21.50)

new_price = price * 0.95
print(f"{new_price:.2f}")
