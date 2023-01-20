years_of_person = input()
adults_count = 0
kids_count = 0
money_for_toys = 0
money_for_sweaters = 0
while years_of_person != 'Christmas':
    years_of_person = int(years_of_person)
    if years_of_person <= 16:
        kids_count += 1
        money_for_toys += 5
    elif years_of_person > 16:
        adults_count += 1
        money_for_sweaters += 15
    years_of_person = input()
print(f"Number of adults: {adults_count}")
print(f"Number of kids: {kids_count}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")
