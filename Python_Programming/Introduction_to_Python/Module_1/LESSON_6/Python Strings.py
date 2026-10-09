                    # Example code:

# You can use double or single quotes:
print("hello")
print('hello')

                    # Assign String to a Variable:
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

Variable = "hello"
print(Variable)

                    # Multiline Strings:
# You can assign a mutiline string to a variable by useing three quotes:

 # Example code:
# You can use three double quotes:

Multiline = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(Multiline)

                    # Or three single  quotes:

single = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(single)

# Note's: In the result, the line breaks are inserted at the same postion as in the code.

                    # Strings are Arrays:

'''
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
'''
                    # Example code:
# Get the character at position 1 (remember that the first character has the position 0):

a = "hello world!"
print(a[1])


                    
                    # Looping Through a String:
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

# Example code:
# Loop through the letters in the word "banana":

for x in "banana":
    print(x)


                # Python For Loops
'''
Python For Loops

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
'''

# Example code:
# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

 # The for loop does not require an indexing variable to set beforehand.
  
                # Looping Through a String:
# Even strings are iterable objects, they contain a sequence of characters:\
  
                # Example code:
  
for x in "banana":
   print(x)


                # The break Statement:
# With the 'break' statement we can stop the loop before it has looped through all the items:
   
                    # Example code 1 :
# Exit the loop when x is "banana":
   
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
   
                    # Example code 2 :
# Exit the loop when x is "banana", but this time the break comes before the print:
   
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 


# The continue Statement

# With the continue statement we can stop the current iteration of 
# the loop, and continue with the next:

              # Example of the code:
            # Do not print  a  banana:
  


fruits = ["apple","banana","cherry"]
for x in fruits:
  if x == "banana": # This makes it where you choice to take a word out:
    continue  
  print(x)

"""
The range() Function 

To loop through a set of code a specified number of times, we can use the 
range() as the function,

The range() function retutns a sequence of numbers, starting 4
from 0 by default, and increments by 1 (by default), and ends at a 
specified number.

Example of the code:

Using the range() function:

for x in range(6):
print(x)
"""

                  # Example of the code:

for x in range(6)  # This print's out the from a list to 0 to 5
  print(x)
  
# Note that range(6) is not the values 
#  of 0 to 6, but the values 0 to 5.
  
"""
The range() function defaults to 0 as a 
starting value, however it is 
possible to specify the 
starting value by adding 
a parameter: range(2, 6), 
which means values from 2 to 6 
(but not including 6):
"""

                  # Example of the code 1:

for x in range(2,6):
  print(x) 

# The range() function defaults to 
# increment the sequence by 1, however 
# it is possible to specify the increment 
# value by adding a third parameter: range(2, 30, 3):

                    # Example of the code 2:
for x in range(2,30,3):
  print(x)



                    # Else in For Loop
# The else keyword in a for loop Specifies a block of code to be executed when the loop is finished:

                  # Example of the code 3:
  
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Note: The else block will Not be executed if the loop is stopped by a 'break' statement.
  
# Example of the code 4:
# Break the loop when 'x' is 3, and see what happens when the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

      # If the loop breaks, 
      # the else block is not executed.
  
  
  
            # Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":

  '''
  Example of code 5:
  print each adjective for every fruit:

  This code print's out 

'red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry'
  '''

  adj = ["red", "big", "tasty"]
  fruits = ["apple", "banana", "cherry"]

  for x in adj:
    for y in fruits:
      print(x,y)

'''
The pass Statment

'for' loop's cannot be empty, but if you 
for some reason have to use 'for' loop with no 
content, put in the pass statement
to avoid geting an Error.

for A Example of the code! 

Its going to have empty for loops like this, would raise
an Error without the pass statement
'''

for x in [0, 1, 2]:
  pass

# String Length
# to get length of a string, use the len() function.
# The 'len()' function returns a string:

a = "Hello, world!"
print(len(a))

'''
check String 

to check if a cetain phrase or character is present in 
a string, we can use the keyword 'in'.

# Example of the code 6:
check if 'free' is present in the following text:

which give's us a true which is !!! Boolean !!!
'''

txt = "The best free software app is Visual Studio"
print("free" in txt)


# Using an 'if' statement:

'''
For a Example!
# Print only if "free" is present:
'''


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


'''
Python If ... Else

Python Conditions and If statements

Python supports the usual logical conditions from mathematics:


    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

for Example of the code
# IF statement:
'''

a = 33
b = 200
if b > a:
  print("b is greater than a")

'''
In this Example we use two variables, 'a' and 'b', 
which are used as part of the if statement to test whether
'b' is greater than a. As a is 33, and b is 200, 
we know that 200 is greater than 33, and so we 
print to screen that "b is greater than a".
'''

# Indentation
'''
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming 
languages often use curly-brackets for this purpose. 

# Syntax Error !! 

                            Example:
# If statement, without indentation (will raise an error):
'''

a = 33
b = 200

if b > a:
print("b is greater than a") # # you will get an error # #

"""
Elif
# The 'Elif' is a keyword is Python way of saying "if the previous conditon were not true, then try this conditon".

for a EXAMPLE:
"""

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
 
 '''
 In this example a is equal to b, so the first 
 condition is not true, but the elif 
 condition is true, so we print to 
 screen that "a and b are equal".
 '''

# Else:
# The else keyword catches anything which isn't caught by the preceding conditions.

# Example of code!!
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

"""
In this example 'a' is greater than 'b', so the first condition is not true, also the 'elif' condition is not true, so we go to the 'else' condition and print to screen that "a is greater than b".

You can also have an else without the 'elif':

Example of code:
"""

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

