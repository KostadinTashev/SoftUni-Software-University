number = int(input())
total_sum = 0
for letter in range(number):
    current_letter = input()
    letter_in_int = ord(current_letter)
    total_sum += letter_in_int
print(f"The sum equals: {total_sum}")
