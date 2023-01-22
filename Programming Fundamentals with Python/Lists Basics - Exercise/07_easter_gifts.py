gifts = input().split()
command = input()

while command != 'No Money':
    command = command.split()
    new_command = command[0]
    gift = command[1]

    if new_command == 'OutOfStock':
        for index in range(len(gifts)):
            if gift in gifts[index]:
                gifts[index] = 'None'

    elif new_command == 'Required':
        for index in range(len(gifts)):
            if index == int(command[2]):
                gifts[index] = command[1]

    elif new_command == 'JustInCase':
        gifts[-1] = gift

    command = input()

while 'None' in gifts:
    gifts.remove('None')

print(' '.join(gifts))