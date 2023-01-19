film_name = input()
type_hall = input()
ticket_count = int(input())
all_price = 0
if type_hall == "normal":
    if film_name == "A Star Is Born":
        all_price = ticket_count * 7.50
    elif film_name == "Bohemian Rhapsody":
        all_price = ticket_count * 7.35
    elif film_name == "Green Book":
        all_price = ticket_count * 8.15
    elif film_name == "The Favourite":
        all_price = ticket_count * 8.75
elif type_hall == "luxury":
    if film_name == "A Star Is Born":
        all_price = ticket_count * 10.50
    elif film_name == "Bohemian Rhapsody":
        all_price = ticket_count * 9.45
    elif film_name == "Green Book":
        all_price = ticket_count * 10.25
    elif film_name == "The Favourite":
        all_price = ticket_count * 11.55
elif type_hall == "ultra luxury":
    if film_name == "A Star Is Born":
        all_price = ticket_count * 13.50
    elif film_name == "Bohemian Rhapsody":
        all_price = ticket_count * 12.75
    elif film_name == "Green Book":
        all_price = ticket_count * 13.25
    elif film_name == "The Favourite":
        all_price = ticket_count * 13.95
print(f"{film_name} -> {all_price:.2f} lv.")