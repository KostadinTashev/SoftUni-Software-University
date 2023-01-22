numbers = input().split(' ')
string = input()
message = []

for sequence in numbers:
    current_sum = 0
    for i in sequence:
        current_sum += int(i)

    current_sum %= len(string)
    message.append(string[current_sum])
    string = string.replace(string[current_sum], '', 1)
print(''.join(message))
