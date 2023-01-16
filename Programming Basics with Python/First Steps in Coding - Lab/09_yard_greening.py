yard_area = float(input())
price = yard_area * 7.61
final_price = price * (100-18) / 100 #price * 0.82
discount = price * 18/100
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
