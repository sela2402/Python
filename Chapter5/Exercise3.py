# Ask the user for a month and year, and display all dates that are Mondays.

import calendar
import datetime

# Ask the user to enter the year 
year = int(input("Please enter the year : "))

# Ask the user to enter the month 
month = int(input("Please enter the month(1-12) : "))
name_of_month = calendar.month_name[month]

print("Monday in", name_of_month , year)

for day in range(1, calendar.monthrange(year, month)[1] + 1):
    
    if calendar.weekday(year, month, day) == 0:
        print(f"{year}-{month:02d}-{day:02d}")
