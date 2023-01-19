desired_profit = float(input())
sum_price = 0
command = input()
while command != "Party!":
    name_cocktail = command
    cocktail_count = int(input())
    price = len(name_cocktail)
    sum = price * cocktail_count
    if sum % 2 != 0:
        sum *= 0.75
        sum_price += sum
    else:
        sum_price += sum
    if sum_price >= desired_profit:
        break

    command = input()
if command == "Party!":
    print(f"We need {desired_profit - sum_price:.2f} leva more.")
elif sum_price >= desired_profit:
    print("Target acquired.")
print(f"Club income - {sum_price:.2f} leva.")