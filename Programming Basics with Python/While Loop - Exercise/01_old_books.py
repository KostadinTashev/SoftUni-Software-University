looking_book = input()
is_book_found = False
book_count = 0
input_line = input()
while input_line != "No More Books":
    if input_line == looking_book:
        is_book_found = True
        break
    book_count = book_count + 1
    input_line = input()

if is_book_found:
    print(f"You checked {book_count} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_count} books.")
