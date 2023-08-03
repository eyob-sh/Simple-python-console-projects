import os
import webbrowser
import datetime
import time
if not os.path.isfile("alarm videos.txt"):
    alarmfile = open("alarm videos.txt", "w")
    alarmfile.write("file:///C:/Users/eyobs/Desktop/mov/default.html")

def check(alarm):
    if len(alarm) == 1:
        if 0 <= alarm[0] < 24:
            return True
    elif len(alarm) == 2:
        if 0 <= alarm[0] < 24 and 0 <= alarm[1] < 60:
            return True
    elif len(alarm) == 3:
        if 0 <= alarm[0] < 24 and 0 <= alarm[1] < 60 and 0 <= alarm[2] < 60:
            return True
    return False

while True:
    alarminput = input("input alarm time in the form of HH:MM:SS")
    alarmtime = [int(n) for n in alarminput.split(":")]
    if check(alarmtime):
        break
    else:
        raise Exception("please input time in form of HH:MM:SS format")
seconds = [3600, 60, 1]
alarmtimeseconds = sum(alarmtime[x] * seconds[x] for x in range(len(alarmtime)))

now = datetime.datetime.now()
now = [now.hour, now.minute, now.second]
nowseconds = sum(now[x] * seconds[x] for x in range(len(alarmtime)))

timedif = alarmtimeseconds - nowseconds

if timedif < 0:
    timedif += 86400

print("alarm set to go off at {}".format(timedif))

time.sleep(timedif)
print("wake up")
alarmfile = open("alarm videos.txt", "r")
videos = alarmfile.readline()

webbrowser.open('https://www.wikipedia.com')


