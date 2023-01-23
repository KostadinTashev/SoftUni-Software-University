# def length_is_valid(some_string):
#     if 6 <= len(some_string) <= 10:
#         return True
#     print("Password must be between 6 and 10 characters")
#     return False
#
#
# def symbols_are_valid(some_string):
#     if some_string.isalnum():
#         return True
#     print("Password must consist only of letters and digits")
#     return False
#
#
# def have_at_least_two_digits(some_string):
#     digits_counter = 0
#     for character in some_string:
#         if character.isdigit():
#             digits_counter += 1
#     if digits_counter >= 2:
#         return True
#     print("Password must have at least 2 digits")
#     return False
#
#
# some_password = input()
# validated = [length_is_valid(some_password),\
#              symbols_are_valid(some_password),\
#              have_at_least_two_digits(some_password)]
# if all(validated):
#     print("Password is valid")

def validation(some_string):
    password_is_valid = True
    if len(some_string) < 6 or len(some_string) > 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False

    if not some_string.isalnum():
        print("Password must consist only of letters and digits")
        password_is_valid = False

    digits_counter = 0
    for character in some_string:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False
    return password_is_valid


some_password = input()
validated = validation(some_password)
if validated:
    print("Password is valid")
