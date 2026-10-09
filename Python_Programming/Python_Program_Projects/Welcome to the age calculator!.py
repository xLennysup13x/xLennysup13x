# My Code lenny.
#
# Gets user input
name = input("What's is your name: ")
print("")

# Uses user input to print out information
print("hello " + name + '!' )

from datetime import datetime, timedelta

# Get the current date
now = datetime.now()

# Ask the user for their date of birth
print("Enter your date of birth (YYYY-MM-DD):")
dob_input = input()

# Parse the user's input into a datetime object
birthday = datetime.strptime(dob_input, "%Y-%m-%d")

# Calculate the difference between the current date and the birthday
difference = now - birthday

# Calculate the person's age in years
age_in_years = difference.days // 365

print(f"You are {age_in_years} years old.")
#


# clean UPDATED code!!!
from datetime import datetime, timedelta

def get_user_input():
    print("Welcome to the age calculator!")
    name = input("What's your name: ")
    return name

def get_date_of_birth():
    while True:
        dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
        try:
            return datetime.strptime(dob_input, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")

def calculate_age(birthday, current_date):
    difference = current_date - birthday
    age_in_years = difference.days // 365
    return age_in_years

if __name__ == "__main__":
    name = get_user_input()
    now = datetime.now()
    birthday = get_date_of_birth()

    age = calculate_age(birthday, now)

    if age < 0:
        print("It seems like you entered a future date of birth. Please check and try again.")
    else:
        print(f"Hello {name}! You are {age} years old.")

'''
let's break every line or script by line in a simple term's:

# Gets user input
name = input("What's is your name: ")

This line prompts the user to enter their name, 
and the input is stored in the variable named name.

# Uses user input to print out information
print("hello " + name + '!' )

Here, the line code prints a greeting 
message using the user's name that was entered earlier.

# Uses user input to print out information
print("hello " + name + '!' )

from datetime import datetime, timedelta
This line imports necessary functionality related 
to handling dates and times from the datetime module.

# Get the current date
now = datetime.now()

This line retrieves the current 
date and time and stores it in the variable named now.

# Ask the user for their date of birth
print("Enter your date of birth (YYYY-MM-DD):")
dob_input = input()

The script asks the user to input 
their date of birth in the specified 
format (YYYY-MM-DD), 
and the input is stored in the variable named dob_input.

# Parse the user's input into a datetime object
birthday = datetime.strptime(dob_input, "%Y-%m-%d")

This line converts the user's input 
(date of birth) from a string 
to a datetime object, 
making it easier to work with dates.

# Calculate the difference between the current date and the birthday
difference = now - birthday

The script calculates the time difference 
between the current date and the user's birthday.

# Calculate the person's age in years
age_in_years = difference.days // 365

Using the time difference, the line code  
calculates the person's age in years by dividing the total days by 365.

print(f"You are {age_in_years} years old.")
Finally, the script prints out the calculated age in a user-friendly message.
'''