'''
Short Hand If

If you have only one statement to 
execute, you can put it on the 
same line as the if statement.

Example of the code:

# One line if statement:

'if a > b: print("a is greater than b")
'''
a = 200
b = 33

if a > b: print("a is greater than b")


                  # Short Hand If ... Else
# If you have only one statement to execute, 
# one for if, and one for else, you can put it all on the same line:

            # Example of the code:
# One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")

# Note: This Is a technique is Known as Ternary Operators, 
# or Conditional Expressions.

# You can also have multiple else statements on the same line:

# Example: One line if else statement, with 3 condititons:
a = 330 
b = 330 
print("A"if a > b else print("=") if a == b else("B"))

                            #And
'''
The 'and' keyword is a logical operator, and is used to combine conditonal statments:

Example: Test if 'a' is greater than 'b', 'AND' if 'c' is greater than 'a':

  a = 200 
  b = 33 
  c = 500 
  
   if a > b and c > a: 
    print("Both conditions are True")
   
'''

a = 200 
b = 33 
c = 500 
  
if a > b and c > a: 
  print("Both conditions are True")

#                                 Or 

'''
The 'or' keyword is logical operator, and used t combine conditional 
statements:

Example: Test if a is greater than b, OR if a is greater than c:

a = 200 
b = 33 
c =  500 

if a > b or a > c:
  print("At least one of the conditions is True")

'''

a = 200 
b = 33 
c =  500 

if a > b or a > c:
  print("At least one of the conditions is True")
  
# Not 

'''
The not keyword is a logical operator, and is used to 
reverse the result of the conditional statement:

Example: Test if a is NOT greater than b:


a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  
'''

a = 33
b = 200

if not a > b:
  print("a is NOT greater than b")
  
# Nested If

'''
you can have 'if'  statements inside 'if'  
statements, this called nested 'if' statements.

Example: 

x = 41

if x > 10:  
  print("and also above 20!")
   if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.") 
'''

x = 41
if x > 10:  
  print("and also above 20!")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.") 
    
#                         The pass Statement                                    # 


'''
  if statements cannot be empty, but 
  if you for some reason have an 
  if statement with no content,  put in the 
  pass statement to avoid getting an error.    
  
Example: 
       
a = 33
b = 200

if b > a:
  pass

# having an empty if statement like 
# this, would raise an error without the pass statement

'''

a = 33
b = 200

if b > a:
  pass

# having an empty if statement like 
# this, would raise an error without the pass statement



'''
Check if NOT
To check if a certain phrase or character is NOT present
in a string, we can use the keyword not in.

Example: Check if "expensive" is NOT present in the following text: 

txt = "The best things in life are free!"
print("expensive" not in txt)

'''

txt = "The best things in life are free!"
print("expensive" not in txt)

# print's true ✅

                        # Use it in an 'if' statement:
                        
'''
Example: print only if "expensive" is NOT present.

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
'''

# Python - Slicing Strings

# Slicing ! 

'''
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, 

separated by a colon, to return a part of the string.

b = "Hello, World!"
print(b[2:5])

'''

b = "Hello, World!"
print(b[2:5]) 

# print's 'llo'

               # Note: The first character has index 0.
               
               
               
'''
                          Slice From the Start
                        
                    By leaving out the start index, 

              the range will start at the first character:     
              
                             Example
                             
                    Get the characters from 

            the start to position 5 (not included):
            
                        b = "Hello, World!"
                        
                          print(b[:5])
                        
                        #print's 'hello'
'''      

b = "Hello, World!"
print(b[:5])



'''
                            Slice To the End

        By leaving out the end index, the range will go to the end:
        
                              Example
                              
        Get the characters from position 2, and all the way to the end:
        
                           b = "Hello, World!"
                           
                            print(b[2:])
                            
                        #print's 'llo, World!'
'''

'''
                        Negative Indexing
                        
               Use negative indexes to start the
      
               slice from the end of the string:
               
                          Example
                          
                    Get the characters:

              From: "o" in "World!" (position -5)

      To, but not included: "d" in "World!" (position -2):

                    b = "Hello, World!"
                      
                      print(b[-5:-2]
'''

                        # Python - Modify String's 

# Python has set of built - in methods that you can use on sting's.

                          #Upper Case
                            
  #Example: The 'upper()' method returns the string in upper case:
  
a = "Hello, World!"
print(a.upper())

# print's: 'HELLO, WORLD!'.

'''
                                    Lower Case:
                                    
          Example: The lower() method retruns the string in lower case: 
 
                            a = ""hello, world!"
                              print(a.lower))                                   
'''
a = "hello, world!"
print(a.lower)

# Remove  Whitespace

'''
Whitespace is is the space before and/or after the actual text,
and very often you want to remove this space.

Example: The 'strip()'  method removes any whitespace from the beginning or the end:
'''

a = "Hello, World!"
print(a.strip()) # returns "Hello, World!"
                            
                          
#                           Replace String              
'''
                          
                   The replace() method replaces a string with another string:

                        a = "Hello, World!"
                      print(a.replace("H", "J"))  
'''                                           
#                              Example:

'''

                      a = "Hello, World!"
                    print(a.replace("H", "J"))
                    
                          Split String

The split() method returns a list where the 
text between the specified separator becomes the list items.

Example: The split() method splits the string into 
substrings if it finds instances of the separator:
  
                  a = "Hello, World!"
  print(a.split(",")) # returns ['Hello', ' World!']
'''

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#               Python Lists

mylist = ["apple", "banana", "cherry"]


#                  List
'''Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:'''

#           Example: Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)

