temp = float(input())
if (temp >= 26.00) and (temp <= 35.00):
    print('Hot')
elif (temp >= 20.1) and (temp <= 25.9):
    print('Warm')
elif (temp >= 15.00) and (temp <= 20.00):
    print('Mild')
elif (temp >= 12.00) and (temp <= 14.9):
    print('Cool')
elif (temp >= 5.00) and (temp <= 11.9):
    print('Cold')
else:
    print('unknown')
