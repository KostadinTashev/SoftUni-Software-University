computer_count = int(input())
total_sales = 0
total_rating = 0
for current_model in range(computer_count):
    current_model = int(input())
    rating = current_model % 10
    all_sales = current_model // 10
    if rating == 2:
        all_sales = 0.0 * all_sales
        total_rating += 2
    elif rating == 3:
        all_sales = all_sales * 0.5
        total_sales += all_sales
        total_rating += 3
    elif rating == 4:
        all_sales = all_sales * 0.7
        total_sales += all_sales
        total_rating += 4
    elif rating == 5:
        all_sales = all_sales * 0.85
        total_sales += all_sales
        total_rating += 5
    elif rating == 6:
        all_sales = all_sales * 1
        total_sales += all_sales
        total_rating += 6

print(f"{total_sales:.2f}")
total_rating = total_rating / computer_count
print(f"{total_rating:.2f}")

