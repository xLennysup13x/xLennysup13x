# Python programing

# Learn Python'

# Python is a popular programming language.
# Python can be used on a server to create web applications.

# Learning by Examples
# With our "Try it Yourself" editor, you can edit Python code and view the result.

# Example
print("hello, world!")

# Python File Handling
# In our File Handling section you will learn how to open, read, write, and delete files.

# Python File Open

# File handling is an important part of any web application. 
# Python has several functions for creating, reading, updating, and deleting files.

# File Handling 

# the key fuction for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:

"r" # - Read - Default value. Opens a file for reading, error if the file does not exist
"a" # - Append - Opens a file for appending, creates the file it dose not exist
"w" # - Write  - opens a file for writeing, creates the file if dose noy exist
"x" # -  create - creates the specified file, returns an error if the file exists

# In additon you can specify if the file should be handled as binary or text mode!

"t" # - Text Default value. Text mode 

"b" # - Binary - Binary mode (e.g images)

# Syntax

# To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")

# The code above is the same as:

f = open("demofile.txt","rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# note Make sure the file exitst, or else you will get an error.
 
# Python Comments 
# Comments can be used to explain Python code.
# Comments can be used to make the code more readable.
# Comments can be used to prevent excution when testing code.

# Createing a Comment'

# Comments starts with a '#' , and Python will ignore them 

# Example 

# this is a comment

# print just print's 'hello world!'
print("hello, world!")

# Comments dose not have to be text that explaints the code, it can also be used to prevent python from executing, code!

# Example 

# print("hello world!")
print("Cheers, Mate!")

# Multiline Comments
# Python does not really have a syntax for multiline comments.
# To add a multiline comment you could insert a # for each line:

# Example 
# written in 
# more than just one line
print("hello, world!")
# print's the 'hello world!'

 # As Long as the string is not assigned to a varable, Python will read the codel but then ignore it, and you have mad a multiline comment.

