import calendar

if(calendar.isleap(2024)):
    print('2024 is leap year')
else:
    print('2024 is not leap year')

print(calendar.firstweekday()) #0 is Monday

print(calendar.leapdays(1996,2024))

print(calendar.weekday(2024,1,18))