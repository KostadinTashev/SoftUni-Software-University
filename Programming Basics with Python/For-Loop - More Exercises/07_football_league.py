stadium_capacity = int(input())
fans_count = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
all_fans = 0
for fans in range(fans_count):
    sector = input()
    all_fans += 1
    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1
percentage_fans_in_a = sector_a / fans_count * 100
percentage_fans_in_b = sector_b / fans_count * 100
percentage_fans_in_v = sector_v / fans_count * 100
percentage_fans_in_g = sector_g / fans_count * 100
percentage_all_fans = all_fans / stadium_capacity * 100
print(f"{percentage_fans_in_a:.2f}%")
print(f"{percentage_fans_in_b:.2f}%")
print(f"{percentage_fans_in_v:.2f}%")
print(f"{percentage_fans_in_g:.2f}%")
print(f"{percentage_all_fans:.2f}%")