#              List Items
'''
List items are ordered, changeable, and 
allow duplicate values.

List items are indexed, the first item 
has index [0], the second item has index [1] etc.
'''

#             Ordered

# When we say that lists are ordered, 
# it means 

# that the items have a 
# defined order, and that order will not change.

#             Note:

# There are some list methods that will change the 
# order, but in 
# general: the order of the items will not change.


#      Python - List Methods
'''
mylist = ["apple", "banana", "cherry"

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

'''
                        #Python Tuples
'''
mytuple = ("apple", "banana", "cherry")

                          Tuple:

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

Example: Create a Tuple: 

thistuple = ("apple", "banana", "cherry")
print(thistuple)

                          Tuple Items:
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

                                Unchangeable:

Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

                             Allow Duplicates:
Since tuples are indexed, they can have items with the same value:

Example: 
                Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

                          Tuple Length:
To determine how many items a tuple has, use the len() function:

                Example:
Print the number of items in the tuple:
thisuple = (("apple","banana","cherry"))
print(len(thistuple))

Create Tuple With One Item: 

To create a tuple with only one item, 
you have to add a comma after the item, 
otherwise Python will 
not recognize it as a tuple.

                        Example: 

one item tuple, remeber the comma: 
thisuple = ("apple",)
print(type(thisuple))


#NOT a tuple
thistuple = ("apple") 
print(type(thistuple))

# Result = <class 'str'> + <class 'tuple'>

    Tuple Items - Data Types:
Tuple items can be of any data type:

                Example:
String's, int and bolean data types: 
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1,5,7,9,3)
tuple3 = (True,False, False)

# A tuple can contain different data types:

                  For Example: 
A tuple with strings, integers and boolean values:
tuple1 = ("abc",34,True, 40 "male")
print(tuple1)

        type():
From Python's perspective, 
tuples are defined 
as objects with the data type 'tuple':

<class 'tuple'>

          Example:
What is the data type of a tuple? 

mytuple = ("apple","banana","cherry")

  print(type(myuple))

# Result = <class 'tuple'>

      The tuple() Consturctor:
It is also possible to use the 
'Tuple()' constructor to make a tuple.

                Example: 
Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry"))
  print(thistuple)

Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members
'''

                      # Python Sets
'''
myset = {"apple", "banana", "cherry"}
                    
                    Set:

Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data 
types in Python used to store collections of data, the other 3 are List, Tuple, 
and Dictionary, 
all with different qualities and usage.

A set is a collection 
which is unordered, unchangeable*, and unindexed.

# * Note: Set items are unchangeable, 
but you can remove items and add new items.

Sets are written with curly brackets.

                    Example:

                  Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: the set list is unordered, meaning: the items 
will appear in a random order.

# Refresh this page to see the change in the result.           

# Note: Sets are unordered, so you 
cannot be sure in which order the items will appear.


'''                             


# List Methods
'''
Python has a set of built-in methods that 
you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

#                   Changeable!

#               The list is changeable, 
#               meaning that we can change, 
#               add, and remove items in a 
#               list after it has been created.


#                 Allow Duplicates

#             Since lists are indexed, 
#       lists can have items with the same value:

                    #Example
        #Lists allow duplicate values:
  
thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)


'''
List Length
To determine how many items a list has, use the len() function:

Example
Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

3
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) 

'''
#             List Items - Data Types 
#         list items can be of any data type:

#                      Example:
#         String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]String, int and boolean data
types:
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#       A list can contain different data types:

#                       Example:
#       A list can contain different data types:
 list1 = ["abc", 34, True, 40, "male"]

print(list1)

#                         type():
#                 From Python's perspective, 
#                     lists are defined 
#                         as objects 
#                            with 
#                     the data type 'list':

#                         It Will be a           
#                        <class 'list'>


#                         Example:
#               WHAT IS THE DATA TYPE OF A LIST?

            mylist = ["apple", "banana", "cherry"]

                      print(type(mylist))



#                   The list() Constructor:
'''  
            It is also possible to use the list() 
              onstructor when creating a new list.

                            Example:
        Using the list() constructor to make a List:

            thislist = list(("apple", "banana", "cherry"))
                          print(thislist) 

       
                    ['apple', 'banana', 'cherry']

#                   note the double round-brackets

Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
'''

#                 Python - String Concatenation:
#                     String Concatenation:

#                         To concatenate, 
#      or combine, two strings you van use the + operator.


#                           Example of code!:

# Merge variable 'a' with variable 'b' into variable 'c':


a = "Hello"
b = "World"
c = a + b
print(c)



#                           Example of code!:
#                 To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)


#                     Python - Format - Strings

#                           String Format:

#                         As we learned in the 
#                       Python Variables chapter,
#                         we cannot combine strings 
#                         and numbers like this:

#                             SYNTAX EEORE!

age = 36
txt = "My name is john, I am" + age
print(txt)

# But we can combine strings and numbers by using f-strings or the format() method!

'''
F-Strings
F-String was introduced in 
Python 3.6, and is now the preferred 
way of formatting strings.

