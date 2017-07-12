import datetime
import pytz
local_time=datetime.datetime.now()
utc_time=datetime.datetime.utcnow()
print ("local time  is {}".format(local_time))
print ("utc time is {}".format(utc_time))
aware_local_time=pytz.utc.localize(local_time)
aware_utc_time=pytz.utc.localize(utc_time)
print("aware local time {} timezone {}".format(aware_local_time,aware_local_time.tzinfo))

print("aware local time {} timezone {}".format(aware_utc_time,aware_utc_time.tzinfo))