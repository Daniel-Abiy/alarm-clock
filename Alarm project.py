from playsound import playsound

import time
clear = "\033[2J"
clear_and_return = "\033[H"

hours = int(input("The amount of hours: "))
minute = int(input("The amound of minute: "))
Seconds = int(input("The anount of seconds: "))
total_time = hours * 60 * 60 + minute * 60 + Seconds

print(clear)
def alarm(total_time):
    time_elapsed = 0

    while time_elapsed < total_time:
        time.sleep(1)
        time_elapsed += 1

        time_left = total_time - time_elapsed 
        hours_left = time_left // 3600
        minute_left = (time_left % 3600) // 60
        seconds_left = time_left % 60

        print(clear_and_return)
        print(f"The Alarm will sound in:{hours_left:02d}:{minute_left:02d}:{seconds_left:02d}")




alarm(total_time)

playsound("./alarm.mp3")