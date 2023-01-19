joinery_count = int(input())
type_joinery = input()
delivery = input()
price = 0
if type_joinery == "90X130":
    price = 110 * joinery_count
    if 30 < joinery_count < 60:
        price *= 0.95
    elif joinery_count > 60:
        price *= 0.92
elif type_joinery == "100X150":
    price = 140 * joinery_count
    if 40 < joinery_count < 80:
        price *= 0.94
    elif joinery_count > 80:
        price *= 0.9
elif type_joinery == "130X180":
    price = 190 * joinery_count
    if 20 < joinery_count < 50 :
        price *= 0.93
    elif joinery_count > 50:
        price *= 0.88
elif type_joinery == "200X300":
    price = 250 * joinery_count
    if 25 < joinery_count < 50:
        price *= 0.91
    elif joinery_count > 50:
        price *= 0.86
if delivery == "With delivery":
    price += 60
else:
    price = price
if joinery_count > 99:
    price *= 0.96
    print(f"{price:.2f} BGN")
elif 10 <= joinery_count <= 99:
    print(f"{price:.2f} BGN")
else:
    print("Invalid order")
