# python Numbers

# python Numbers
#There are three numeric type in Python:

# 'int'
# 'float'
# 'complex

# Variables of numeric types are created when you assign a value to them:

# Example:
x = 1 # int
y = 2.8 # float
z = 1j # comples

# to Verify the type of any object in Python, use type() function:

# Example:
print(type(x))
print(type(y))
print(type(z))

''' 
Example: 
x = 1 # int
y = 2.8 # float# Gets user input
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
z = 1j # comples

print(type(x))
print(type(y))
print(type(z))
'''
# Int 
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

# Example:
# Integers: 

x = 1 # int
y = 35656222554887711 # int
z = -3255522 # int

print(type(x)) # <class 'int'>
print(type(y)) # <class 'int'>
print(type(z)) # <class 'int'>

# Float 
# Float, "floating point number" is a number, posititve or negative, containing one or more decimals.

# Example 
# Floats:

x = 1.10
y = 1.0   # only print's  '<class 'float'>'
z = -35.59 

print(type(x)) # <class 'float'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'float'>

# Float can also be scientfic numbers with me "e " indicate the power of 10.

# Example 
# Floats: 

x = 35e3
y = 12E4  # only print's  '<class 'float'>'
Z = -87.7e100

print(type(x)) # <class 'float'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'float'>

# Type Conversion 
# You can convert from one type to another with the int(), float(), and complex() methods:

# Example 
# Convert from one type to another:

x = 1 # int
y = 2.8 # float
z = 1j # complex

# convert from int to float:
a = float(x)

# convert from int to int:
b = int(y)

# convert from int to complex:
c = complex(x) 

print(a) # print's the '1'
print(b) # print's the 2.8
print(c) # print's (1+0j)

print(type(a)) # <class 'float'>
print(type(b)) # <class 'int'>
print(type(c)) # <class 'complex'>

# Note: You cannot convert complex numbers into another number type:.

# Random Number 
# Python dose not have a random() fuction to make a random number, but Python has a built-in module called
# random that can be used to make random numbers:

# Example: 
# Import the random module, and the display a random number between 1 and 9:

import random # Import is a the random module, and the display a random number between 1 and 9:

print(random.randrange(1,10))

# then  print's '4'

# Python Random Module: 

# Python has a built-in module that can you use to make random number.
# The random module has a set of methods:

# Method:                           Description:
# seed()                            Initialize the random number generator
# getstate()                        Returns the current internal state of the random number generator
# setstate()                        Restores the internal state of the random number generator
# getrandbits()                    Returns a random number between the given range
# randrange()                      	Returns a random number between the given range 
# randint()                         Returns a random number then given range 
# choice()                        Returns a random element from the given sequence
# choices()	                        Returns a list with a random selection from the given sequence
# shuffle()	                        Takes a sequence and returns the sequence in a random order
# sample()	                        Returns a given sample of a sequence
# random()	                        Returns a random float number between 0 and 1
# uniform()	                        Returns a random float number between two given parameters
# triangular()	                    Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
# betavariate()	                    Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
# expovariate()	                    Returns a random float number based on the Exponential distribution (used in statistics)
# gammavariate()	                Returns a random float number based on the Gamma distribution (used in statistics)
# gauss()	                        Returns a random float number based on the Gaussian distribution (used in probability theories)
# lognormvariate()	                Returns a random float number based on a log-normal distribution (used in probability theories)
# normalvariate()	                Returns a random float number based on the normal distribution (used in probability theories)
# vonmisesvariate()	                Returns a random float number based on the von Mises distribution (used in directional statistics)
# paretovariate()	                Returns a random float number based on the Pareto distribution (used in probability theories)
# weibullvariate()	                Returns a random float number based on the Weibull distribution (used in statistics)

"""
Python Random seed() Method 

Example set the seed vaule to 10 see wha happens:

imoprt random

random.seed(10)
print(random.seed()) 

#the generator creates 
a random number based on 
the seed value, so if the seed 
value is 10, you will always
get 0.5714025946899135 
as the first random number.

Defintion and Usage 

The seed() method is used to initallized the random number generator.

The random number generator need a number to start with ( a seed value), to be able to genrate a random number.

By default the random number generator uses the current system time.

use default the random number genertor use the current system time.

use the seed9 method to customize the start number of the random number genertor.

Note: If you use the same seed value twice you will get the same random number twice.

see example below! 

Syntax:

Parameter Values:

Paramter:                    Description:
a                            oPTIONAL. The seed value need to genrate a random number.
                            If its an integer it used diretly, if not it has to be converted into 
                            an intger.
                            Default value is None, The generator used the current
                            system time.

version                     An inter specifying how to convert the 'a' parameter into a integer.
                            Default value is 2                          
"""
# Example: 

