import datetime

today = datetime.date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)

today = datetime.datetime.now()

print(today)
print(today.hour)
print(today.minute)
print(today.second)

tomorrow = today + datetime.timedelta(days=1)
print(tomorrow.date())

tzstring = today.astimezone()
print(tzstring.tzinfo)
print(tzstring.tzname())