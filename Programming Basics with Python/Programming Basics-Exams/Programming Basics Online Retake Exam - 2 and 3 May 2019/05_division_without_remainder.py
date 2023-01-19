numbers = int(input())
multiple_of_two = 0
multiple_of_three = 0
multiple_of_four = 0
for n in range(numbers):
    current_number = int(input())
    if current_number % 2 == 0:
        multiple_of_two += 1
    if current_number % 3 == 0:
        multiple_of_three += 1
    if current_number % 4 == 0:
        multiple_of_four += 1
percent_multiple_of_two = multiple_of_two / numbers * 100
percent_multiple_of_three = multiple_of_three / numbers * 100
percent_multiple_of_four = multiple_of_four / numbers * 100
print(f"{percent_multiple_of_two:.2f}%")
print(f"{percent_multiple_of_three:.2f}%")
print(f"{percent_multiple_of_four:.2f}%")