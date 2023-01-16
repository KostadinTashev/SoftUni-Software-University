type_flower = input()
count_flowers = int(input())
budget = int(input())

sum = 0
if type_flower == "Roses":
    sum = 5 * count_flowers
    if count_flowers > 80:
        sum = sum * 0.9
elif type_flower == "Dahlias":
    sum = 3.80 * count_flowers
    if count_flowers > 90:
        sum = sum * 0.85
elif type_flower == "Tulips":
    sum = 2.80 * count_flowers
    if count_flowers > 80:
        sum = sum * 0.85
elif type_flower == "Narcissus":
    sum = count_flowers *  3
    if count_flowers < 120:
        sum = sum *  1.15
elif type_flower == "Gladiolus":
    sum = count_flowers * 2.5
    if count_flowers < 80:
        sum = 1.2 * sum

diff = abs(budget - sum)
if budget >= sum:
    print(f"Hey, you have a great garden with {count_flowers} {type_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")