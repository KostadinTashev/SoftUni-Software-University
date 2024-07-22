budget = float(input())
price_for_kilo_flour = float(input())
price_for_pack_eggs = 0.75 * price_for_kilo_flour
price_for_liter_milk = 1.25 * price_for_kilo_flour
bread_price = price_for_kilo_flour + price_for_pack_eggs + price_for_liter_milk * 0.25

loaves = 0
colored_eggs = 0

while budget >= bread_price:
    loaves += 1
    budget -= bread_price
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= (loaves - 2)

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
