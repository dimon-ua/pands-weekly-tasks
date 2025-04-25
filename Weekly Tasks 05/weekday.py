# Importing datetime module
import datetime

# creating a list with working days
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# datetime.datetime.now() will output a date in a format 2025-04-25 15:14:37.751113
# to get a day but its name we need to add strftime("%A") method with %A argument to get the weekday - Monday, Tuesday, etc
today_day = datetime.datetime.now().strftime("%A")

# if/else statment, if Mon-Fri is in weekdays list. This is workday
if today_day in weekdays:
    print("Yes, unfortunately today is a weekday.")
    # if not, weekday
else:
    print("It is the weekend, yay!")
