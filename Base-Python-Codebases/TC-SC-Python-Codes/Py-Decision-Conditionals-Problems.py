# Problem #1
n1 = 3
n2 = n1
n3 = n1

if n1 == n2 and n2 == n3 and n1 == n3:
    print( 3 * (3 * n1 ) )

n1 = 1

if n1 == n2 or n2 == n3 or n1 == n3:
    print( 2 * (n1+n2+n3) )
    
n2 = 2
n3 = 3
    
if n1 != n2 and n2 != n3 and n1 != n3:
    print( n1+n2+n3 )
    
# Problem 3
a = 20
b = 10
c = 30
n = 5

print( (a ** n) + (b ** n ) )
print (c ** n ) 
print(  (  (a ** n) + (b ** n ) != (c ** n ) ) )

if n >= 2 and (  (a ** n) + (b ** n ) != (c ** n ) ):
    print( 'Theorom Holds' )
else:
    print( 'Nope!' )
    
# Problem 5
# Use Conditionals for validations

import datetime

# Program
date = datetime.datetime( 2023, 12, 1 )
newDate = date + datetime.timedelta( days=1 )
print( date )
print( newDate )

# Problem 6
# import random

# for i in range(10):
#     print( random.randrange(1, 36) )
#     # bets.append( random.randrange(1, 36) )

bets = [ 7, 14, 28, 11, 6, 16, 4, 15, 4, 9, 45, 0 ]

# Solution 1 
for i in bets:
            
    if i >= 1 and i <=12:
        if i % 2 == 0:
            print( i, ':', 'Red & Low' )
        else:
            print( i, ':', 'Black & Low' )
    elif i > 12 and i <=24:
        if i % 2 == 0:
            print( i, ':', 'Red & Medium' )
        else:
            print( i, ':', 'Black & Medium' )
    elif i > 24 and i <=36:
        if i % 2 == 0:
            print( i, ':', 'Red & High' )
        else:
            print( i, ':', 'Black & High' )
    else:
        print( ' Out of Range' )
    
# Solution 2 - Short
for i in bets:
    print( '--' )
    if i % 2 == 0:
        print( i, ':', 'Red' )
    else:
        print( i, ':', 'Black' )
        
    if i >= 1 and i <=12:
        print( i, ':', 'Low' )
    elif i > 12 and i <=24:
        print( i, ':', 'Medium' )
    elif i > 24 and i <=36:
        print( i, ':', 'High' )
    else:
        print( i, ':', 'Out of Range' )
    
    