length = int(input())
width = int(input())
height = int(input())
percetage = float(input())

volume = length * width * height
volume_liter = volume / 1000
final_liter = volume_liter * (1-(percetage/100))
print(final_liter)