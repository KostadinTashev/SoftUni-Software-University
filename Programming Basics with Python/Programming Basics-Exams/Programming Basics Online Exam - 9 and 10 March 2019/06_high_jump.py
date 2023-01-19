wanted_high = int(input())
current_high = wanted_high - 30

total_jumps = 0
failed = False
failed_jumps = 0

while not failed:
    jump = int(input())
    total_jumps = total_jumps + 1

    if jump <= current_high:
        failed_jumps = failed_jumps + 1
        if failed_jumps == 3:
            failed = True
    else:
        if current_high >= wanted_high:
            break
        current_high = current_high + 5
        failed_jumps = 0

if not failed:
    print(f"Tihomir succeeded, he jumped over {current_high}cm after {total_jumps} jumps.")
else:
    print(f"Tihomir failed at {current_high}cm after {total_jumps} jumps.")