numList = []

print( 'Binary Search Algorithm!' )

import random

for i in range(13):
    numList.append( random.randrange( -255, 256 ) )

print( '\n Initial Numbers List : ', numList )

numList.sort()

print( '\n Sorted Numbers List : ', numList )

num_to_find = int( input('\n Enter the Number to Find: ' ) )

start = 0
end = len( numList ) - 1

for i in range( len(numList) ):
    
    # Since we need a Decimal Value and not a Float one, we do Floor Division
    mid_point = (start + end) // 2
    
    print( '\n start : ', start, ' , end : ', end, ' , mid_point : ', mid_point  )
    print( '\t Internal List : ', numList[ start: end+1 ] )

    # Is the number at the mid-position?
    if numList[ mid_point ] == num_to_find:
        print( '\n \t', num_to_find, ' was found at Position #', mid_point )
        break

    # Start cannot be > End - Stopping Condition
    elif start > end:
        print( '\n \t', num_to_find, ' was NOT FOUND in the List!' )
        break
    
    # If num_to_find > mid-point , Change the Start point 
    elif num_to_find > numList[ mid_point ]:
        start = mid_point + 1
    
    # If num_to_find < mid-point , Change the End point    
    elif num_to_find < numList[ mid_point ]:
        end = mid_point - 1