def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


def add_and_subtract(first, second, third):
    sum_of_first_and_second_integers = sum_numbers(first, second)
    result = subtract(sum_of_first_and_second_integers, third)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))

# def sum_numbers(num_1, num_2):
#     result = num_1 + num_2
#     return result
#
#
# def subtract(num_1, num_2,  num_3):
#     return num_1 + num_2 - num_3
#
#
# first_num = int(input())
# second_num = int(input())
# third_num = int(input())
# print(subtract(first_num, second_num, third_num))
