people_asses = int(input())

input_line = input()
all_grades_sum = 0
count_grades = 0
while input_line != "Finish":
    presentation = input_line

    sum = 0
    for i in range(1, people_asses + 1):
        current_grade = float(input())
        count_grades += 1
        all_grades_sum = all_grades_sum + current_grade
        sum = sum + current_grade

    avg_grade_current = sum / people_asses
    print(f"{presentation} - {avg_grade_current:.2f}.")

    input_line = input()

total_avg_grade = all_grades_sum / count_grades
print(f"Student's final assessment is {total_avg_grade:.2f}.")