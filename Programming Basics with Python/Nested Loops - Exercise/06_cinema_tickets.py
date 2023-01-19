input_line = input()
total_count_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
while input_line != "Finish":
    movie = input_line
    capacity = int(input())

    count_tickets_current_movie = 0
    command_line = input()
    while command_line != "End":
        type_ticket = command_line
        if type_ticket == "student":
            student_tickets += 1
        elif type_ticket == "standard":
            standard_tickets += 1
        else:
            kids_tickets += 1

        total_count_tickets += 1
        count_tickets_current_movie += 1
        if count_tickets_current_movie == capacity:
            break
        command_line = input()

    percent_full = count_tickets_current_movie / capacity * 100
    print(f"{movie} - {percent_full:.2f}% full.")

    input_line = input()

print(f"Total tickets: {total_count_tickets}")
percent_student = student_tickets / total_count_tickets * 100
print(f"{percent_student:.2f}% student tickets.")
percent_standard = standard_tickets / total_count_tickets * 100
print(f"{percent_standard:.2f}% standard tickets.")
percent_kid = kids_tickets / total_count_tickets * 100
print(f"{percent_kid:.2f}% kids tickets.")
