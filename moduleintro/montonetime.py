
import time
#from time import monotonic as my_timer
from time import process_time as my_timer
import random

print (time.clock())

input("press enter to start")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("press enter to stop")
end_time = my_timer()
print("strat time" + time.strftime('%X', time.localtime(start_time)))

print("end time" + time.strftime('%X', time.localtime(end_time)))

print("reaction time is {}". format(end_time - start_time))