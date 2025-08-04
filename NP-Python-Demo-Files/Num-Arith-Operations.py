numList = []

for i in range( 1, 10, 2 ):
    numList.append( i )

for j in range( 0, 10, 2 ):
    numList.append( j )

print( '\t Numbers Sort Initially : ', numList )
numList.reverse()
print( '\t Numbers Sort Reversed : ', numList )
numList.sort()
print( '\t Numbers Sort Ascending : ', numList )
numList.sort(reverse=True)
print( '\t Numbers Sort Descending : ', numList )

print( '\t Sum of All Numbers : ', sum(numList) )
print( '\t Count of List Items  : ', len(numList) )
print( '\t Average of All Numbers : ', sum(numList)/len(numList) )

numSquares = []
numCubes = []
numSqrRoot = []
numCubeRoot = []

for num in numList:
    numSquares.append( num ** 2 )
    numCubes.append( num ** 3 )
    numSqrRoot.append( round(num ** (1/2), 3) )
    numCubeRoot.append( round(num ** (1/3), 3) )

print( '\t Nums : ', numList )
print( '\t Squares : ', numSquares )
print( '\t Square-Roots : ', numSqrRoot )
print( '\t Cubes : ', numCubes )
print( '\t Cube-Roots : ', numCubeRoot )