# Demonstrate that if you use the seed value twice, you will get the same random 

import random

random.seed(10)
print(random.random())

random.seed(10)
print(random.random()) 

'''
Python Random gestate() Method 

Example:
Return the current state of the random generator:

import random
x = random.getstate()
print(x)

# print's out '3(2147483648, 3103207354, 496875541, 757866351, 2961889146, 1723687987, 3983212609, 4294563582, 2167504868, 4131303989, 30541827, 1847032101, 4046416791, 886984731, 358944830, 42211964, 3168821458, 1211076867, 1421058748, 1013130355, 2069454997, 3779430210, 2160036842, 2400645795, 3850228842, 3463710532, 2538873538, 1405505158, 3230075244, 245688412, 3898651951, 427677002, 3472227126, 267743468, 2245627246, 4228296001, 3063901127, 2807318768, 391618047, 823239808, 1584318905, 1579453613, 997403543, 1764763131, 1472699256, 2450503703, 261739515, 526827084, 4092732213, 1741873752, 497895734, 3392207753, 3977517516, 2887569271, 2529992687, 1221719415, 3327554247, 113661918, 4241769877, 451015713, 2342033285, 1184277155, 1489314301, 4123384057, 1132920368, 437432721, 913685165, 1925484129, 1090190256, 1383618750, 2330515266, 338100431, 627709766, 2567213954, 568760880, 149137593, 963971225, 912750668, 1743082519, 530115509, 1730692772, 2750879488, 1642212454, 3992049402, 2126902815, 2163010782, 1781522632, 2085203126, 4007264263, 723964955, 1275337085, 1169521472, 3974170437, 2615467417, 2309106671, 537031725, 1630797687, 1553216255, 1399060812, 1112021028, 3288841091, 1508036158, 744192872, 1147369365, 3964491971, 3082686983, 2017113167, 1599927836, 2504510940, 4116660910, 560351097, 1527973632, 3130259314, 3087905315, 2581843632, 1484241468, 3319499724, 3693833991, 3812658967, 2952080689, 2456484788, 285399166, 2866352648, 1929410588, 360250710, 2602635685, 719044063, 3692092492, 3978526775, 2926625573, 2484360426, 4131425768, 2432536633, 2761638805, 3836314513, 356597858, 1278720734, 1649424437, 1861916655, 3224655028, 1508896360, 336881532, 977794399, 2023346979, 2932377126, 2531952665, 2098284188, 4002328022, 3832083721, 3116464025, 3313180663, 4162917240, 802241637, 1980169014, 359925233, 2113670677, 814110330, 2070953523, 1266510215, 2832453410, 3829922378, 3739864126, 1710477925, 2946319458, 3375908310, 933695863, 347880229, 1269302116, 1183913056, 1020900670, 1411857584, 1811427321, 864459895, 916844091, 1482364269, 506057606, 3712935876, 2328269942, 3521169425, 2192820157, 22176442, 1447728893, 3537320730, 3874347462, 3543997871, 760929304, 4232176725, 1273688311, 1126452889, 1508949270, 2834035775, 978319625, 3518745531, 963480, 1844562876, 3608767420, 1922645405, 2427409295, 560090799, 3914228582, 562403051, 2895467506, 4160342092, 2400640403, 1586062546, 1727948911, 636688453, 2632459682, 4147539603, 1060496114, 1392220045, 114715597, 572941511, 4142183733, 1925432945, 335335855, 2692189346, 2753967402, 3408546647, 3220664231, 2188379244, 3968453480, 3722713854, 3880170020, 3834634009, 3652114754, 505217010, 1630964016, 2838375131, 4029856210, 1445668832, 3089413533, 444128611, 881282628, 2528808033, 1832771694, 2481239136, 1307853641, 2907584135, 1524267515, 2947013478, 1600674079, 3204172870, 2966380869, 16786239, 4125290902, 3344548977, 1544440254, 2580789726, 2641271019, 1130936490, 1189045462, 1378453560, 1543102053, 3305989421, 2678474942, 4219470166, 4068803097, 197208581, 540234917, 2959687507, 612179788, 4063006856, 553784112, 2725875649, 2433590363, 3203730746, 993361898, 1031808673, 2203741953, 1033337536, 204726970, 1097816360, 3862589176, 4232402667, 3472709511, 1952882048, 802707612, 3004227299, 3778541798, 2740767108, 724089176, 3689608439, 2595938463, 2077786960, 507860463, 3520064008, 318543445, 1444443937, 837095585, 1503544416, 1215011040, 9072081, 1989078373, 3742746541, 4095454360, 3611196247, 3100793229, 617564546, 2254333491, 3452557022, 4215820403, 2284991454, 4026046537, 2092823841, 3843589413, 588762946, 3201120103, 490388376, 3668364523, 1331856465, 714917151, 3332770498, 3953322202, 1119284145, 389701966, 19841203, 279359256, 2154072802, 3520518677, 1177165312, 3413175909, 2855839919, 2054150973, 3812689400, 3937032386, 183120664, 1538238349, 1422998930, 2450700661, 2233649402, 3645600498, 1332010287, 3213722001, 3900223002, 4174876127, 255227276, 241752154, 919896928, 3475848964, 3543181050, 646555009, 2659780675, 2989654225, 2823518802, 2299901621, 3259214603, 4127736893, 847572108, 2095656117, 3567001579, 2118804340, 3311843851, 747056621, 1497229373, 3792292943, 2605570869, 1395127771, 639495642, 3684559704, 1144008382, 1598832020, 1079774075, 1604252873, 4013700616, 3685618614, 3561094387, 1671168930, 2156551410, 1245896923, 1641177213, 1431412261, 4051858921, 3964242481, 900846560, 2075088993, 775596786, 2476905916, 2648635760, 1829773870, 4081908499, 1874211396, 2034477267, 3610792957, 1945026204, 1617344457, 3414740698, 2774287287, 4042042561, 1371858782, 3285975299, 3014047142, 219399020, 1811289578, 2546747426, 3794952230, 2616407199, 659178664, 452839981, 644484588, 3618831842, 3555083573, 3842098866, 4083101841, 387129499, 2191512888, 2107001564, 588982144, 2854070442, 3631763639, 1840230311, 265676729, 3701927, 2302123645, 2795520987, 3277278721, 3001424752, 3113094712, 3095452314, 1038685259, 4080521261, 2666218888, 1437157770, 1673503188, 337018274, 3759300102, 3738357700, 733520350, 565853502, 2083195153, 1300455347, 3493801974, 316069680, 2274789976, 3865791379, 1206297504, 319200528, 206937392, 4013686611, 545116722, 477123439, 2249566481, 196414087, 457961193, 1589564583, 3479638366, 1065661106, 179609447, 3213254729, 3901252195, 3676308627, 1010862253, 2517046198, 2037333705, 1881903526, 1094275464, 810687727, 1644041947, 2400545602, 1052834040, 1121106038, 3269988811, 106464388, 549892110, 1753402521, 249202119, 3429841671, 2047330503, 1631675380, 2593138286, 365790248, 672447557, 674660303, 1079278551, 4134822575, 2290315889, 3688356281, 3995073583, 4203056589, 998809636, 4241935872, 2552976229, 1721192811, 485049386, 1275027385, 3322575066, 2572285048, 2371982480, 1866150220, 2965420094, 240673242, 4288898419, 3789682248, 3593329681, 1263196631, 2388104963, 2252298379, 902023350, 3508664743, 597843166, 2522558877, 805716972, 1793963741, 920578445, 274009908, 1595577988, 2801045907, 3625547835, 3709586820, 3460191333, 1905466644, 1464135327, 2406535026, 936355512, 157611015, 2586224737, 1615581096, 650173611, 1226032064, 1266588890, 1054089997, 3475408923, 2714818886, 48253405, 3812068102, 276733063, 979568804, 3184644452, 3972098485, 3891772147, 3290558857, 808736677, 1525153261, 524729090, 373631980, 1245523017, 1976376576, 2354900878, 1406787568, 1053720232, 392716890, 2654583277, 1062155354, 991722775, 3833903838, 653671427, 2938939791, 55240300, 2209622499, 3407446491, 228872433, 2763642956, 3245769557, 1257178620, 4017924808, 2191433338, 2136630027, 1399349192, 3171528095, 268456624, 710861821, 1656520577, 3952909742, 3144570086, 2276605883, 1699441591, 2951651173, 878549598, 819230133, 4053629439, 1810377574, 869207813, 3370189165, 288709678, 494002815, 1841235633, 1706282786, 36196380, 3263724312, 2041112509, 1334451109, 1541506188, 2960231685, 909508816, 1364918519, 3506906261, 4100077784, 2636525026, 3728515895, 1647345277, 1733172084, 2814596348, 1065312351, 1890425055, 2165528352, 205773904, 1574853755, 4016646824, 762370041, 1775261235, 1603862364, 995260862, 3283169324, 2348948442, 1012358937, 2673073448, 316445370, 1311535543, 2726324604, 384006089, 2299262434, 2573795791, 2463632521, 3849012891, 4139899535, 2737753182, 3765117040, 2831778236, 4294105582, 688571532, 2857040204, 3708245388, 1257799323, 944183133, 624)None'
'''
# Definititon and Usage
# The getstate() method returns an object with with the current state of the random number generator.

