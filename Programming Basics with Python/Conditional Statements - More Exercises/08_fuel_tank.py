fuel = input()
liter_fuel = float(input())
if liter_fuel >= 25:
    if fuel == "Diesel":
        print(f"You have enough diesel.")
    elif fuel == "Gasoline":
        print(f"You have enough gasoline.")
    elif fuel == "Gas":
        print(f"You have enough gas.")
    else:
        print("Invalid fuel!")
elif liter_fuel < 25:
    if fuel == "Diesel":
        print(f"Fill your tank with diesel!")
    elif fuel == "Gasoline":
        print(f"Fill your tank with gasoline!")
    elif fuel == "Gas":
        print(f"Fill your tank with gas!")
    else:
        print("Invalid fuel!")
