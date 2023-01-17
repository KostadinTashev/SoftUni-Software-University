width = int(input())
length = int(input())

total_pieces = width * length
input_line = input()
while input_line != "STOP":
    current_pieces = int(input_line)

    total_pieces = total_pieces - current_pieces
    if total_pieces <= 0:
        break
    input_line = input()
if total_pieces > 0:
    print(f"{total_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")