# Python Boolean's

'''
Booleans represent one of two values: 'True or False'.

Boolean Values
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:
'''
# Example: of the code!

print(10 >  9)
print(10 == 9)
print(10 <  9)

# Note: when you run a conditcom in an if statement, Python returns True or False:


# Example: print a Message bassed on wether the condition is 'True or False':

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluete Values and Variables:
'''
The bool() the function will allow 
you to evalute any value, give you 'True'
 or 'False' in return,
'''
# Exmaple of the a Evaluate of a string and a number
print(bool("hello"))
print(bool)(15)

# For a Example of a Evaluate Two Variables:
x = "Hello lenny"
y = 15

print(bool((x)))
print(bool((y)))

"""
Most of the Values what we put to become True

Almost of the value is Evaluated to 'True' if it has been some of sort of content

and for that any type of string is 'True',  but except empty string's.

and other thing a number is 'True', but not for 0.

for the list tuple, set, and the dictionary are 'true', except empty ones.
"""

# Example of the following code!
# if the following will return 'True':

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# Some of the Values are False.

"""

"""
