import math

name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
relax_time = break_duration / 4

time_for_episode = break_duration - lunch_time - relax_time

diff = abs(time_for_episode - episode_duration)
if time_for_episode >= episode_duration:
    print(f"You have enough time to watch {name} and left with {math.ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(diff)} more minutes.")