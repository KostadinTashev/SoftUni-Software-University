minuti_kontrola = int(input())
sekundi_kontrola = int(input())
duljina_metri = float(input())
sekundi_100_metra = int(input())

all_second_kontrola = minuti_kontrola * 60 + sekundi_kontrola
zabavqne = duljina_metri / 120
all_zabavqne = zabavqne * 2.5
vreme_marin = (duljina_metri / 100) * sekundi_100_metra - all_zabavqne
diff = (vreme_marin - all_second_kontrola)
if vreme_marin <= all_second_kontrola:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {vreme_marin:.3f}.")
else:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")