# use this method to capture the state, use the setstate() method, with the captured state, to restore the state.

# Syntax 
random.getstate()

# parameter Values 
# No parameter values.

# Python Random setstate() Method

# Example: 
# Capture and restore the state of the random number generator:

import random

#print a random number:
print(random.random())

#capture the state:
state = random.getstate()

#print another random number:
print(random.random())

#restore the state:
random.setstate(state)

#and the next random number should be the same as when you captured the state:
print(random.random())

# Definiton and Usage;
# The setstate() method is used to restore the state of te random number generator
# back to the specified state.

# Use the getstate method to caputre the state 

# Syntax
random.setstate(state)

# Parameter Values

# Pametr Values:         Descripion:
'''
state           Requied. A state object. the setstate() method will restore the state
                of the random number generator back to tis state.
'''
# Python Random getrandbits()
# Method.

# example: 
# return an 8 bits sized integer:

import random

print(random.gettrandbits(8)) # print's 246

 # Definiton and Usage: 
# The getrandbits( ) Method returns an integer in the specified size (in bits.)

# Syntax: Error! 
random.gettrandbits(n) 

# Parameter Values

# Parameter:	Description: 
# n	            Required. A number specifying the size, in bits, of the returned integer.

# Python Random randrange() Method 

# Example: 
# Return a number between 3 nd 9:

