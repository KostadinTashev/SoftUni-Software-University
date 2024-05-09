deposit = float(input())
months = int(input())
annual_rate = float(input())

per_year = deposit * (annual_rate / 100)
per_month = per_year / 12
total_sum = deposit + (months * per_month)
# result = deposit + months ((deposit * annual_rate)/12)

print(total_sum)
