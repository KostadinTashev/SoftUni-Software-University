fruit = input()
set_size = input()
set_count = int(input())
total_price = 0
price = 0
if fruit == "Watermelon":
    if set_size == "small":
        price = 2 * 56 * set_count
    elif set_size == "big":
        price = 5 * 28.70 * set_count
elif fruit == "Mango":
    if set_size == "small":
        price = 2 * 36.66 * set_count
    elif set_size == "big":
        price = 5 * 19.60 * set_count
elif fruit == "Pineapple":
    if set_size == "small":
        price = 2 * 42.10 * set_count
    elif set_size == "big":
        price = 5 * 24.80 * set_count
elif fruit == "Raspberry":
    if set_size == "small":
        price = 2 * 20 * set_count
    elif set_size == "big":
        price = 5 * 15.20 * set_count
total_price += price
if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.5
print(f"{total_price:.2f} lv.")
