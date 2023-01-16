count_groups = int(input())

musala_count = 0
monblan_count = 0
kilimanjora_count = 0
k2_count = 0
everest_count = 0
all_people = 0
for i in range(1, count_groups + 1):
    count_people = int(input())
    all_people = all_people + count_people

    if count_people <= 5:
        musala_count = musala_count + count_people
    elif count_people <= 12:
        monblan_count = monblan_count + count_people
    elif count_people <= 25:
        kilimanjora_count = kilimanjora_count + count_people
    elif count_people <= 40:
        k2_count = k2_count + count_people
    else:
        everest_count = everest_count + count_people
musala_percent = musala_count / all_people * 100
monblan_percent = monblan_count / all_people * 100
kilimanjora_percent = kilimanjora_count / all_people * 100
k2_percent = k2_count / all_people * 100
everest_count = everest_count / all_people * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimanjora_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_count:.2f}%")
