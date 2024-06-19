month = int(input())
total_electricity = 0
total_water = 0
total_internet = 0
total_others = 0
average_price = 0
for current_month in range(month):
    electricity = float(input())
    water = 20
    internet = 15
    others = (electricity + water + internet) * 1.2
    total_electricity += electricity
    total_water += water
    total_internet += internet
    total_others += others
average_price = (total_electricity + total_water + total_internet + total_others) / month
print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {average_price:.2f} lv")
