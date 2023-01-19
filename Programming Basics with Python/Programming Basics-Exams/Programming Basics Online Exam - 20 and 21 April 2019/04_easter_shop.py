eggs_count = int(input())
command = input()
fill_eggs = 0
sold_eggs = 0
while command != "Close":
    buy_or_fill_eggs = int(input())
    if command == "Buy":
        eggs_count -= buy_or_fill_eggs
        sold_eggs += buy_or_fill_eggs
    if eggs_count < 0:
        eggs_count += buy_or_fill_eggs
        sold_eggs -= buy_or_fill_eggs
        break
    elif command == "Fill":
        eggs_count += buy_or_fill_eggs
        fill_eggs += buy_or_fill_eggs
    command = input()
if command == "Close":
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")
else:
    print("Not enough eggs in store!")
    print(f"You can buy only {eggs_count}.")