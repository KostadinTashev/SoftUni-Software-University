film_name = input()
total_ticket = 0
student_ticket = 0
standard_ticket = 0
kid_ticket = 0

while film_name != "Finish":
    empty_places = int(input())
    busy_places = 0
    for i in range(empty_places):
        ticket = input()
        if ticket == "student":
            student_ticket += 1
        elif ticket == "standard":
            standard_ticket += 1
        elif ticket == "kid":
            kid_ticket += 1
        elif ticket == "End":
            break
        total_ticket += 1
        busy_places += 1
    percent_fullness = busy_places / empty_places * 100
    total_ticket = standard_ticket + student_ticket + kid_ticket
    print(f"{film_name} - {percent_fullness:.2f}% full.")

    film_name = input()

print(f"Total tickets: {total_ticket}")
print(f"{(student_ticket / total_ticket) * 100:.2f}% student tickets.")
print(f"{(standard_ticket / total_ticket) * 100:.2f}% standard tickets.")
print(f"{(kid_ticket / total_ticket) * 100:.2f}% kids tickets.")