import random
print(random.randrange(3,9)) 

# Definiton and Usage!

# The randrange() method returns a randomly selected element from the specified range.

# Syntax <---> ERROR! 
random.randrange(start,stop, step)

# Parameter Values:

'''
Paramter:       Description:
start:          Optional. An integer specifying at wich position to start.
                Default is '0'

stop:           Required. An integer specifying at which position to the end.

step:           Option. An interger specifying the incrementation.
                Default '1'
'''

# Pyhon Random randint() Method

# For a Example:
# Return a number between 3 and 9 (both included): 

import random 
print(random.randint(3,9)) 
# This will return a number between '3 to 9 which is both included'

# Definiton and Usage
# The randint() method returns an integer number selected element from the specified rang.

'''
Note: This method is an alias for randrange(start, stop+1)

Syntax: Error!!!
random.randint(start, stop)

Parameter Values!

Parameter:       Description:
start:           Requird. An integer specifying at which postion to start.

stop:            Required. An integer specifying at which positon to end.
'''

# Python Random choice() Method!

# Example:
# Return a random element from a list:

import random
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

# which print's out the following random 'list' on the closed '[]'

# Definiton and Usage
# The choice() method returns a randomly selected element from the specified sequence.
# The sequence can be a string, and a range, and a tuple or any other kind of sequence.

'''
Syntax Error!!
random.choice(sequence)

Parameter Values:

Parameter:       Description:
sequence         Requird. A sequence like a list, a range of numbers etc.
'''

# Example:
# Return a random character from a string:

import random
x = "WELCOME"
print(random.choice(x)) # print's any word in that 'x' variables.

# Python Random choices() Method!

# Example:
'''
Return a list with 14 items.
The list should contain a randomly secection of the values from a specified list, and there should be 10 times higher 
Possibilty to select "apple" than the other two:
'''