To specify 
a string 
as 
an 
f-string, 
simply put an f in 
front of the string literal, 
and add curly brackets {} 
as placeholders for variables and other operations.
'''
#                     Example: 
#                  Create an F-string:

age = 36 
txt = f"My Name is Lenny, I am {age} "
print(txt)

#           Placeholders and Modifiers:
# A placeholder can contain variables, operations, 
# functions, and modifiers to format the value.

#                      Example:
#           Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

"""
A placeholder can include a modifier to format the value.

A modifier is included by adding a colon ':'
followed by a legal formatting type, like .2f 
which means fixed point number with 2 decimals:
"""

#                   Example:

#         Display the price with 2 decimals:

price = 59 
txt = f"The price is {price:.2f} dollars"
print(txt)

#                  A placeholder can 
#     contain Python code, like math operations:

#                       Example:

#          Perform a math operation in the 
#          placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)

#               Python String Formatting!

"""
F-String was introduced in Python 3.6, and is 
now the preferred way of formatting strings.

Before Python 3.6 we had to use the format() method.

F-Strings
F-string allows you to format selected parts of a string.

To specify a string as an f-string, 
simply put an f in front of 
the string literal, like this:
"""
#                       Example:
#                   Create an f-string:

txt = f"The price is 49 dollars"
print(txt)

#              Placeholders and Modifiers:

"""
To format values in an 
f-string, add placeholders 
'{}', a placeholder 
can contain variables, 
operations, functions, 
and modifiers to format the value.
"""
#                       Example:
#         Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

"""
A placeholder can also include a modifier to format the value.

A modifier is included by 
adding a colon : followed by a legal formatting type, like .
2f which means fixed point number with 2 decimals:
"""
 
#                        Example:
#         Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Note: You can also format a value directly without keeping it in a variable:

#                           Example:
#               Display the value 95 with 2 decimals:

txt = f"The price is {95:.2f} dollars"
print(txt)

"""
Perform Operations in F-Strings

You can perform Python operations inside the placeholders.

You can do math operations:
"""

#                       Example:
#                     Perform a math 
# operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)

# Note: You can perform math operations on variables:
#                 Example of the code:

#         Add taxes before displaying the price:

price = 59 
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

'''
You can perform 'if...else' statements inside the placeholders:
'''

#                   Example of the code!: 

# Return "Expensive" if the price is over 50, otherwise return "Cheap":

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)


'''
                Execute Functions in F-Strings

        You can execute functions inside the placeholder: 

                          Example: 
                Use the string method upper()
            to convert a value into upper case letters:  

    The function does not have to be a built-in Python method, 
        you can create your own functions and use them:                                            
'''

fruit = "apples"
txt = f"I love {fruit.upper()} "
print(txt)


#                           Example:
#       Create a function that converts feet into meters:

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

"""
                            More Modifiers:

          At the beginning of this chapter we explained 
          how to use the .2f modifier to format a number 
            into a fixed point number with 2 decimals.

          There are several other modifiers that can be 
                        used to format values:                           
"""
#                             Example:

#            Use a comma as a thousand separator:

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

#                 list of all the formatting types.

'''
:<  Left aligns the result (within the available space)

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "<" to left-align the value:

txt = f"We have {49:<8} chickens."
print(txt)

:> Right aligns the result (within the available space)

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use ">" to right-align the value:

txt = f"We have {49:>8} chickens."
print(txt)

:^  Center aligns the result (within the available space)

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "^" to center-align the value:

txt = f"We have {49:^8} chickens."
print(txt)


:=		Places the sign to the left most position

#To demonstrate, we insert the number 8 to specify the available space for the value.

#Use "=" to place the plus/minus sign at the left most position:

txt = f"The temperature is {-5:=8} degrees celsius."

print(txt)


:+		Use a plus sign to indicate if the result is positive or negative

#Use "+" to always indicate if the number is positive or negative:

txt = f"The temperature is between {-3:+} and {7:+} degrees celsius."

print(txt)

:-		Use a minus sign for negative values only

#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):

txt = f"The temperature is between {-3:-} and {7:-} degrees celsius."

print(txt)

: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)

#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:

txt = f"The temperature is between {-3: } and {7: } degrees celsius."

print(txt)

:,  Use a comma as a thousand separator

#Use "," to add a comma as a thousand separator:

txt = f"The universe is {13800000000:,} years old."

print(txt)


:_		Use a underscore as a thousand separator

#Use "_" to add a underscore character as a thousand separator:

txt = f"The universe is {13800000000:_} years old."

print(txt)


:b		Binary format

#Use "b" to convert the number into binary format:

txt = f"The binary version of 5 is {5:b}"

print(txt)

:c		Converts the value into the corresponding Unicode character


:d		Decimal format

#Use "d" to convert a number, in this case a binary number, into decimal number format:

txt = f"We have {0b101:d} chickens."

print(txt)

:e		Scientific format, with a lower case e

#Use "e" to convert a number into scientific number format (with a lower-case e):

txt = f"We have {5:e} chickens."

print(txt)

:E  Scientific format, with an upper case E

#Use "E" to convert a number into scientific number format (with an upper-case E):

txt = f"We have {5:E} chickens."

print(txt)

:f		Fix point number format

#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:

txt = f"The price is {45:.2f} dollars."
print(txt)

#without the ".2" inside the placeholder, this number will be displayed like this:

txt = f"The price is {45:f} dollars."
print(txt)

:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)

#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

x = float('inf')

txt = f"The price is {x:F} dollars."
print(txt)

#same example, but with a lower case f:

txt = f"The price is {x:f} dollars."
print(txt)

:g		General format

:G		General format (using a upper case E for scientific notations)

:o		Octal format

Use "o" to convert the number into octal format:

txt = f"The octal version of 10 is {10:o}"

print(txt)

:x		Hex format, lower case

#Use "x" to convert the number into Hex format:

txt = f"The Hexadecimal version of 255 is {255:x}"

print(txt)

:X		Hex format, upper case

#Use "X" to convert the number into upper-case Hex format:

txt = f"The Hexadecimal version of 255 is {255:X}"

print(txt)

:n		Number format

:%		Percentage format

#Use "%" to convert the number into a percentage format:

