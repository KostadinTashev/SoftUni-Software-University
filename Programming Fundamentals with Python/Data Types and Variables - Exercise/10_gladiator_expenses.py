lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0
second_shield = 0
for time in range(1, lost_fights_count + 1):
    if time % 2 == 0:
        broken_helmet += 1
    if time % 3 == 0:
        broken_sword += 1
    if time % 2 == 0 and time % 3 == 0:
        broken_shield += 1
        second_shield += 1
    if second_shield > 1 and second_shield % 2 == 0:
        broken_armor += 1
        second_shield = 0
price_for_helmet = broken_helmet * helmet_price
price_for_sword = broken_sword * sword_price
price_for_shield = broken_shield * shield_price
price_for_armor = broken_armor * armor_price
expenses = price_for_helmet + price_for_sword + price_for_shield + price_for_armor
print(f"Gladiator expenses: {expenses:.2f} aureus")