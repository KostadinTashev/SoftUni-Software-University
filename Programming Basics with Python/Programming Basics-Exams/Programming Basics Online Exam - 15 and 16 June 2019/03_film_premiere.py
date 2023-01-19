film_name = input()
packet_for_film = input()
ticket_count = int(input())
total_price = 0
if film_name == "John Wick":
    if packet_for_film == "Drink":
        total_price = ticket_count * 12
    elif packet_for_film == "Popcorn":
        total_price = ticket_count * 15
    elif packet_for_film == "Menu":
        total_price = ticket_count * 19
elif film_name == "Star Wars":
    if packet_for_film == "Drink":
        total_price = ticket_count * 18
    elif packet_for_film == "Popcorn":
        total_price = ticket_count * 25
    elif packet_for_film == "Menu":
        total_price = ticket_count * 30
    if ticket_count >= 4:
        total_price *= 0.7
elif film_name == "Jumanji":
    if packet_for_film == "Drink":
        total_price = ticket_count * 9
    elif packet_for_film == "Popcorn":
        total_price = ticket_count * 11
    elif packet_for_film == "Menu":
        total_price = ticket_count * 14
    if ticket_count == 2:
        total_price *= 0.85
print(f"Your bill is {total_price:.2f} leva.")

