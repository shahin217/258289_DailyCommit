year = int(input("Input a year: "))
month = int(input("Input a month [1-12]: "))
day = int(input("Input a day [1-31]: "))

if year % 400 == 0:
    leap_year = True

elif year % 100 == 0:
    leap_year = False

elif year % 4 == 0:
    leap_year = True

else:
    leap_year = False

if 1 <= month <= 12:
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31

    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    elif month in (4, 6, 9, 11):
        month_length = 30
else:
    print("Invalid month")
    month_length = 0

if 1 <= day <= 31:
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

else:
    print("Invalid day")
    day = 0
    year = 0
if month_length != 0 and day != 0 and year != 0:
    print("The next date is  %d-%d-%d." % (day, month, year))
