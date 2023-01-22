number = int(input())
positive = []
negative = []
positive_count = 0
negative_sum = 0
for _ in range(number):
    current_num = int(input())
    if current_num >= 0:
        positive.append(current_num)
        positive_count += 1
    else:
        negative.append(current_num)
        negative_sum += current_num
print(positive)
print(negative)
print(f"Count of positives: {positive_count}")
print(f"Sum of negatives: {negative_sum}")