# Python Data Types

#Bulit-in Data Types 

# In programming, data types is an important concept
# Variables can store data of different types, and different type can do different thing's
# Pyhon has the following data types built- in by default in case categories:

# Text Tpye:      'str'
# Numeric Types:  'int, float, complex'
# Sequence Types: 'list, tuple, range'
# Mapping Type:	  'dict'
# Set Types:	  'set, frozenset'
# Boolean Type:	  'bool'
# Binary Types:	  'bytes, bytearray, memoryview'
# None Type:	  'NoneType'

# Getting the Data Type 
# You can get the data type type of any object by using the type() function:

X = 5  # x is being used to use a value  x = 5 meaning saying print's '5'!
print(type(x)) # pirnt's a  <------> <class 'int'!

# Setting the Data Type 
# In Python, the data type is set when you assign a value to a variable:

# |Example|                      |Data Type|
# x = "hello world"                 'str'

x = "hello" # this print's 'hello'
# display x:
#display the data type of x:
print(type(X)) # We End up Getting a value of  print 'command'  'hello'

x = 20 
# display x:  
print(X) # print's x then takes it and print's <--->  '20'
# display the data type of x:
print(type(X)) # print's <class 'int'
 
# we get a <class 'float'>
x= 20.5  # and we also get '20.5'
#display x:
print(X) # print's the x 
#display the data type of x:
print(type(X)) # print's the x '

# x = 1j	complex 
x = 1j 
# display x:
print(x) # print's the following x:
# display the data type of x:
print(type(X)) # print's 'type(x)'

# x = ["apple", "banana", "cherry"]	'list'
x = ["apple", "banana", "cherry"]
# display x:
print(X)
# display the data type of x:
print(type(X))

# x = ("apple", "banana", "cherry")	tuple
x = ("apple", "banana", "cherry")
# display x:
print(x) # print's the x
# display the data type of x:
print(type(x)) 

# x = range(6)  'range'
x = range(6)
# display x:
print(x) # print's x
#displays the data type of x:
print(type(x))
# gives a <class 'range'> 

# x = {"name" : "Lenny", "age" : 36}  'dict'
x = {"name" : "Lenny", "age" : 36}
# display x:
print(x)
#display the data type of x:
print(type(x)) # give's a <class 'dict'>

# x = {"name" : "Lenny", "age" : 36} 'set'
# display x:
print(x) # print's x
#display the data type of x:
print(type(x)) # give's a <class 'set'>

# x = frozenset({"apple", "banana", "cherry"})	frozenset	frozenset
x = frozenset({"apple", "banana", "cherry"}) # print's 'apple','banana','cherry'
print(x) # print's x
# display's the data type of x: 
print(type(x))

# x = True	'bool'
x = True # give's us a true 
print(x) # print's x
print(type(x)) # print's the data type of x:
# gives us a <class'bool'> ! 

# x = b"Hello"	bytes
x = b"hello" # gives us a 'b 'hello'
print(X) # display x:
# display the data type of x:

# x = bytearray(5)	'bytearray'
x = bytearray(5) #  print's bytearray(b'\x00\x00\x00)
print(X) # print's x:
print(type(X)) # print's the data type x:
# <class 'bytearray'>

# x = memoryview(bytes(5))	memoryview 
x = memoryview(bytes(5)) #  Print's <memory at 0x006F8FA0>
print(x) # display's the x: 
print(type(x)) # print's the data value of x:

# x = None	'NoneType'
x = None # print's None 
print(x) # display x:
print(type(x)) #  print's the data type of x:
# give's us a <class 'NoneType'

#          Setting the Specific Data Type       #
# If you want to specify the data type, you can use the following constructor functions:


#Example:	                              Data Type:      #
# x = str("hello")                          'srt'
# x = int(20)	                            'int'
# x = float(20.5)	                       'float'
# x = complex(1j)	                       'complex'
# x = list(("apple", "banana", "cherry"))	'list'
# x = tuple(("apple", "banana", "cherry"))	'tuple'
# x = range(6)	                            'range'
# x = dict(name="John", age=36)	             'dict'
# x = set(("apple", "banana", "cherry"))      'set'
# x = frozenset(("apple", "banana", "cherry")) 'frozenset'
# x = bool(5)	                                'bool'
# x = bytes(5)	                                'bytes'
# x = bytearray(5)	                            'bytearray'
# x = memoryview(bytes(5))	                    'memoryview'

X = str("hello") # print's 'hello world' / <class str>
print(x) # display x:
print(type(x)) # print's the data type of x:

x = int(20)  # give us a '20' and a <class tint'>
print(x) # display x:
print(type(x)) # print the data type of x:

x = float(20.5) # print's 20.5 and gives us <class 'float'>
print(x) # display's x:
print(type(x)) # print's the data type of x:

x = complex(1j) # print's the following '1j'
print(x) # display's x:
print(type(x)) # print's the data type of x:
# give's us a <class 'complex>

x = list(("apple","banana","cherry"))  # this print's the following: "apple","banana","cherry" !
print(x) # display's the x:
print(type(x)) # print's the data type x:
# give's us a <class 'list'> 

x = tuple(("apple", "banana", "cherry")) #his print's the following: "apple","banana","cherry" !
print(x) # display the following x:
print(type(x)) # print's the data type of x:
# This give's us a <class 'tuple'> 

x = range(6) # print's the following from (0,6)
print(x) # display's x:
print(type(x)) # print's the data type of x:
# gives us a following <class 'range'>

x = dict(name="lenny", age=18) # this print's {'name': 'John', 'age': 36}
print(x) # display's x:
print(type(x)) # prints the data type x:
# This gives us a <class 'dict'>

x = set(("apple", "banana", "cherry")) # This print's {'banana', 'apple', 'cherry'}
print(x) #display x:
print(type(x)) #print's  the data type of x:
# this gives us a <class 'set'>

x = frozenset(("apple","banana","cherry")) # print's frozenset({'cherry', 'apple', 'banana'})
print(x) # display
print(type(x)) # print's the data type of x:
# <class 'frozenset'> 

x = bool(5) # print's true
print(x) # display's x:
print(type(x)) # print's the data type of x:
# <class 'bool'>

x = bytes(5) # print's the following b'\x00\x00\x00\x00'
print(x) # display x:
print(type(x)) # display the data type of x:
# <class 'bytes'>

x = bytearray(5) # print's bytearray(b'\x00\x00\x00\x00\x00')
print(x) # display's x:
print(type(x)) # print's the data type of x:
# we get <class 'bytearray'>

x = memoryview(bytes(5)) # print's the following <memory at 0x00D58FA0>
print(x) # display's x:
print(type(x))  # print's the data type of x:
# class 'memoryview'> 

# Test myself With Exercises

x = 5 # print's x and 5 well just '5'
print(type(x)) # print's the data type of x:
int