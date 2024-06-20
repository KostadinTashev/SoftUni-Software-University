start = int(input())
end = int(input())
combination = ""
for i in range(start, end + 1):
    for j in range(start, end + 1):
        for k in range(start, end + 1):
            for l in range(start, end + 1):
                if i > l and (j + k) % 2 == 0:
                    if i % 2 == 0 and l % 2 != 0:
                        print(f"{i}{j}{k}{l}", end=" ")
                    elif i % 2 != 0 and l % 2 == 0:
                        print(f"{i}{j}{k}{l}", end=" ")
