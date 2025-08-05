for i in range( 100,200,25 ):
    
    print( '\n' )

    for j in range( 600, 1000, 100 ):
        print( i, '\t', j )

list1 = [ [1,2,3], [4,5,6], [7,8,9] ]

for i in range(3):
    
    print( '\n' )

    for j in range(3):
        print( '[', i, ',', j, ']', end='\t' )
        print( list1[i][j], end='\t' )

import turtle
import time

t = turtle.Turtle()


time.sleep( 5 )
t.screen.bgcolor('cyan')
t.color( 'red' )
t.pensize(5)
t.shape('turtle')
# t.home()

time.sleep( 5 )
t.color( 'green' )
t.forward(100)
t.left(90)
t.penup()

time.sleep( 5 )
t.color( 'brown' )
t.forward(100)
t.right(90)
t.pendown()

time.sleep( 5 )
t.color( 'blue' )
t.forward(100)

t.home()
t.color( 'yellow' )
time.sleep( 5 )

