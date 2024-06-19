import sys

n = int(input())
oddSum = 0
oddMin = sys.maxsize
oddMax = -sys.maxsize
evenSum = 0
evenMin = sys.maxsize
evenMax = -sys.maxsize
for i in range(1, n + 1):
    num = float(input())

    if i % 2 == 0:
        evenSum += num

        if num > evenMax:
            evenMax = num

        if num < evenMin:
            evenMin = num

    else:
        oddSum += num

        if num > oddMax:
            oddMax = num

        if num < oddMin:
            oddMin = num

print(f"OddSum={oddSum:.2f},")
if oddMin != sys.maxsize:
    print(f"OddMin={oddMin:.2f},")

else:
    print("OddMin=No,")

if oddMax != -sys.maxsize:
    print(f"OddMax={oddMax:.2f},")

else:
    print("OddMax=No,")

print(f"EvenSum={evenSum:.2f},")
if evenMin != sys.maxsize:
    print(f"EvenMin={evenMin:.2f},")

else:
    print(f"EvenMin=No,")

if evenMax != -sys.maxsize:
    print(f"EvenMax={evenMax:.2f}")

else:
    print("EvenMax=No")
