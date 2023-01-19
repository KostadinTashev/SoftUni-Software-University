n = int(input())

print(f"+{' -' * (n - 2)} +")

for rows in range(n - 2):
   print(f"|{' -' * (n - 2)} |")

print(f"+{' -' * (n - 2)} +")