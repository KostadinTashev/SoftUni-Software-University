fina_sector = input()
first_sector_row = int(input())
seats_odd_row = int(input())
cnt = 0
start_sector = 65
start_seat = 97
for sector in range(start_sector, ord(fina_sector) + 1):
    for row in range(1, first_sector_row + 1):
        if row % 2 != 0:
            for seats in range(start_seat, (start_seat + seats_odd_row)):
                print(f'{chr(sector)}{row}{chr(seats)}')
                cnt += 1
        elif row % 2 == 0:
            for seats in range(start_seat, (start_seat + seats_odd_row + 2)):
                print(f'{chr(sector)}{row}{chr(seats)}')
                cnt += 1
    if first_sector_row + 1 > first_sector_row:
        first_sector_row += 1

print(cnt)
