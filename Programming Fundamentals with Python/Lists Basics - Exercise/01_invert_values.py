string = input().split(" ")
list = []
for num in string:
    if int(num) <= 0:
        list.append(abs(int(num)))
    else:
        list.append(-int(num))
print(list)

# list_of_numbers = input().split()
# opposite_numbers = []
# for element in list_of_numbers:
#     opposite_numbers.append(-int(element))
# print(opposite_numbers)