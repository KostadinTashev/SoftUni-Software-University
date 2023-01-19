import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_one_meter = float(input())
seconds = distance_in_meters * time_for_one_meter
delay = (math.floor((distance_in_meters / 50)) * 30)
total_time = seconds + delay
diff = abs(total_time - record_in_seconds)
if record_in_seconds <= total_time:
    print(f"No! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
