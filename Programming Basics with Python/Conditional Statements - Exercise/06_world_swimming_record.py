import math

record_in_seconds = float(input())
distance = float(input())
time_in_sec_for_one = float(input())

total_time = distance * time_in_sec_for_one
resistance_time = math.floor(distance / 15) * 12.5
total_time = total_time + resistance_time

if total_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diff = total_time - record_in_seconds
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
