country = input()
device = input()
points = 0
if device == "ribbon":
    if country == "Russia":
        points = 9.100 + 9.400
    elif country == "Bulgaria":
        points = 9.600 + 9.400
    elif country == "Italy":  # else
        points = 9.200 + 9.500
elif device == "hoop":
    if country == "Russia":
        points = 9.300 + 9.800
    elif country == "Bulgaria":
        points = 9.550 + 9.750
    elif country == "Italy":  # else
        points = 9.450 + 9.350
elif device == "rope":
    if country == "Russia":
        points = 9.600 + 9.000
    elif country == "Bulgaria":
        points = 9.500 + 9.400
    elif country == "Italy":  # else
        points = 9.700 + 9.150
points_to_max = 20 - points
percent_to_max = points_to_max / 20 * 100
print(f"The team of {country} get {points:.3f} on {device}.")
print(f"{percent_to_max:.2f}%")
