location_count = int(input())
for current_location in range(location_count):
    average_yield = float(input())
    days_for_location = int(input())
    total_gold= 0
    for current_days in range(days_for_location):
        extract_kg = float(input())
        total_gold += extract_kg
    average_extract_gold = total_gold / days_for_location
    diff = abs(average_extract_gold - average_yield)
    if average_extract_gold >= average_yield:
        print(f"Good job! Average gold per day: {average_extract_gold:.2f}.")
    else:
        print(f"You need {diff:.2f} gold. ")