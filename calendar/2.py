import calendar

cal = calendar.TextCalendar(6)

str = cal.formatmonth(2077, 1)
print(str)

for i in cal.itermonthdays(2027, 4):
    print(i)