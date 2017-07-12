import pytz
import datetime
# country = 'Europe/Moscow'
# tz_to_display=pytz.timezone(country)
# local_time=datetime.datetime.now(tz=tz_to_display)
# print(tz_to_display)
# print(local_time)
# print(datetime.datetime.utcnow())

for x in pytz.country_names:
	print (x)

for x in pytz.country_names:
	print( x + ":" + pytz.country_names[x])

for x in sorted(pytz.country_names):
	print ("{}: {}: {}".format(x,pytz.country_names[x],pytz.country_timezones.get(x)))