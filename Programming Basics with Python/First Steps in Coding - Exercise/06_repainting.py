nylon = int(input())
paint = int(input())
razr = int(input())
hours_workers = int(input())
sum_nylon = (nylon + 2 ) * 1.50
sum_paint = (paint + 1.10 ) * 14.50
sum_razr = razr * 5.00
total_sum = sum_nylon + sum_paint + sum_razr + 0.40
sum_workers = (total_sum * 0.3) * hours_workers
finally_sum = total_sum + sum_workers
print(finally_sum)
