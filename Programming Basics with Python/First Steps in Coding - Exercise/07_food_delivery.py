chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

sum_chicken_menu = chicken_menu * 10.35
sum_fish_menu = fish_menu * 12.40
sum_veg_menu = veg_menu * 8.15

total_sum = sum_chicken_menu + sum_fish_menu + sum_veg_menu
desert = total_sum * 0.2
finally_sum = total_sum + desert + 2.50
print(finally_sum)