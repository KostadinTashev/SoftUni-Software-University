student_count = int(input())
less_than_3 = 0
more_than_3 = 0
more_than_4 = 0
more_than_5 = 0
average = 0
for grade in range(1, student_count + 1):
    grade = float(input())
    if 2 <= grade <= 2.99:
        less_than_3 += 1
    elif 3 <= grade <= 3.99:
        more_than_3 += 1
    elif 4 <= grade <= 4.99:
        more_than_4 += 1
    elif 5 <= grade <= 6:
        more_than_5 += 1
    average += grade / student_count
fail_percent = less_than_3 / (less_than_3 + more_than_3 + more_than_4 + more_than_5) * 100
poor_percent = more_than_3 / (less_than_3 + more_than_3 + more_than_4 + more_than_5) * 100
good_percent = more_than_4 / (less_than_3 + more_than_3 + more_than_4 + more_than_5) * 100
very_good_percent = more_than_5 / (less_than_3 + more_than_3 + more_than_4 + more_than_5) * 100
print(f"Top students: {very_good_percent:.2f}%")
print(f"Between 4.00 and 4.99: {good_percent:.2f}%")
print(f"Between 3.00 and 3.99: {poor_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average:.2f}")
