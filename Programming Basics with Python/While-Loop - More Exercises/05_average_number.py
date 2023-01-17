number = int(input())
total_sum = 0
for n in range(number):
    current_number = int(input())
    total_sum += current_number
average = total_sum / number
print(f"{average:.2f}")