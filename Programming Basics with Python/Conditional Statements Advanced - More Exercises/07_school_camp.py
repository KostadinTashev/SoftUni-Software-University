season = input()
group_type = input()
student = int(input())
night_stay = int(input())
price = 0
sport = ""

if season == "Winter":
    if group_type == "boys":
        sport = "Judo"
        price = student * 9.60 * night_stay
    elif group_type == "girls":
        sport = "Gymnastics"
        price = student * 9.60 * night_stay
    elif group_type == "mixed":
        sport = "Ski"
        price = student * 10 * night_stay
elif season == "Spring":
    if group_type == "boys":
        sport = "Tennis"
        price = student * 7.20 * night_stay
    elif group_type == "girls":
        sport = "Athletics"
        price = student * 7.20 * night_stay
    elif group_type == "mixed":
        sport = "Cycling"
        price = student * 9.50 * night_stay
elif season == "Summer":
    if group_type == "boys":
        sport = "Football"
        price = student * 15 * night_stay
    elif group_type == "girls":
        sport = "Volleyball"
        price = student * 15 * night_stay
    elif group_type == "mixed":
        sport = "Swimming"
        price = student * 20 * night_stay

if student >= 50:
    price = price * 0.5
elif 20 <= student < 50:
    price = price * 0.85
elif 10 <= student < 20:
    price = price * 0.95

print(f"{sport} {price:.2f} lv.")
