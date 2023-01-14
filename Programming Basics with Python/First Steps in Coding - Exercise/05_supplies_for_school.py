pen = int(input())
markers = int(input())
liter_detergent = int(input())
percent_discount = int(input())
total_pen = pen * 5.80
total_markers = markers * 7.20
total_detergent =  liter_detergent * 1.20
sum = total_pen + total_markers + total_detergent
final_sum = sum - (sum*(percent_discount/100))
print(final_sum)