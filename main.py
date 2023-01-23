
#/usr/bin/python3

def getYear():
    """Returns an integer value between 1800-2099, inclusive, or -1."""

def leapYear(year):
    """Returns True if provided year a leap year, otherwise returns False."""

def dayOfWeekJan1(year, leap_year):
    """Returns the day of the week for January 1 of the provided year.
       year must be between 1800 and 2099. leap_year must be True if year a leap year, and False otherwise.
    """

def numDaysInMonth(month_num, leap_year):
    """Returns the number of days in a given month.
       month_num must be in the range 1-12, inclusive.
       leap_year must be True if month in a leap year, otherwise False.
    """

def constructCalMonth(month_num, first_day_of_month, num_days_in_month):
    """Returns a formatted calendar month for display on the screen.
       month_num must be in the range 1-12, inclusive.
       first_day_of_month must be in the range 0-6 (1-Sun, 2-Mon, ..., 0-Sat).
       Returns a list of strings of the form,
       [month_name, week1, week2, week3, week4, week5, week6].
    """

def constructCalYear(year):
    """Returns a formatted calendar year for display on the screen.
       year must be in the range 1800-2099, inclusive.
       Returns a list of list of strings of the form,
       [year, month1, month2, month3, ..., month12].
    """

def displayCalendar(calendar_year):
    """Displays the provided calendar_year on the screen three months across.
       Provided calendar year should be in the form of a list of twelve sublists, in which each sublist is of the form [monthname, week1, week2, ..., ]
    """

# main
terminate = False

print("This program will display a calendar year for a given year")

while not terminate:
    year = getYear()

    if year == -1:
        terminate = True
    else:
        calendar_year = constructCalYear(year)
        displayCalendar(calendar_year)