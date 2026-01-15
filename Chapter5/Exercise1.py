import datetime

date1 = datetime.date(2026, 2, 24)

date2 = date1 - datetime.date.today()

print(date2.days, "day more")