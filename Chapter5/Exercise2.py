# Ask the user to enter a month and year, and count how many Saturdays are in that month.

import calendar

# Ask the user to enter the year
year = int(input("Enter the year : "))

# Ask the user to enter the month
month = int(input("Ebter the month (1-12) : "))

month_celander = calendar.monthcalendar(year, month)

saturday = sum(1 for week in month_celander if week[5] != 0)

# print the result
print(f"The total numebr of the Saturday in August", year , "is", saturday)