txt = f"You scored {0.25:%}"
print(txt)

#Or, without any decimals:

txt = f"You scored {0.25:.0%}"
print(txt)
'''

# String format()

'''
Before Python 3.6 we used the 'format()' method to format string's.

The format() method can still be used, but f-strings are faster and the preferred way to format strings.

The next examples in this page demonstrates how to format strings with the format() method.

The format() method also uses curly brackets as placeholders {}, but the syntax is slightly different:
'''
# Example: Add a placeholder where you want to display the price:

price = 49 
txt = "The price is {} dollars"
print(txt.format(price))

# Note! - You can add parameters inside the curly brackets to specify how to convert the value:

# Example: Format the price to be displayed as a number with two decimals:

price = 49 
txt = " The price is {:.2f} dollars "
print(txt.format(price))

# Diffent Types of String's formating Reference.

#               Python String format() Method:

# Example: Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:

txt = "For only {price:.2f} dollars! "
print(txt.format(price = 49))

'''
Definiton and Usage:

The format() method formats the specified value(s) and insert them inside the string's placeholder.

The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

The format() method returns the formatted string.

                        Syntax Error!

                string.format(value1, value2...)

                        Parameter Values

Parameter	        Description
value1, value2...	Required. One or more values that should be formatted and inserted in the string.

                  The values are either a list of values separated by commas, a key=value list, or a combination of both.

                  The values can be of any data type.                        

                  
                          The Placeholders:

The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.

For a Example: Using a diffent placeholder values:

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)
'''

#                         Formatting Types!

#  Inside the placeholders you can add a formatting type to format the result:

'''
:<		Left aligns the result (within the available space)

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "<" to left-align the value:

txt = "We have {:<8} chickens."
print(txt.format(49))

:>		Right aligns the result (within the available space)

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use ">" to right-align the value:

txt = "We have {:>8} chickens."
print(txt.format(49))

:^		Center aligns the result (within the available space)

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "^" to center-align the value:

txt = "We have {:^8} chickens."
print(txt.format(49))

:=		Places the sign to the left most position

#To demonstrate, we insert the number 8 to specify the available space for the value.

#Use "=" to place the plus/minus sign at the left most position:

txt = "The temperature is {:=8} degrees celsius."

print(txt.format(-5))

:+		Use a plus sign to indicate if the result is positive or negative

#Use "+" to always indicate if the number is positive or negative:

txt = "The temperature is between {:+} and {:+} degrees celsius."

print(txt.format(-3, 7))

:-		Use a minus sign for negative values only

#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):

txt = "The temperature is between {:-} and {:-} degrees celsius."

print(txt.format(-3, 7))

: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)

#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:

txt = "The temperature is between {: } and {: } degrees celsius."

print(txt.format(-3, 7))

:,		Use a comma as a thousand separator

#Use "," to add a comma as a thousand separator:

txt = "The universe is {:,} years old."

print(txt.format(13800000000))

:_		Use a underscore as a thousand separator

#Use "_" to add a underscore character as a thousand separator:

txt = "The universe is {:_} years old."

print(txt.format(13800000000))

:b		Binary format

#Use "b" to convert the number into binary format:

txt = "The binary version of {0} is {0:b}"

print(txt.format(5))

:c		Converts the value into the corresponding unicode character

:d		Decimal format

#Use "d" to convert a number, in this case a binary number, into decimal number format:

txt = "We have {:d} chickens."
print(txt.format(0b101))

:e		Scientific format, with a lower case e

#Use "e" to convert a number into scientific number format (with a lower-case e):

txt = "We have {:e} chickens."
print(txt.format(5))

:E		Scientific format, with an upper case E

#Use "E" to convert a number into scientific number format (with an upper-case E):

txt = "We have {:E} chickens."
print(txt.format(5))

:f		Fix point number format

#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:

txt = "The price is {:.2f} dollars."
print(txt.format(45))

#without the ".2" inside the placeholder, this number will be displayed like this:

txt = "The price is {:f} dollars."
print(txt.format(45))

:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)

#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

x = float('inf')

txt = "The price is {:F} dollars."
print(txt.format(x))

#same example, but with a lower case f:

txt = "The price is {:f} dollars."
print(txt.format(x))

:g		General format

:G		General format (using a upper case E for scientific notations)

:o		Octal format

#Use "o" to convert the number into octal format:

txt = "The octal version of {0} is {0:o}"

print(txt.format(10))

:x		Hex format, lower case

#Use "x" to convert the number into Hex format:

txt = "The Hexadecimal version of {0} is {0:x}"

print(txt.format(255))

:X		Hex format, upper case

#Use "X" to convert the number into upper-case Hex format:

txt = "The Hexadecimal version of {0} is {0:X}"

print(txt.format(255))

:n		Number format

:%		Percentage format

#Use "%" to convert the number into a percentage format:

txt = "You scored {:%}"
print(txt.format(0.25))

#Or, without any decimals:

txt = "You scored {:.0%}"
print(txt.format(0.25))
'''

# Multiple Values's
# If you want to use more values, just add more values to format() method:

print(txt.format(price, itemno count))

# Note!: Add more placeHolder:

#                     Example of the code!

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#                       Index Numbers:
'''
You can use index numbers 
(a number inside the curly brackets {0}) 
to be sure the values are placed in the correct placeholders:
'''

#                        Example:

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Also, if you want to refer to the same value more than once, use the index number:

#                         Example:

age = 18 
name = "lenny"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

#                       Named Indexes:
'''
            You can also use named indexes 
              by entering a name inside 
                the curly brackets {carname}, 
                  but then you must use names 
                    when you pass the parameter values 
                      txt.format(carname = "Ford"):
