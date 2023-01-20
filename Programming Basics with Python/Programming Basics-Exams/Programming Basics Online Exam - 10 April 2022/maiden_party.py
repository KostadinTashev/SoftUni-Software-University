price_maiden_party = float(input())
message_count = int(input())
rose_count = int(input())
keychain_count = int(input())
caricature_count = int(input())
luck_surprise_count = int(input())

total_things = message_count + rose_count + keychain_count + caricature_count + luck_surprise_count
message_price = message_count * 0.60
rose_price = rose_count * 7.20
keychain_price = keychain_count * 3.60
caricature_price = caricature_count * 18.20
luck_surprise_price = luck_surprise_count * 22
total_price = message_price + rose_price + keychain_price + caricature_price + luck_surprise_price
if total_things >= 25:
    total_price *= 0.65
total_price *= 0.9
diff = abs(total_price - price_maiden_party)
if total_price > price_maiden_party:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
