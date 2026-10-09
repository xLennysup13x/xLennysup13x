                    # Python Casting

# Specify a Variable Type:

# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an
# object-orientated language, and as such it uses classes to dinfe data types, including its primitive types.

# Casting in Python is therefore done using constructor functions:

int() - # Construct an integer number from an integer literal, a float literal (by removing all decimals), or a
    # string lileral (providing the string represents a whole number)

    # float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string 
    # represents a float or an integer)

    # str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals


# Example of code:
#   :Integers:

x = int(1)
y = int(2.8)
z = int('3')
print(x) # x will be 1
print(y) # y will be 2
print(z) # z will be 3

# Example of code:
#   :Float:

x = float(1.0)
y = float(2.8)
z = float('3') 
w = float("4.2")
print(x) # x will be 1.0
print(y) # y will be 2.8
print(z) # z will be 3.0
print(w) # w will be 4.2


# Example of code:
#   :strings:

x = str(1.0)
y = str(2.8)
z = str('3') 
print(x) # x will be 's1'
print(y) # y will be '2'
print(z) # z will be '3.0'