'''

#                         Example:

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

#               Python - Escape Characters

"""
                      Escape Character:

To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

                            Example:
You will get an error if you use double quotes inside a string that is surrounded by double quotes:

txt = "We are the so-called "Vikings" from the north."


#You will get an error if you use double quotes inside a string that are surrounded by double quotes:
"""
# To fix this Problem, use the escape character \":

#                           Example:

# The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#                     Escape Characters! 
#           Other escape characters used in Python:

'''
Code	          Result
\'	            Single Quote
txt = 'It\'s alright.'
print(txt) 

\\	Backslash
txt = "This will insert one \\ (backslash)."
print(txt) 

\n	New Line
txt = "Hello\nWorld!"
print(txt) 

\r	Carriage Return
txt = "Hello\rWorld!"
print(txt) 

\t	Tab
txt = "Hello\tWorld!"
print(txt) 

\b	Backspace
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

\f	Form Feed

\ooo	Octal value
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

\xhh	Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
'''
#                   Python - String Methods:

#                        String Methods:

# Python has a set of built-in methods that you can use on strings.

# Note: All string methods return new values. They do not change the original string.

'''
Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''

#               Python String capitalize() Method:

# Example: Upper case the first letter in this sentence:

txt = " hello, and welcome to my world."

x = txt.capitalize()

print(x)

# Definition and Usage

'''
The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
'''

#                         SYNTAX ERROR'S
# string.capitalize()

#                       Parameter Values:

#                         No parameters!

#                       More Examples:

#                          Example:
# The first character is converted to upper case, and the rest are converted to lower case:

txt = "python is FUN!"

x = txt.capitalize()

print (x)

# Example!!!
# See what happens if the first character is a number:

txt = "36 is my age."

x = txt.capitalize()

print (x)

# Python String casefold() Method

# Example of the code!!
# Make the string lower case:

txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

'''
Definition and Usage
The casefold() method returns a string where all the characters are lower case.

This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.
'''

# Python String lower() Method

# Example: Lower case the string:

txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

'''
Definition and Usage
The lower() method returns a string where all characters are lower case.

 Symbols and Numbers are ignored.
'''

# Syntax error's
# string.lower()

# Parameter Values
# No parameters

#                         Syntax Error's

#                       string.casefold() 

#                       Parameter Values
# No parameters.


#               Python String center() Method! 


# Example!: Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:

txt = "Banana"

x = txt.center(20)

print(x)

'''
Definition and Usage
The center() 
method will center align the 
string, using a specified character 
(space is default) as the fill character.
'''

# Syntax
# string.center(length, character)

# Parameter Values
# Parameter	Description
# length	Required. The length of the returned string
# character	Optional. The character to fill the missing space on each side. Default is " " (space)

# More Examples

#                             Example.

#       Using the letter "O" as the padding character:

txt = "banana"

x = txt.center(20, "O")

print(x)


#                 Python String count() Method

# Example: Return the number of times the value "apple" appears in the string:

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)


# Definition and Usage
# The count() method returns the number of times a specified value appears in the string.

# Syntax
# string.count(value, start, end)
# Parameter Values
# Parameter	Description
# value	Required. A String. The string to value to search for
# start	Optional. An Integer. The position to start the search. Default is 0
# end	Optional. An Integer. The position to end the search. Default is the end of the string

# Example
# Search from position 10 to 24:

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x)



#           Python String encode() Method

# Example: UTF - 8 encode the string:

txt = "My name is Ståle"

x = txt.encode()

print(x)


# Definition and Usage
# The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.

# Syntax
# string.encode(encoding=encoding, errors=errors)

#                     Parameter Values

# Parameter	Description
# encoding	Optional. A String specifying the encoding to use. Default is UTF-8
# errors	Optional. A String specifying the error method. Legal values are:
# 'backslashreplace'	- uses a backslash instead of the character that could not be encoded
# 'ignore'	- ignores the characters that cannot be encoded
# 'namereplace'	- replaces the character with a text explaining the character
# 'strict'	- Default, raises an error on failure
# 'replace'	- replaces the character with a questionmark
# 'xmlcharrefreplace'	- replaces the character with an xml character

#                       More Examples

# Example: These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))


#             Python String endswith() Method

#                       Example!!
# Check if the string ends with a punctuation sign (.):

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

# Definition and Usage
# The endswith() method returns True if the string ends with the specified value, otherwise False.

# Syntax
# string.endswith(value, start, end)

#                       Parameter Values:
# Parameter	Description
# value	Required. The value to check if the string ends with
# start	Optional. An Integer specifying at which position to start the search
# end	Optional. An Integer specifying at which position to end the search

#                        More Examples

# Example: Check if the string ends with the phrase "my world.":

txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)

# True.

# Example: Check if position 5 to 11 ends with the phrase "my world.":

txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x)


#             Python String expandtabs() Method

# Example: Set the Tab size to 2 whitespaces:

txt = "H\te\tl\t1\to"

x = txt.expandtabs(2)

print(x) 

# Defintion and Usage:

# The 'expandtabs()' method sets the tab size to the specifed number of whitespaces.

# Syntax: 
# string.expandtabs(tabsize)

# Parameter Values

# Parameter	Description
# tabsize	Optional. A number specifying the tabsize. Default tabsize is 8

#                         More Examples!

# Example: See the Result using different Tab sizes:

txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

#             Python String find() Method.

# Example: Where in the text is the word "Welcome"?:

txt = "Hello, Welcome to my world!"

x = txt.find("welcome")

print(x)

