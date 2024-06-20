men = int(input())
women = int(input())
tables = int(input())
counter = 0
couples = ''
for i in range(1, men + 1):
    for j in range(1, women + 1):
        counter += 1
        couples += f"({i} <-> {j}) "
        if counter == tables:
            break
    if counter == tables:
        break
print(couples)
