clients_count = int(input())
price_for_all_clients = []
for current_client in range(1, clients_count + 1):
    total_price = 0

    products = 0
    text = input()
    while True:
        if text == "Finish":
            if products % 2 == 0:
                total_price *= 0.8
                price_for_all_clients.append(total_price)
            else:
                price_for_all_clients.append(total_price)
            print(f"You purchased {products} items for {total_price:.2f} leva.")
            break
        elif text == "basket":
            total_price += 1.50
            products += 1
        elif text == "wreath":
            total_price += 3.80
            products += 1
        elif text == "chocolate bunny":
            total_price += 7
            products += 1
        text = input()
for price in price_for_all_clients:
    average_price = sum(price_for_all_clients) / len(price_for_all_clients)
    print(f"Average bill per client is: {average_price:.2f} leva.")
    break
