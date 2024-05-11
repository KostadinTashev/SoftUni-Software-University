type_flower = input()
count_flowers = int(input())
budget = int(input())

total_sum = 0
if type_flower == "Roses":
    total_sum = 5 * count_flowers
    if count_flowers > 80:
        total_sum = total_sum * 0.9
elif type_flower == "Dahlias":
    total_sum = 3.80 * count_flowers
    if count_flowers > 90:
        total_sum = total_sum * 0.85
elif type_flower == "Tulips":
    total_sum = 2.80 * count_flowers
    if count_flowers > 80:
        total_sum = total_sum * 0.85
elif type_flower == "Narcissus":
    total_sum = count_flowers * 3
    if count_flowers < 120:
        total_sum = total_sum * 1.15
elif type_flower == "Gladiolus":
    total_sum = count_flowers * 2.5
    if count_flowers < 80:
        total_sum = 1.2 * total_sum

diff = abs(budget - total_sum)
if budget >= total_sum:
    print(f"Hey, you have a great garden with {count_flowers} {type_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
