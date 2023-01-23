def orders(prod, qua):
    if prod == "coffee":
        return 1.50 * qua
    elif prod == "water":
        return 1.00 * qua
    elif prod == "coke":
        return 1.40 * qua
    elif prod == "snacks":
        return 2.00 * qua


product = input()
quantity = int(input())
print(f"{orders(product, quantity):.2f}")
