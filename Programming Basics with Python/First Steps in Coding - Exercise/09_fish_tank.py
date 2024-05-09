length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = length * width * height
volume_liter = volume / 1000
final_liter = volume_liter * (1 - (percentage / 100))
print(final_liter)
