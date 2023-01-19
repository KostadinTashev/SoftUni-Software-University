rent = int(input())
statuetki = rent - (rent * 0.30)
ketaring = statuetki - (statuetki * 0.15)
muzika = ketaring * 0.5
all_money = rent + statuetki + ketaring + muzika
print(f"{all_money:.2f}")