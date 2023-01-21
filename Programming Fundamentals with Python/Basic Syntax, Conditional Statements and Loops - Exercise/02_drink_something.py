#Wariant 1 za reshenie
# years = int(input())
# if years <= 14:
#     print("drink toddy")
# elif years <= 18:
#     print("drink coke")
# elif years <= 21:
#     print("drink beer")
# else:
#     print("drink whisky")
#Wariant 2 za reshenie
ages = int(input())
drink_type = ""
if ages <= 14:
    drink_type = "toddy"
elif ages <= 18:
    drink_type = "coke"
elif ages <= 21:
    drink_type = "beer"
else:
    drink_type = "whisky"
print(f"drink {drink_type}")