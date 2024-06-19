loads_count = int(input())
price1 = 0
price2 = 0
price3 = 0
load1 = 0
load2 = 0
load3 = 0
all_load = 0
average_na_ton = 0
for tons in range(1, loads_count + 1):
    current_load = int(input())
    if current_load <= 3:
        load1 += current_load
    elif current_load <= 11:
        load2 += current_load
    elif current_load >= 12:
        load3 += current_load
    all_load = load1 + load2 + load3
    average_na_ton = (load1 * 200 + load2 * 175 + load3 * 120) / (load1 + load2 + load3)
microbus = load1 / all_load * 100
truck = load2 / all_load * 100
train = load3 / all_load * 100
print(f"{average_na_ton:.2f}")
print(f"{microbus:.2f}%")
print(f"{truck:.2f}%")
print(f"{train:.2f}%")
