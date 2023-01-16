chrysanthemums_count = int(input())
rose_count = int(input())
tulips_count = int(input())
season = input()
holiday = input()
price = 0
all_flowers = chrysanthemums_count + rose_count + tulips_count

if season == "Spring":
    if holiday == "N":
        price = chrysanthemums_count * 2 + rose_count * 4.10 + tulips_count * 2.50
    elif holiday == "Y":
        price = (chrysanthemums_count * 2 + rose_count * 4.10 + tulips_count * 2.50) * 1.15
    if tulips_count > 7:
        price = price * 0.95
elif season == "Summer":
    if holiday == "N":
        price = chrysanthemums_count * 2 + rose_count * 4.10 + tulips_count * 2.50
    elif holiday == "Y":
        price = (chrysanthemums_count * 2 + rose_count * 4.10 + tulips_count * 2.50) * 1.15
elif season == "Autumn":
    if holiday == "N":
        price = chrysanthemums_count * 3.75 + rose_count * 4.50 + tulips_count * 4.15
    elif holiday == "Y":
        price = (chrysanthemums_count * 3.75 + rose_count * 4.50 + tulips_count * 4.15) * 1.15
elif season == "Winter":
    if holiday == "N":
        price = chrysanthemums_count * 3.75 + rose_count * 4.50 + tulips_count * 4.15
    elif holiday == "Y":
        price = (chrysanthemums_count * 3.75 + rose_count * 4.50 + tulips_count * 4.15) * 1.15
    if rose_count > 9:
        price = price * 0.9
if all_flowers > 20:
    price = price * 0.8

price += 2
print(f"{price:.2f}")
