v_liter = int(input())
p1_for_hour = int(input())
p2_for_hour = int(input())
worker_hour = float(input())

p1_liter = p1_for_hour * worker_hour
p2_liter = p2_for_hour * worker_hour
all_piper_fill = p1_liter + p2_liter
all_fill_percentage = all_piper_fill / v_liter * 100
p1_percentage = p1_liter / all_piper_fill * 100
p2_percentage = p2_liter / all_piper_fill * 100
diff = (all_piper_fill - v_liter)
if all_piper_fill <= v_liter:
    print(f"The pool is {all_fill_percentage:.2f}% full. Pipe 1: {p1_percentage:.2f}%. Pipe 2: {p2_percentage:.2f}%.")
else:
    print(f"For {worker_hour:.2f} hours the pool overflows with {diff:.2f} liters.")