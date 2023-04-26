# Python program to Find day of the week for a given date

import re  # regular expressions
import calendar  
import datetime  


def process_date(user_input):
    user_input = re.sub(r"/", " ", user_input)  # substitute / with space
    user_input = re.sub(r"-", " ", user_input)  # substitute - with space
    return user_input


def find_day(date):
    born = datetime.datetime.strptime(
        date, "%d %m %Y"
    ).weekday()  # this statement returns an integer corresponding to the day of the week
    return calendar.day_name[
        born
    ]  


# get the input from the user
print("Enter the date you want to check in format 1 2 2023 or 1/2/2023 or 1-2-2023")
user_input = str(input("Enter date     "))
date = process_date(user_input)
print("Day on " + user_input + "  is " + find_day(date))