film_name = input()
days_count = int(input())
ticket_count = int(input())
ticket_price = float(input())
percentage_for_cinema = int(input())

price_ticket_for_day = ticket_count * ticket_price
price_for_whole_period = price_ticket_for_day * days_count
price_for_cinema = price_for_whole_period * percentage_for_cinema / 100
price_for_film = price_for_whole_period - price_for_cinema
print(f"The profit from the movie {film_name} is {price_for_film:.2f} lv.")