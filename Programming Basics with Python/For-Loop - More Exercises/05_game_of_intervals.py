number_of_moves = int(input())
init_points = 0
between_0_9 = 0
between_10_19 = 0
between_20_29 = 0
between_30_39 = 0
between_40_50 = 0
invalid = 0
sum = 0
for hod in range(number_of_moves):
    current_hod = int(input())
    if 0 <= current_hod <= 9:
        sum += 0.2 * current_hod
        between_0_9 += 1
    elif 10 <= current_hod <= 19:
        sum += 0.3 * current_hod
        between_10_19 += 1
    elif 20 <= current_hod <= 29:
        sum += 0.4 * current_hod
        between_20_29 += 1
    elif 30 <= current_hod <= 39:
        sum += 50
        between_30_39 += 1
    elif 40 <= current_hod <= 50:
        sum += 100
        between_40_50 += 1
    else:
        sum /= 2
        invalid += 1
p1_percent = between_0_9 / number_of_moves * 100
p2_percent = between_10_19 / number_of_moves * 100
p3_percent = between_20_29 / number_of_moves * 100
p4_percent = between_30_39 / number_of_moves * 100
p5_percent = between_40_50 / number_of_moves * 100
p6_percent = invalid / number_of_moves * 100
print(f"{sum:.2f}")
print(f"From 0 to 9: {p1_percent:.2f}%")
print(f"From 10 to 19: {p2_percent:.2f}%")
print(f"From 20 to 29: {p3_percent:.2f}%")
print(f"From 30 to 39: {p4_percent:.2f}%")
print(f"From 40 to 50: {p5_percent:.2f}%")
print(f"Invalid numbers: {p6_percent:.2f}%")
