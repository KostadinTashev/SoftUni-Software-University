budget = float(input())
videocards_count = int(input())
procesors_count = int(input())
ram_count = int(input())

price_all_videocards = videocards_count * 250
price_procesor = (price_all_videocards * 0.35) * procesors_count
price_ram = (price_all_videocards * 0.1) * ram_count

total_price = price_all_videocards + price_procesor + price_ram

if videocards_count > procesors_count:
    total_price = total_price * 0.85

diff = abs(total_price - budget)
if budget >= total_price :
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")