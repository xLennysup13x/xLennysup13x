# Creating Variables
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

# example 

# Assigning the value "lenny" to the variable named 'name'
name = "lenny"
# Assigning the value "lenny" to the variable named 'name'
name = "lenny"
# Printing the value of the variable 'name'
print(name)

x = 4 # x is of type int 
x = "lenny" # x is now type str
print(x)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(3) # x will be '3'
y = int(3) # y will be '3'
z = float(3) # z will be 3.0

# print's the x/y/z
print(x)
print(y)
print(z)

# Get the Type
# You can get the data type of a variable with the type() function.

# Python Data Types
# Built-in Data Types
# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

# Text Type: str

# Numeric Types: int, float, complex

# Sequence Types: list, tuple, range

# Mapping Type: dict

# Set Types: set, frozenset

# Boolena Type: bool

# Binary Types: bytes, bytearray, memoryview

# None Type: NoneType

x = 5 
y = "lenny"

# print's the type x/y
print(type(x))
print(type(y))

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes:

x = "lenny"

# print's x = "lenny"
print(x)

# is the same as 

x = 'lenny'

# print's x = 'lenny'
print(x)

# Case-Sensitive
# Variable names are case-sensitive.

# Example
# this will create two variables:

a = 4
A = "lenny"
# aw will not overwrite a 

# print the 4 / "lenny"
print(A)
print(a)

# Variable Names

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )

# Python Keywords

# Keyword:	  Description:
# and	      A logical operator
# as	      To create an alias
# assert      For debugging
# break	      To break out of a loop
# class	      To define a class
# continue	  To continue to the next iteration of a loop
# def	      To define a function
# del	      To delete an object
# elif	      Used in conditional statements, same as else if
# else	      Used in conditional statements
# except	  Used with exceptions, what to do when an exception occurs
# False	      Boolean value, result of comparison operations
# finally	  Used with exceptions, a block of code that will be executed no matter if there is an exception or not
# for	      To create a for loop
# from	      To import specific parts of a module
# global	  To declare a global variable
# if	      To make a conditional statement
# import	  To import a module
# in	      To check if a value is present in a list, tuple, etc.
# is	      To test if two variables are equal
# lambda	  To create an anonymous function
# None	      Represents a null value
# nonlocal	  To declare a non-local variable
# not	      A logical operator
# or	      A logical operator
# pass	      A null statement, a statement that will do nothing
# raise	      To raise an exception
# return	  To exit a function and return a value
# True	      Boolean value, result of comparison operations
# try	      To make a try...except statement
# while	      To create a while loop
# with	      Used to simplify exception handling
# yield	      To end a function, returns a generator

# Example
# Legal variable names:

myvar = "lenny"
my_var = "lenny"
_my_var = "lenny"
myVar = "lenny"
MYVAR = "lenny"
myvar2 = "lenny"

# Print's  myvar/my_var/_my_var/myVar/MYVAR/myvar2

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# Example 
# Illegal variable neame's: 

2myvar ="lenny"
my-var = "lenny"  # sytax Error <-------> code line '157'! 
my var = "lenny"

# This exampple we produce an error in the result

# note: Remeber that variable names are case-sensitive!

# Variable names with more than one word can be diffcult to read.
#There are several Techniques you can make them more readable:

# Camel case 
# Each word, except the frist, start's with a capital letter:

myVariableName = "lenny"

# print the 'myVariablename' then get 'value name'.
print(myVariableName)

# Pascal Case.
# Each word starts with a cappital letter:

MyVariableName = "lenny"
# print the <------> 'myVariablename' <------> then get <------>  'value name'.
print(MyVariableName)

# Snake Case 
# Each word is separated by an undersocre charcter:

my_variable_name = "lenny"
# print's the <------> ('my_variable_name' + "name") <------> ('lenny'). 
print(my_variable_name)

# Python Variables - Assign Multiple Values.
# python allow you to assign values to mutiple variables in one line:

# Example 

x, y, z = "Orange", "Banana", "Cherry"
#print's <-----> the x/y/z <---> "Orange", "Banana", "Cherry"!
print(x)
print(y)
print(z)

# Note: Make sure the number of variable matches the number of values, or else you will get error.

#One Value to Multiple Variables.
# And you can assign the same value to multiple variables in one line.

# Example 

x = y = z = "Orange" # <----> sytax Error code line 208 + 210 + 211 + 212
print(x) # print's the x
print(y) # print's the y
print(z) # print's the z

# Unpack a Collection 
# If you have a collection of values in list, tuple etc. Python allow you to extract the values into variables. This is 

