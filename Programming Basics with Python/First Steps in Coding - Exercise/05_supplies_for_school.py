pen = int(input())
markers = int(input())
liter_detergent = int(input())
percent_discount = int(input())
total_pen = pen * 5.80
total_markers = markers * 7.20
total_detergent = liter_detergent * 1.20
sum_of_supplies = total_pen + total_markers + total_detergent
final_sum = sum_of_supplies - (sum_of_supplies * (percent_discount / 100))
print(final_sum)
