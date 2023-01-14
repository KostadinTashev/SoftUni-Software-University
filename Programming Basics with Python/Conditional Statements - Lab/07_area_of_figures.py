from math import pi
type_fig = input()
if type_fig == 'square':
    a = float(input())
    area_squ = a*a
    print(area_squ)
elif type_fig == 'rectangle':
    a = float(input())
    b = float(input())
    area_rec = a*b
    print(area_rec)
elif type_fig == 'circle':
    r = float(input())
    area_cir = pi * r * r
    print(area_cir)
elif type_fig == 'triangle':
    a = float(input())
    h = float(input())
    area_tri = (a * h) / 2
    print(area_tri)
