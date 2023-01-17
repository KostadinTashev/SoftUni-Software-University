poor_grades = int(input())

grades_count = 0
sum_grades = 0
last_problem = ""
count_poor_grades = 0
has_failed = False
input_line = input()
while input_line != "Enough":
    grade = int(input())
    if grade <= 4:
        count_poor_grades += 1

    last_problem = input_line

    grades_count = grades_count + 1
    sum_grades = sum_grades + grade

    if poor_grades == count_poor_grades:
        has_failed = True
        break
    input_line = input()
if has_failed:
    print(f"You need a break, {count_poor_grades} poor grades.")
else:
    average_grades = sum_grades / grades_count
    print(f"Average score: {average_grades:.2f}")
    print(f"Number of problems: {grades_count}")
    print(f"Last problem: {last_problem}")
