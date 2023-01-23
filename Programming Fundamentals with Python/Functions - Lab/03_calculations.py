def calculator(num_1, num_2):
    if operator == "multiply":
        return num_1 * num_2
    elif operator == "divide":
        return num_1 // num_2
    elif operator == "add":
        return num_1 + num_2
    elif operator == "subtract":
        return num_1 - num_2


operator = input()
num_1 = int(input())
num_2 = int(input())
result = calculator(num_1, num_2)
print(result)

# operator = input()
# first_num = int(input())
# second_num = int(input())
#
# def solve(first_num, second_num, operator):
#     result = None
#     if operator == "multiply":
#         return first_num * second_num
#     elif operator == "divide":
#         return first_num // second_num
#     elif operator == "add":
#         return first_num + second_num
#     elif operator == "subtract":
#         return first_num - second_num
#     return result
