first_line = input().split()
second_line = input().split()
third_line = input().split()

first = "1"
second = "2"
if first == first_line[0] and first == first_line[1] and first == first_line[2]:
    print('First player won')
elif first == second_line[0] and first == second_line[1] and first == second_line[2]:
    print('First player won')
elif first == third_line[0] and first == third_line[1] and first == third_line[2]:
    print('First player won')
elif first == first_line[0] and first == second_line[0] and first == third_line[0]:
    print('First player won')
elif first == first_line[1] and first == second_line[1] and first == third_line[1]:
    print('First player won')
elif first == first_line[2] and first == second_line[2] and first == third_line[2]:
    print('First player won')
elif first == first_line[0] and first == second_line[1] and first == third_line[2]:
    print('First player won')
elif first == first_line[2] and first == second_line[1] and first == third_line[0]:
    print('First player won')
elif second == first_line[0] and second == first_line[1] and second == first_line[2]:
    print('Second player won')
elif second == second_line[0] and second == second_line[1] and second == second_line[2]:
    print('Second player won')
elif second == third_line[0] and second == third_line[1] and second == third_line[2]:
    print('Second player won')
elif second == first_line[0] and second == second_line[0] and second == third_line[0]:
    print('Second player won')
elif second == first_line[1] and second == second_line[1] and second == third_line[1]:
    print('Second player won')
elif second == first_line[2] and second == second_line[2] and second == third_line[2]:
    print('Second player won')
elif second == first_line[0] and second == second_line[1] and second == third_line[2]:
    print('Second player won')
elif second == first_line[2] and second == second_line[1] and second == third_line[0]:
    print('Second player won')
else:
    print('Draw!')