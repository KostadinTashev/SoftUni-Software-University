def character(first_string, second_string):
    collected_characters = []
    for current_character in range(ord(first_string) + 1, ord(second_string)):
        collected_characters.append(chr(current_character))

    return collected_characters


first_char = input()
second_char = input()
result = character(first_char, second_char)
# print(" ".join(result))
print(*result, sep=" ")