import random 
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist,weights = [10, 1, 1], k = 14))

'''
Definton and Usage

The choices() method returns a list with the randomly selected element from the specified sequence.
you can weigh the possibility of each result with the weights paramter or the cum_weights paramter.
The sequence can be a string, a range, a list, a turple or any other kind of sequence.

Syntax Error:
random.choices(sequence, weights=None, cum_weights=None, k=1)

Parameter Values 

Parameter: 	    Description:
sequence:	    Required. A sequence like a list, a tuple, a range of numbers etc.

weights:	    Optional. A list were you can weigh the possibility for each value.
                Default None.

cum_weights:     Optional. A list were you can weigh the possibility for each value, only this time the possibility is accumulated.
                Example: normal weights list: [2, 1, 1] is the same as this cum_weights list; [2, 3, 4].
                Default None.

k:          	Optional. An integer defining the length of the returned list
'''

# Python Random shuffle() Method

# Example:
# Shuffle a list (reorganize the order of the list items):

import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist) # print's out ['banana', 'cherry', 'apple']

'''
Definiton and Usage!!! 

The shuffle() method takes a sequence, like a list and reorganize the order of the items.

Note's !!!!!: This method changes the original list, it does not return a new list.

Syntax: random.shuffle(sequence) 

Parameter Values:

Parameter: 	       Description:
Sequence:          Required. A sequence.

Function:          Deprecated since Python 3.9. Removed in Python 3.11.
                   Optional. The name of a function that returns a number between 0.0 and 1.0.
                   If not specified, the function random() will be used
'''

# More Examples!
# This example uses the function parameter, which is deprecated since Python 3.9 and removed in Python 3.11.
# You can dfine your own function to weigh or specify the result.
# If the funcition returns the same number each time, the result will be in the same order each time:

import random
def myfucntion():
    return 0.1
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist,myfucntion)
print(mylist) # Then print's a random shuffle ["banana", "cherry", "apple"] 

                    # Python Random sample() Method:

# For a Example !!!

# Return a list that contains any 2 of the items from list:

import random
mylist = ["apple", "banana", "cherry"]
print(random.sample(mylist, k=2))
# This gives us a 2 from the list like random one.

'''
Definition and Usage:

The sample() method returns a list with a randomly selection of a specified number of items from a sequnce.

Note's: This method dose not change the Original sequence.

Syntax ERROR !!!:
random.sample(sequence, k)

Parameter Values:

Parameter: 	    Description:
Sequence:       Required. A sequence. Can be any sequence: list, set, range etc.

k:              Requird. The size of the returned list.
'''

             # Python Random random() Method:

# Example:

# Return random number between 0.0 and 1.0:

import random
print(random.random()) # This print's from 0.0 to 1.0:

'''
Definition and Usage: The random() method returns a random floating number between 0 and 1.

Syntax Error !!!!

random.random()

Parameter Values: No parameters
'''

                # Python Random uniform() Method

# Example! 
# Return a random numhber between, and included, 20 and 60:

import random
print(random.uniform(20,60)) # This can print any number between '20, to 60'

'''
Definiton of the Usage:

The uniform() method returns a random floating number between the two specified numbers (both included.)

Sytax Error:
random.uniform(a, b)

Parameter Values:

Parameter:       Descrition:
a:               Required. A number specifying the lowest possible outcome

b:               Required. A number specifying the highest possible oucome
'''

                    # Python Random Triangular() Method

# Example code:
# Return a random number between, and included, 20 and 60, but most likly closer to 20:

import random

print(random.triangular(20, 60, 30))

'''
Definition and Usage

The triangular() method returns a random floating number between the two specified numbers (both included), but you can also specify a third parameter, the mode parameter.

The mode parameter gives you the opportunity to weigh the possible outcome closer to one of the other two parameter values.

The mode parameter defaults to the midpoint between the two other parameter values, which will not weigh the possible outcome in any direction.

Syntax Error !!! 
random.triangular(low, high, mode)

Parameter Values

Parameter 	Description
low:	    Optional. A number specifying the lowest possible outcome.
            Default 0
high: 	    Optional. A number specifying the highest possible outcome.
            Default 1
mode: 	    Optional. A number used to weigh the result in any direction.
            Default the midpoint between the low and high values
'''