# Definition and Usage:

# The find() method finds the first occurrence of the specified value.

# The find() method returns -1 if the value is not found.

# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)

#               Python String index() Method.

# Example: Where in the text is the word "welcome"?:

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)
 
'''
Definition and Usage
The index() method finds the first occurrence of the specified value.

The index() method raises an exception if the value is not found.

The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below)
'''

# Syntax
# string.index(value, start, end)

# Parameter Values

# Parameter	Description
# value	Required. The value to search for
# start	Optional. Where to start the search. Default is 0
# end	Optional. Where to end the search. Default is to the end of the string

# More Examples

# Example: Where in the text is the first occurrence of the letter "e"?:

txt = "Hello, Welcome to my house"

x = txt.index("e")

print(x)

# Example: Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:

txt = "Hello, Welcome to my world."

x = txt.index("e",5,10)

print(x)

# Example: If the value is not found, the find() method returns -1, but the index() method will raise an exception: 

txt = "Hello, Welcome to my world!."

print(txt.find("q"))
print(txt.index("q"))

# Syntax
# string.find(value, start, end)

# Parameter Values
# Parameter	Description
# value	Required. The value to search for
# start	Optional. Where to start the search. Default is 0
# end	Optional. Where to end the search. Default is to the end of the string



#             Python String isalnum() Method.

# Example: Check if all the characters in the text are alphanumeric:

txt = "Compant12"

x = txt.isalnum()

print(x)


# Definition and Usage
# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

# Example of characters that are not alphanumeric: (space)!#%&? etc.

# Syntax
# string.isalnum()

# Parameter Values
# No parameters.

# Example: Check if all the characters in the text is alphanumeric:

txt = "Company 12"

x = txt.isalnum()

print(x)

            # Python String isalpha() Method


#                       Example.

# Check if all the characters in the text are letters:

txt = "CompanyX"

x = txt.isalpha()

print(x)

# Definition and Usage
# The isalpha() method returns True if all the characters are alphabet letters (a-z).

# Example of characters that are not alphabet letters: (space)!#%&? etc.

# Syntax
# string.isalpha()

# Parameter Values
# No parameters.

                    # More Examples

#                     Example
# Check if all the characters in the text is alphabetic:

txt = "Company10"

x = txt.isalpha()

print(x)





#             Python String isascii() Method

# Example: Check if all the characters in the text are ascii characters:

txt = "Company123"

x = txt.isascii()

print(x)

# Definition and Usage
# The isascii() method returns True if all the characters are ascii characters  (a-z).

# Check our ASCII Reference.

# Syntax
# string.isascii()

# Parameter Values
# No parameters.

'''
HTML ASCII Reference:

ASCII was the first character set (encoding standard) used between computers on the Internet.

Both ISO-8859-1 (default in HTML 4.01) and UTF-8 (default in HTML5), are built on ASCII.

                    The ASCII Character Set:

ASCII stands for the "American Standard Code for Information Interchange".

It was designed in the early 60's, as a standard character set for computers and electronic devices.

ASCII is a 7-bit character set containing 128 characters.

It contains the numbers from 0-9, the upper and lower case English letters from A to Z, and some special characters.

The character sets used in modern computers, in HTML, and on the Internet, are all based on ASCII.

The following tables list the 128 ASCII characters and their equivalent number.

                  ASCII Printable Characters:

Char	Number	Description
 	0 - 31	Control characters (see below)
 	32	space
!	33	exclamation mark
"	34	quotation mark
#	35	number sign
$	36	dollar sign
%	37	percent sign
&	38	ampersand
'	39	apostrophe
(	40	left parenthesis
)	41	right parenthesis
*	42	asterisk
+	43	plus sign
,	44	comma
-	45	hyphen
.	46	period
/	47	slash
0	48	digit 0
1	49	digit 1
2	50	digit 2
3	51	digit 3
4	52	digit 4
5	53	digit 5
6	54	digit 6
7	55	digit 7
8	56	digit 8
9	57	digit 9
:	58	colon
;	59	semicolon
<	60	less-than
=	61	equals-to
>	62	greater-than
?	63	question mark
@	64	at sign
A	65	uppercase A
B	66	uppercase B
C	67	uppercase C
D	68	uppercase D
E	69	uppercase E
F	70	uppercase F
G	71	uppercase G
H	72	uppercase H
I	73	uppercase I
J	74	uppercase J
K	75	uppercase K
L	76	uppercase L
M	77	uppercase M
N	78	uppercase N
O	79	uppercase O
P	80	uppercase P
Q	81	uppercase Q
R	82	uppercase R
S	83	uppercase S
T	84	uppercase T
U	85	uppercase U
V	86	uppercase V
W	87	uppercase W
X	88	uppercase X
Y	89	uppercase Y
Z	90	uppercase Z
[	91	left square bracket
\	92	backslash
]	93	right square bracket
^	94	caret
_	95	underscore
`	96	grave accent
a	97	lowercase a
b	98	lowercase b
c	99	lowercase c
d	100	lowercase d
e	101	lowercase e
f	102	lowercase f
g	103	lowercase g
h	104	lowercase h
i	105	lowercase i
j	106	lowercase j
k	107	lowercase k
l	108	lowercase l
m	109	lowercase m
n	110	lowercase n
o	111	lowercase o
p	112	lowercase p
q	113	lowercase q
r	114	lowercase r
s	115	lowercase s
t	116	lowercase t
u	117	lowercase u
v	118	lowercase v
w	119	lowercase w
x	120	lowercase x
y	121	lowercase y
z	122	lowercase z
{	123	left curly brace
|	124	vertical bar
}	125	right curly brace
~	126	tilde
'''

