import calendar

print(calendar.month(2024, 1))

print(calendar.calendar(2024))

for m in calendar.Calendar().monthdayscalendar(2024,5):
    print(m)

textCal = calendar.TextCalendar()

width = 4
linespacing = 2

print(textCal.formatmonth(2024,1,width,linespacing))