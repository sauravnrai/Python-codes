# The task is to find age of the person

from datetime import date

age = int(input("Enter your birth year: "))

current_date = date.today() # will give todays date 

age =  current_date.year - age # we are just selecting the year from the value
print(f'Your age is {age}')