'''
ASCII Device Control Characters

The ASCII control characters (range 00-31, plus 127) were designed to control hardware devices.

Control characters (except horizontal tab, line feed, and carriage return) have nothing to do inside an HTML document.

Char	Number	Description
NUL	00	null character
SOH	01	start of header
STX	02	start of text
ETX	03	end of text
EOT	04	end of transmission
ENQ	05	enquiry
ACK	06	acknowledge
BEL	07	bell (ring)
BS	08	backspace
HT	09	horizontal tab
LF	10	line feed
VT	11	vertical tab
FF	12	form feed
CR	13	carriage return
SO	14	shift out
SI	15	shift in
DLE	16	data link escape
DC1	17	device control 1
DC2	18	device control 2
DC3	19	device control 3
DC4	20	device control 4
NAK	21	negative acknowledge
SYN	22	synchronize
ETB	23	end transmission block
CAN	24	cancel
EM	25	end of medium
SUB	26	substitute
ESC	27	escape
FS	28	file separator
GS	29	group separator
RS	30	record separator
US	31	unit separator
 	 	 
DEL	127	delete (rubout)
'''

# Python String isascii() Method
#Examle: check if all the characters in the next are ascii characters:

txt = "Company123"

x = txt.isascii()

print(x)

# Definiton and Usage!
'''
The isascii() method returns True if all the characters are ascii characters  (a-z).

Check our ASCII Reference.

Syntax
string.isascii()

Parameter Values
No parameters.
'''

#             Python String isdecimal() Method


# Example: Check if all the characters in string are decimals (0-9)

txt ="1234"

x = txt.isdecimal()

print(x)

# Definition and Usage:

# The isdecimal() mehod returns True if all the characters decimals (0=9)

# This method can also be used on unicode objects. See example below.

# Syntax: String.isdecimal()

# Parameter Values: NO parameters.

# MORE EXAMPLE: CHECK IF ALL THE CHARACTERS IN unicode are decimals:

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())

#               Python String isdigit() Method 

#                         Example: 
# Check if all the characters in the text are digits.

txt = "50800"
 
x = txt.isdigit

print(x)


'''
Definition and Usage
The isdigit() method returns True if all the characters are digits, otherwise False.

Exponents, like ², are also considered to be a digit.

    Syntax
string.isdigit()

Parameter Values
No parameters.
'''

#                           More Example:

# Example: Check if all the characters in the text are digits:

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())

#           Python String isidentifier() Method:

# Example: check if the string is a valid identifier:

txt = "Demo" 

x = txt.isidentifier()

print(x)

'''
Definiton and Usage:

The isidentifier() method returns True if the string is a valid identifer, otherwise False.

Astring is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

Syntax
string.isidentifier()

Parameter Values
No parameters.
'''

# More Example!

# Example: Check if the strings are valid ifentifiers:

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())


# Python String islower() Method <--->

# Example: Check if all the characters in the text are in lower case:

txt = "hello world!"

x = txt.islower()

print(x)


'''
Definition and Usage
The islower() method returns True if all the characters are in lower case, otherwise False.

Numbers, symbols and spaces are not checked, only alphabet characters.
'''

# Syntax: string.islower()

# Parameter Values.
# No parameters.

# For example: Check if all the characters in the texts are in lower case:

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())


#         Python String isnumeric() Method.

# Example: Check if the characters in the text are numeric:

txt = "565543"

x = txt.isnumeric()

print(x)

'''
Definition and Usage
The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.

Exponents, like ² and ¾ are also considered to be numeric values.

"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
'''
# Syntax: 'string.isnumeric()'

# Parameter Values:
# No parameters:

# More Examples:

# For Example: Check if the characters are numeric:


a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())

# Python String isprintable() Method!

'''
Example: check if all the characters in the text  are printable.
'''

txt =  "hello Are you #1?"

x =  txt.isprintable()

print(x)

# Definiton of the Usage.

'''
The isprintable() method returns True if all the characters are printable, otherwise False.

Example of none printable character can be carriage return and line feed.
'''

# Syntax: string.isprintable()

# Parameter Values:
# No Parameters.

# More Examples: 

# Example of the code!
# Check if all the characters in the text are printable:

txt = "Hello!\nAre you #1?"

x = txt.isprintable()

print(x)


                #Python String isspace() Method

# Example: Check if all the characters in the text are whitespace:

txt = "   "

x = txt.isspace()

print(x)

# Definition and the Usage:
# The 'isspace()' 
# method returns True if all the characters in 
# string are whitespacees, otherwise False.

'''
Syntax: String.isspace()

Parameter Values: No parameters.
'''

# More Examples
# Check if all the charaters in the text are whitespace: 
'''
text = " s " 
x = txt.isspac()
print(x)  -------- Answer = FALSE
'''

# Python String istitle() Method
 # EXAMPLE ---- Check if each word start with an upper case Letter:
  
  x = txt.istitle()
print(x)

#Definition and Usage
# The istitle() method returns True 
# if all words in text start with
# all words in text start with a 
# upper case letter, AND the rest #
# of the word  are lower case letters, otherwise false.

# Symbols and numbers are ignored.

'''

Syntax ----- String.istitle()

'''
# Parameter Values --- No parameters.

# More Examples --- Check if each word start 
# with an upper case letter:
 
      a = "HELLO, AND WELCOME TO MY WORLD"
    B = "Hello" \
    c = "22 Name"
    d = "This Is %'!?"
 
print(a.istitle()) # False
print(b.istitle()) # True
print(c.istitle()) # True
print(d.istitle()) # True
