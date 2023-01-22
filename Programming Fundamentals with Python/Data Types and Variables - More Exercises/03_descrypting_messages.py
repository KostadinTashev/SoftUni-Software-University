key = int(input())
number = int(input())
for letters in range(number):
    current_letter = input()
    letter_in_int = ord(current_letter)
    result_in_int = letter_in_int + key
    result_in_chr = chr(result_in_int)
    print(result_in_chr, end="")