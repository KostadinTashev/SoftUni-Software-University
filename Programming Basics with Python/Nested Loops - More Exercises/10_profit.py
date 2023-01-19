one_lev_coins = int(input())
two_lev_coins = int(input())
five_lev_coins = int(input())
suma = int(input())

for one in range(0, one_lev_coins + 1):
    for two in range(0, two_lev_coins + 1):
        for five in range(0, five_lev_coins + 1):
            if (one * 1) + (two * 2) + (five * 5) == suma:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {suma} lv.")
