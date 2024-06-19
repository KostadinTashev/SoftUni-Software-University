count = int(input())
previous_sum = int(input()) + int(input())
max_difference = 0

for i in range(count - 1):
    currentSum = int(input()) + int(input())

    if abs(previous_sum - currentSum) > max_difference:
        max_difference = abs(previous_sum - currentSum)

    previous_sum = currentSum

if max_difference == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_difference}")
