visitor_count = int(input())
back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
work_out_count = 0
protein_shake = 0
protein_bar = 0
protein_count = 0
for visitor in range(visitor_count):
    activity = input()
    if activity == "Back":
        back_count += 1
        work_out_count += 1
    elif activity == "Chest":
        chest_count += 1
        work_out_count += 1
    elif activity == "Legs":
        legs_count += 1
        work_out_count += 1
    elif activity == "Abs":
        abs_count += 1
        work_out_count += 1
    elif activity == "Protein shake":
        protein_shake += 1
        protein_count += 1
    elif activity == "Protein bar":
        protein_bar += 1
        protein_count += 1
percentage_work_out = work_out_count / visitor_count * 100
percentage_protein = protein_count / visitor_count * 100
print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{percentage_work_out:.2f}% - work out")
print(f"{percentage_protein:.2f}% - protein")