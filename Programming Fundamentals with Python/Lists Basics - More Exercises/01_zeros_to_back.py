numbers = input().split(", ")
list_of_numbers = []
zeros = 0
for current_num in numbers:
    list_of_numbers.append(int(current_num))
    if int(current_num) == 0:
        zeros += 1
        list_of_numbers.remove(int(current_num))
for zero in range(1, zeros + 1):
    list_of_numbers.append(zero * 0)
print(list_of_numbers)

