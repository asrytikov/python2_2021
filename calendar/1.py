import calendar

while True:
    year = int(input("Year:"))
    month = int(input("Month:"))
    if month>=1 and month<=12:
        cal = calendar.TextCalendar(0)
        str = cal.formatmonth(year, month)
        print(str)
        break
    if month<1 or month>12:
        print("Text again")