# Example 
# Unpack a list:

# fruits = ["apple","Banana","cherry"]
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  
print(y) # print's <---> 'x', 'y', 'z', <--->  
print(z) 

# Learn more about unpacking in our Unpack Tuples Chapter.

# Python - Unpack Tuples!

# Unpacking a Tuple
# when we create a tuple, we normally assign values to it. This called "packing" a tuple:

# Example 
# packing a tuple:
fruits = ("apple", "banana" , "cherry") # fruit , name's <---->  'apple' , 'banana' 'cherry'!!!
print(fruits) # print's <----> 'value data name's'!!!

# But in Python, we are also allowed to extract the values the valies back into variables. The is called "unpacking":

# Example 
#Unpacking a tuple:

fruits = ("apple", "banana","cherry")
#this line is value which has the. 'value name = fruits'
(green, yellow , red ) =  fruits

print(green)
print(yellow) # Print's  <----> The 'green,yellow,red'
print(red)

# Note: The number of variable must match the number of 
# values in the tuple, if not you must use 
# an asterisk to collect 
# the remainging values as a list.

# Using Asterisk*

# If the Number of variables is less than the number of values, you can add an * to variable name and the
# values will be assigned to the variable as a list:

# Example 
# add a list of values the 'tropic' variable:
# Assign the rest of the values as list called 'red':

fruits = ("apple","mango","papaya","pinapple","cherry")
#this line is value which has the. 'value name = fruits'
(green, *tropic, red) = fruits 

print(green)
print(tropic) # Print's  <----> The 'green,yellow,red'
print(red)

# Python - Output Variables
#The Python print() function is often used to output variables.

# Example 

# print's 'Python is awesome!
x = "Python is awesome!"
print(x) # prints 'x'

# In the print() function, you output multiple variables, separted by a comma:

# Example 

x = "Python"
y = "is"        # value character's
z = "aswome"

print(x, y, z ) # print's x/y/z

# You can aslo  use the  + opeator to output multiple variables:

# Note: Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome"

# for numbers, the + chracter works as a mathematical operator:

# Example:

# print's the value 'x = y'
x = 5  
y = 10 

print(x + y) # print's 'x/y' <---> 5/10

# In the print() function, when you try to combine a string and number with the  + operator, Python will give you 
# an error:

# Example:

x = 5  # !!!! syntax error code!!! | TypeError: unsupported operand type(s) for +: 'int' and 'str'
y = "lenny"
#print's the data value name's  x/y' to get back.
print(x + y)

# The best way to output Multiple variables in the print() function is to separate them with commas, which even
# support diffent data types:

# Examples:

x = 5  # print's the value  '5'!
y = "lenny" # print's the value 'lenny'!
 
print(x , y) # print 'x/y'

# Python - Global Variables

# Global Variables 
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

# Example: 

# Create a variable outside of a function, use iit inside the function
 
# print's the 'awesome' , 
#then takes the x 
#to move on to inside the box which is 'Python is' 
x = "awesome"

def myfunc():
    print("Python is" + x)

myfunc() 

# IF you create a variable with same inside a function, this variable will be local, and can be used inside the function. The function. The global variable withe the same.
# name will remain as it was, global and with the original value.

# Example 
# Create a variable inside a function, with the same name as the global variable
 
x = "awesome" # print's 'the 'awesome'!

def myfunc():
    x = "fantastic"  # print's the 'fantastic' 
    print("Python is" + x) # print's the 'Python is'

myfunc()

print("Python is " + x) # print's the 'fantastic'  and 'x'!

# The global Keyword
# Normally,when you create a variable inside function, that variable is local and can only be used inside function.
# to create a global varialble inside a funtion, you can use the global keyword.

# Example
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
    global x 
    x = "fanstastic" # print's the x menaing x 'x' <---> print's the following 'fanstastic'

myfunc()

print("Python is "+ x) # print's 'Python is' and then the x which print's 'fanstastic'
 
# Als, use the global key word if you want to change a global variable inside a function.

# Example:
# To change the value of a global variable inside a function, refe to the variable by useing the global keyword:

x = "awesome" # print's 'awesome'

def myfunc():
    global x 
    x = "fabtstic" # print's 'fabtstic'

myfunc()
print("Python is" + x) # print's  'Python is'

# Python - Variable Exercises

# Test Yourself With Exercises 
# Now you have learned a lot about variable, and how to use them in Python.
# Are you ready for test?
# Try to inser the missing part to make the code work as expected: