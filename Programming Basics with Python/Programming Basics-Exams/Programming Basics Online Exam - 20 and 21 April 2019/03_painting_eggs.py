egg_size = input()
color_egg = input()
batch = int(input())
total_price = 0
if egg_size == "Large":
    if color_egg == "Red":
        total_price = batch * 16
    elif color_egg == "Green":
        total_price = batch * 12
    elif color_egg == "Yellow":
        total_price = batch * 9
elif egg_size == "Medium":
    if color_egg == "Red":
        total_price = batch * 13
    elif color_egg == "Green":
        total_price = batch * 9
    elif color_egg == "Yellow":
        total_price = batch * 7
elif egg_size == "Small":
    if color_egg == "Red":
        total_price = batch * 9
    elif color_egg == "Green":
        total_price = batch * 8
    elif color_egg == "Yellow":
        total_price = batch * 5
discount = total_price * 0.35
total_price = total_price - discount
print(f"{total_price:.2f} leva.")