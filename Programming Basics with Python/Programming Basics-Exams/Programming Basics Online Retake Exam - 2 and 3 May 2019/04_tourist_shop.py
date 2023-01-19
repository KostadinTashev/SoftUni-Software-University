budget = float(input())
product = input()
products_count = 0
total_price = 0
while product != "Stop":
    price_product = float(input())
    products_count += 1
    total_price += price_product
    if products_count % 3 == 0:
        total_price -= price_product
        price_product = price_product / 2
        total_price += price_product
    if total_price > budget:
        break
    product = input()

if product == "Stop":
    print(f"You bought {products_count} products for {total_price:.2f} leva.")
diff = abs(total_price - budget)
if total_price > budget:
    print(f"You don't have enough money!")
    print(f"You need {diff:.2f} leva!")
