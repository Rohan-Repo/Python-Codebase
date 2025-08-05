"""
Basic Data-Types - bool, float, int and str
In C or Java we need to have long or short for variables types like ints or floats but in 
Python by default they are of a bigger range (more bits in memory) so it's just int & float
more datatypes - range [Loop], tuple[x,y pairs], list[Arrays], dict[Key,Value Pairs], set [Like Mathematical Set, eliminates duplicates]

For Increment Decrement Operator ++ is replaced by (+= 1) and -- is replaced by (-= 1)

For Loop in C & Java, for( int i=0; i<3; i++ ) is replaced by (for i in [0, 1, 2]:) OR in short [for i in range(3):]
Range gives each value one by one for each iteration so memory has to be created for only that value and not the 
entire length increasing efficiency and reducing computation time
Eg. Handing you one card out of 52 at a time instead of giving the whole deck of cards together

A struct in C can only hold data whereas Python being an OOP Language it can hold data (class members) 
as well as behaviour (member functions) 

Python Strings are immutable i.e. they cannot be changed, so Yes and yes are two different strings  

Python variables are also available outside of the scope

By Default print() gives a Space between each of the Argument passed and a new line at the end

Print something n number of times just multiply by n Eg. print( '*' * 5 ) to get [*****] OR print( '?' * 3 ) [???]

Python Checks String Value and not compares the Memory Address like C so == checks value
"""

print("Hello, World")

from cs50 import get_string

name = get_string( "Enter Name:" )
print( 'Hello, ' + name )
print( 'Hello, ', name )
print( 'Hello, {name}'  )
print( f'Hello, {name}'  )

# print( range(2), ' === ', range(3)  )
# for i in range(2):
#     print(i)

# for i in range(3):
#     print(i)

"""
O/P:
Enter Name:David
Hello, David
Hello,  David   [Extra space provided]
Hello, {name}   [Value not Interpolated as we forgot the f before the String]
Hello, David    [name variable's value is interpolated because of the f-string]
"""

# Input could be in multiple formats but we cant check every combination, so convert everything to lower case or upper case
ans = input( 'Say Yes or No? ' )
if ans in [ "yes", "YES", "y", "Y", "yES", "YEs" ]:
    print( 'Agree' )
elif ans in [ "no", "NO", "n", "N", "No", "nO"]:
    print( 'Disagree' )

# Rewrite it as follows

ans = input( 'Say Yes or No? ' )
if ans.lower() in [ "yes", "y" ]:
    print( 'Agreed' )
elif ans.lower() in [ "no", "n" ]:
    print( 'Disagreed' )

# sayWoof()
# This will give an error : NameError: name 'sayWoof' is not defined

def sayWoof():
    print( 'Dog barks Woof' )

def sayMeow():
    print( 'Cat says Meow' )

# This will work perfectly
sayWoof()

def animalSays(animalType):
    print( ' Inside animalSays() - ' + animalType )
    if animalType == 'dog':
        sayWoof()
    elif animalType == 'cat':
        sayMeow()
    else:
        print( 'Incorrect Animal-Type entered' )

animalSays('dog')
animalSays('cat')
animalSays('horse')

# Print something n number of times just multiply by n
print( '*' * 5 )
print( '?' * 7 )
print( 'Chandler', 'Muriel','Bing' )
print( 'Chandler', 'Muriel','Bing',  sep='-' )

str2 = input( 'Enter String: ' )
print( str2, ' - ', str2.upper(), ' - ', str2.capitalize() )

from sys import argv

print( 'Len: ', len(argv) )
for i in range( len(argv) ):
    print( argv[i], end=',' )

print()

for i in argv:
    print( i, end='!' )

print()

# For I/P:- python print-dataTypes-loops.py C M B R

# Len:  5
# print-dataTypes-loops.py,C,M,B,R,
# print-dataTypes-loops.py!C!M!B!R!

s1 = "David"
s2 = "David"

if s1 == s2:
    print( 'Same' )
else:
    print( 'Diff')