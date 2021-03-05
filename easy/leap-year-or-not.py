def is_leap_year(year):
    """ calculates  if a given year is a leap year or not
     every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400
     @flow_chart: https://bit.ly/36BjS2D
     @link https://repl.it/@abdelkha/leap-year-calculator?embed=1&output=1#main.py """
    leap_year = f"this year {year} is a Leap year."
    not_leap_year = f"{year} is a Leap year."
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(leap_year)
            else:
                print(not_leap_year)
        else:
            print(leap_year)
    else:
        print(not_leap_year)
