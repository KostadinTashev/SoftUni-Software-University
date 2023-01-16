budget = float(input())
season = input()
price = 0
location = ""
place = ""
if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = 0.45 * budget
elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60
elif budget > 3000:
    place = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.9

print(f"{location} - {place} - {price:.2f}")