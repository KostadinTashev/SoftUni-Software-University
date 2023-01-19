rent_of_the_hall = float(input())
bake_price = rent_of_the_hall * 0.2
drinks = bake_price - (bake_price * 0.45)
animation = rent_of_the_hall / 3
total_budget = rent_of_the_hall + bake_price + drinks + animation
print(f"{total_budget:.1f}")
