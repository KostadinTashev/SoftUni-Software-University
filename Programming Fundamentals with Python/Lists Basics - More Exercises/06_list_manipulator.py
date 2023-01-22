number = [int(num) for num in input().split()]
command = input()
while command != "end":
    command = command.split()
    current_command = command[0]
    if current_command == "exchange":
        index = int(command[1])
        if 0 <= index <= len(number):
            left_part = number[:index:]
            right_part = number[index::]

        else:
            print("Invalid index")
    elif current_command == "max":
        pass
    elif current_command == "min":
        pass
    elif current_command == "first":
        pass
    elif current_command == "last":
        pass
    command = input()
    print(left_part)
    print(right_part)
