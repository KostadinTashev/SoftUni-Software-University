bitcoin_count = int(input())
chinese_count = float(input())
commissions = float(input())
bitcoin_in_leva = bitcoin_count * 1168
chinese_in_leva = chinese_count * 0.15 * 1.76
total_sum_in_euro = (bitcoin_in_leva + chinese_in_leva) / 1.95
commissions_in_euro = commissions / 100 * total_sum_in_euro
total_sum = total_sum_in_euro - commissions_in_euro
print(f"{total_sum:.2f}")