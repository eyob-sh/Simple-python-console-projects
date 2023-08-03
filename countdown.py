import time

inputtime = input("enter time in the form of HH:MM:SS")
inputtime = [int(i) for i in inputtime.split(":")]
sec = [3600, 60, 1]
timesec = sum([inputtime[i]*sec[i] for i in range(len(inputtime))])

while timesec:
    mins, secs = divmod(timesec, 60)
    timer = "{:02d} : {:02d}".format(mins, secs)
    print(timer)
    time.sleep(1)
    timesec -= 1

print("done")
