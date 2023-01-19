import sys

film_count = int(input())
max_rating = - sys.maxsize
min_rating = sys.maxsize
sum_rating = 0
all_rating = 0
max_film = ""
min_film = ""
for current_film in range(film_count):
    current_film_name = input()
    rating_film = float(input())
    sum_rating += 1
    all_rating += rating_film
    if rating_film > max_rating:
        max_rating = rating_film
        max_film = current_film_name
    elif rating_film < min_rating:
        min_rating = rating_film
        min_film = current_film_name
average_rating = all_rating / sum_rating

print(f"{max_film} is with highest rating: {max_rating}")
print(f"{min_film} is with lowest rating: {min_rating}")
print(f"Average rating: {average_rating:.1f}")
