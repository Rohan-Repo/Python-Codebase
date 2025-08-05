numList = []

import random

for i in range(15):
    numList.append( random.randrange( -111, 111 ) )

print( '\n Numbers List : ', numList )

# Short-cut, Internally Linear Search
if 18 in numList:
    print( '18 present in numList' )

if 99 in numList:
    print( '99 present in numList' )

print( 'Linear Search Algorithm!' )

num_to_find = int( input('\t Enter the Number to Find: ' ) )

# Iterate through the whole list from left-to-right until we find our value
for i in range( len(numList) ):
    print( '\t\t', i, ' : ', numList[i] )

    if numList[i] == num_to_find:
        print( '\n \t', num_to_find, ' was found in the List!' )
        break
# If we have exhaustively searched through the list & nothing happened then the else clause will be run
else:
    print( '\n \t', num_to_find, ' was NOT FOUND in the List!' )