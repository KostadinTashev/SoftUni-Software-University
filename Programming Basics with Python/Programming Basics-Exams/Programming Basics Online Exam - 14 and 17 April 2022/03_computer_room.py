month = input()
hours = int(input())
people_in_group = int(input())
day_or_night = input()
price_for_one_person = 0
total_price = 0
if day_or_night == "day":
    if month == "march" or month == "april" or month == "may":
        price_for_one_person = 10.50
    elif month == "june" or month == "july" or month == "august":
        price_for_one_person = 12.60
elif day_or_night == "night":
    if month == "march" or month == "april" or month == "may":
        price_for_one_person = 8.40
    elif month == "june" or month == "july" or month == "august":
        price_for_one_person = 10.20
if people_in_group >= 4:
    price_for_one_person *= 0.9
if hours >= 5:
    price_for_one_person *= 0.5
total_price = price_for_one_person * people_in_group * hours
print(f"Price per person for one hour: {price_for_one_person:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")