airline_name = input()
adult_tickets = int(input())
kid_tickets = int(input())
price_for_adult_ticket = float(input())
price_for_kid_ticket = price_for_adult_ticket * 0.3

price_for_service = float(input())
price_for_one_adult_ticket = price_for_adult_ticket + price_for_service
price_for_one_kid_ticket = price_for_kid_ticket + price_for_service
total_price_for_adults = adult_tickets * price_for_one_adult_ticket
total_price_for_kid = kid_tickets * price_for_one_kid_ticket
total_price = total_price_for_kid + total_price_for_adults
profit = 0.2 * total_price
print(f"The profit of your agency from {airline_name} tickets is {profit:.2f} lv.")