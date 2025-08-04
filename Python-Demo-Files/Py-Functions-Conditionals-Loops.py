# Functions : 
# Used to avoid writing repetative code by creating functions 
# Types : 
    # User-Defined : Functions without parameters, Functions with parameters
    # Built-In Function : Packaged with your Python distribution 

print( 'Functions without parameters:' )
def say_hello():
    print( '\t Hello Everyone!' )

# Defined the method but won't get an O/P until we call the function 
# say_hello()

# Customize Code and O/P as per requirement
print( 'Functions with parameters:' )
def greetUser( msg ):
    print( '\t Parameter passed: ', msg )

greetUser( 'Bonjour!' )
greetUser( "¡Buenos días!" )

# Conditional:
# Make decision based on Condition

print('\n Conditional Example:')
ageList = [ 30, 15, -27 ]

for age in ageList:
    if age >= 18:
        print( "Person with age : ", age, " is Allowed to Vote" )
    elif age < 0:
        print( "Person with age : ", age, ' is Not Even born yet!' )
    else:
        print( "Person with age : ", age, " is Not Allowed to Vote " )

# Loops - Perform the same task over and over again
dayList = [ 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' ]
print( 'Original  List : ',  dayList ) 
print( 'Built-In Function:' )
print( '\t Size of List Before : ', len(dayList) ) # Built-In Function Eg. 1 
dayList.append( 'Sun' ) # Built-In Function Eg. 2 
print( 'Final  List  : ',  dayList ) 
print( '\t Size of List After: ', len(dayList) )

print('While Loop Example:' )
num = 0
while num < len(dayList):
    print( dayList[num], end=',' )
    num = num + 1

print('\n For Loop Example #2:')
for i in range( 7 ):
    print( i, ' : ', dayList[i], end=' , ' )

print('\n ForEach Loop Example :')
for day in dayList:
    print( day, end=' , ' )


# Extra Conditional Example
print( 'Functions with parameters and Conditional:' )
def greet_user( lang='en' ):
    # If lang is fr Greet in French
    if lang == 'fr':
        print( '\t', lang, ' : ', 'Bonjour!' )
    # If lang is es Greet in Spanish
    elif lang == 'es':
        print( '\t', lang, ' : ', "¡Buenos días!" )
    # else if nothing passed assume it's in English
    else:
        print( '\t', lang, ' : ', 'Good Morning!' )

greet_user( 'es' )
greet_user()
greet_user( 'fr' )
