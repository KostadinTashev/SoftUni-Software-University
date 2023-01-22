import math
persons = int(input())
capacity = int(input())

courses = math.ceil(persons / capacity)
if persons <= capacity:
    print("All the persons fit inside the elevator.")
    print("Only one course is needed.")
else:
    print(courses)