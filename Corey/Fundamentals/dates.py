import datetime
import pytz

d = datetime.date(2016,7,24)
print(d)

tday = datetime.date.today()
print(tday)
print(tday.day)
print(tday.year)
print(tday.month)
print(tday.weekday())
print(tday.isoweekday())

# time deltas
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2
bday = datetime.date(2016,9,15)
till_bday = bday - tday
print(till_bday.days)
print(till_bday.total_seconds())

# datetime.time
t = datetime.time(9,30,45,10000)
print(t)
print(t.hour)


dt = datetime.datetime(2016,9,15,9,30,45,10000)
print(dt)
print(dt.hour)
print(dt.date())
print(dt.time())

tdelta = datetime.timedelta(days=7)
print(dt + tdelta)

tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

# pytz
dt = datetime.datetime(2016,7,26,12,30,45, tzinfo=pytz.utc)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.utc)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
#
# for tz in pytz.all_timezones:
#     print(tz)