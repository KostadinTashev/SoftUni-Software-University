numbers = input().split()
removing_numbers = int(input())
deleted_numbers = 0
final_list = []
for current_number in numbers:
    final_list.append(int(current_number))
for i in range(removing_numbers):
    final_list.remove(min(final_list))
print(*final_list, sep=", ")
