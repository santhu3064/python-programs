import time
from time import perf_counter
clock_info = time.get_clock_info('clock')
time_info = time.get_clock_info('time')
pref_info = time.get_clock_info('perf_counter')
mono_info = time.get_clock_info('monotonic')
process_info = time.get_clock_info('process_time')
print (clock_info,time_info,pref_info,mono_info,process_info,sep='\n')