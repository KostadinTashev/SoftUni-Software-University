def tribune(num):
    if num == 1:
        return "1"
    if num == 2:
        return "1"
    if num == 3:
        return "2"

    first_num = 1
    second_num = 1
    third_num = 2

    if num > 3:
        for i in range(4, num + 1):
            current_num = first_num + second_num + third_num
            list.append(str(current_num))
            first_num = second_num
            second_num = third_num
            third_num = current_num
        return " ".join(list)


list = ["1", "1", "2"]
print(tribune(num = int(input())))
