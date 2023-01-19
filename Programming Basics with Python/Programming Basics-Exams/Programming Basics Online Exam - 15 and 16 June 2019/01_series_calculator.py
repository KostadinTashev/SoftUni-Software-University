import math

serial_name = input()
season_count = int(input())
episode_count = int(input())
episode_time = float(input())
ad_time = episode_time * 0.2
all_time_episode = episode_time + ad_time
add_time_special_episode = season_count * 10
all_time_for_serial = all_time_episode * episode_count * season_count + add_time_special_episode
print(f"Total time needed to watch the {serial_name} series is {math.floor(all_time_for_serial)} minutes.")
