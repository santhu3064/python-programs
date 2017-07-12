# import time
# print(time.time())
# print(time.ctime())
# print(time.localtime())
# print(time.altzone)
# print(time.asctime())
# print(time.gmtime())
#
# tm_here=time.localtime()
# print(tm_here)
# print ("year",tm_here[0],tm_here.tm_year )
#
import time
from time import time as my_timer
import random

input("press enter to start")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("press enter to stop")
end_time = my_timer()
print("strat time" + time.strftime('%X', time.localtime(start_time)))

print("end time" + time.strftime('%X', time.localtime(end_time)))

print("reaction time is {}". format(end_time - start_time))
