import datetime
import time
a = datetime.datetime.now()
# datetime module and time

class color:
    RED = '\033[91m'
    END = '\033[0m'
# Ignore this, i'm still working on it.

print ("Welcome to xLuxella's Python Clock")
print ("Press CTRL+C to stop the program.")
time.sleep(2)
# introduction and steps on how to stop program

while (True):
    print ("The time is now:")
    print (time.strftime("%c"))
    time.sleep(1)
# infinite loop with delay of 1 second, can be adjusted in time.sleep(N) for different intervals.
