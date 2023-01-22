number_of_snowballs = int(input())
max_value = 0

weight = 0
time = 0
quality = 0
for balls in range(1, number_of_snowballs + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = int((snowball_weight / snowball_time) ** snowball_quality)

    if value > max_value:
        max_value = value
        weight = snowball_weight
        time = snowball_time
        quality = snowball_quality

print(f"{weight} : {time} = {max_value} ({quality})")

