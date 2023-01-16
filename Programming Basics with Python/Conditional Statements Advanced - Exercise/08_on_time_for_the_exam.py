exam_hour = int(input())
exam_minute = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam_time_min = (exam_hour * 60) + exam_minute
arrival_time_min = (hour_of_arrival * 60) + minute_of_arrival

diff_min = abs(exam_time_min - arrival_time_min)

if exam_time_min < arrival_time_min:
    print("Late")
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        if minutes < 10:
            print(f"{hour}:0{minutes} hours after the start")
        else:
            print(f"{hour}:{minutes} hours after the start")
    else:
        print(f"{diff_min} minutes after the start")
elif exam_time_min == arrival_time_min or diff_min <= 30:
    print("On time")
    if diff_min >= 1 and diff_min <= 30:
        print(f"{diff_min} minutes before the start")
else:
    print("Early")
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        if minutes < 10:
            print(f"{hour}:0{minutes} hours before the start")
        else:
            print(f"{hour}:{minutes} hours before the start")
    else:
        print(f"{diff_min} minutes before the start")