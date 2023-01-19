time_for_photos = int(input())
scene_count = int(input())
scene_time = int(input())
preparation_field = time_for_photos * 0.15
time_for_scene = scene_count * scene_time
all_time = preparation_field + time_for_scene
diff = abs(time_for_photos - all_time)
if all_time > time_for_photos:
    print(f"Time is up! To complete the movie you need {round(diff)} minutes.")
else:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
