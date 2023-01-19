capacity = int(input())
total_people = 0
space_left = capacity
final_price = 0
while True:
    command = input()
    if command == "Movie time!":
        space_left = space_left - total_people
        print(f"There are {space_left} seats left in the cinema.")
        break
    people = int(command)
    price = people * 5
    if people % 3 == 0:
        price -= 5
    if people > capacity:
        print("The cinema is full.")
        break
    final_price += price
    total_people += people
    capacity -= people
print(f'Cinema income - {final_price} lv.')