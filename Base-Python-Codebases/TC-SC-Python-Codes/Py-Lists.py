numList = [ -123, 18,14,22,10, -50, 0, 79, -32, 111 ]

print( '\t Numbers Sort Initially : ', numList )
numList.reverse()
print( '\t Numbers Sort Reversed : ', numList )
numList.sort()
print( '\t Numbers Sort Ascending : ', numList )
numList.sort(reverse=True)
print( '\t Numbers Sort Descending : ', numList )