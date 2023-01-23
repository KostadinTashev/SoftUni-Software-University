def sign(num_1, num_2, num_3):
    negative_sign = 0
    if num_1 < 0:
        negative_sign += 1
    if num_2 < 0:
        negative_sign += 1
    if num_3 < 0:
        negative_sign += 1
    if num_1 == 0 or num_2 == 0 or num_3 == 0:
        return "zero"
    if negative_sign % 2 != 0:
        return "negative"
    return "positive"


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(sign(first_num, second_num, third_num))