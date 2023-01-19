eggs_count = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_eggs = 0
max_color = ""
for color in range (eggs_count):
    current_color = input()
    if current_color == "red":
        red_eggs += 1
    elif current_color == "orange":
        orange_eggs += 1
    elif current_color == "blue":
        blue_eggs += 1
    elif current_color == "green":
        green_eggs += 1

max_eggs = max(red_eggs,orange_eggs, blue_eggs, green_eggs)
if max_eggs == red_eggs:
    max_color = "red"
elif max_eggs == orange_eggs:
    max_color = "orange"
elif max_eggs == blue_eggs:
    max_color = "blue"
elif max_eggs == green_eggs:
    max_color = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {max_color}")