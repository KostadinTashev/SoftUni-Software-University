import math

raketa_cena = float(input())
raketa_count = int(input())
maratonki_count = int(input())

all_cena_raketa = raketa_cena * raketa_count
all_cena_maratonki = (raketa_cena / 6) * maratonki_count
cena_ostanata_ekip = 0.2 * (all_cena_raketa + all_cena_maratonki)
total_cena = all_cena_raketa + all_cena_maratonki + cena_ostanata_ekip
cena_djo = total_cena / 8
cena_sponsor = total_cena - cena_djo

print(f"Price to be paid by Djokovic {math.floor(cena_djo)}")
print(f"Price to be paid by sponsors {math.ceil(cena_sponsor)}")
