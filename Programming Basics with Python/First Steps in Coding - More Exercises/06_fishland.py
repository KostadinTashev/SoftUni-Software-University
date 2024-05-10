price_mackerel = float(input())
price_sprinkle = float(input())
kg_pal = float(input())
kg_saf = float(input())
kg_midi = int(input())

price_pal = price_mackerel * 1.60
sum_pal = kg_pal * price_pal

price_saf = price_sprinkle * 1.8
sum_saf = kg_saf * price_saf

sum_midi = kg_midi * 7.50
finally_sum = sum_pal + sum_saf + sum_midi
print(f"{finally_sum:.2f}")
