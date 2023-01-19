cena_training_year = int(input())
kecove = cena_training_year * 0.6
ekip = kecove * 0.8
topka = ekip / 4
aksesoari = topka / 5
total_price = cena_training_year + kecove + ekip + topka + aksesoari

print(f"{total_price:.2f}")