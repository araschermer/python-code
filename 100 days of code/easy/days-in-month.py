import calendar


def is_leap(year,print_=False):
    """ returns true if year is leap year, otherwise returns False and prints the output per assignment of print_"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:

                if print_: print("Leap year")
                return True
            else:
                if print_: print("Leap yearNot a leap year")
                return False
        else:
            if print_: print("Leap year")
            return True
    else:
        if print_:print("Not a leap year")
        return False


def days_in_month(year, month):
    """returns the number of days in given month of the given year
     for a better visual version of the functionality
     check: https://repl.it/@abdelkha/days-in-month?embed=1&output=1#main.py
     """
    if month > 12 or month < 1 or year < 1:
        return "Invalid input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


def get_month_name(month):
    """gets the month full name from the calendar."""
    # print(calendar.month_abbr[month]) # to print the month appreviated name
    return calendar.month_name[month]


if __name__ == '__main__':
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))

    days = days_in_month(year, month)
    month = get_month_name(month)
    print(f"There are {days} days in {month} of {year}")
