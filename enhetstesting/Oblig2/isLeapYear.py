def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 4000 != 0):
        return True
    else:
        return False