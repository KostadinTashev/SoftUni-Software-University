number_lines = int(input())
capacity = 255
water_counter = 0
for liter in range(number_lines):
    current_liter = int(input())
    if capacity - current_liter < 0:
        print("Insufficient capacity!")
        continue
    water_counter += current_liter
    capacity -= current_liter
print(water_counter)
