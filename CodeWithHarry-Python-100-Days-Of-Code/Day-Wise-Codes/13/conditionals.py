"""
Conditional Flow Statements are used to Alter the Flow of a given Program
Conditionals : >, >=, <, <=, ==, !=
Indentation Specifies to the Compiler that a new block of Code is starting
"""
ageList = [30, 15, 27, 12, 18]

for age in ageList:
    if age >= 18:
        print( "Person with age : ", age, " is Allowed to Vote" )
    else:
        print( "Person with age : ", age, " is Not Allowed to Vote " )


# Separate Even-Odd Numbers and Eliminate Zero
numList = [1,-6,-19,30,-31,12,98, 0]
evenList = []
oddList = []

for num in numList:
    if num == 0:
        continue
    elif num%2 == 0:
        evenList.append( num )
    else:
        oddList.append( num )

print( 'Original List: ', numList )
print( 'Odd Numbers List: ', oddList, '\t Even Numbers List: ', evenList )