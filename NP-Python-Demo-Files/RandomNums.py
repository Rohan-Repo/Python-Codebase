numList = []

cnt = int( input( 'Enter Count : ' ) ) 
start = int( input( 'Enter Start : ' ) ) 
end = int( input( 'Enter End : ' ) ) 

import random

for i in range( cnt ):
    numList.append( random.randrange( start, end ) )

print( '\n Numbers List : ', numList )