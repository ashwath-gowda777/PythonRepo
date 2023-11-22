import calendar

def day_name(month, day, year):
    ans = calendar.weekday(year, month, day)
    return calendar.day_name[ans].upper()