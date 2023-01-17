bottle_of_detergent = int(input())
dishes_count = 0
pots_count = 0
command = input()
loading = 0
total_detergent = bottle_of_detergent * 750
spent_detergent = 0
while command != "End":
    vessels = int(command)
    loading += 1
    if loading % 3 == 0:
        spent_detergent += vessels * 15
        pots_count += vessels
    else:
        spent_detergent += vessels * 5
        dishes_count += vessels
    if total_detergent < spent_detergent:
        print(f"Not enough detergent, {spent_detergent - total_detergent} ml. more necessary!")
        break
    command = input()
diff = abs(total_detergent - spent_detergent)
if command == "End":
    print("Detergent was enough!")
    print(f"{dishes_count} dishes and {pots_count} pots were washed.")
    print(f"Leftover detergent {diff} ml.")



