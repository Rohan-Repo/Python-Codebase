# Functions Avaliable
print( 'Readymade Functions Avaliable:' )
numList = [ -123, 18,14,22,10, -50, 0, 79, -32, 111 ]

print( '\n \t Numbers List : ', numList )
print( '\t Numbers Items Count : ', len(numList) )
print( '\t Minimum Value from List : ', min(numList) )
print( '\t Maximum Value from List : ', max(numList) )
print( '\t Sum of Numbers from List : ', sum(numList) )
print( '\t Average of Numbers from List : ', sum(numList)/len(numList) )

torAirport1 = 'Pearson'
torAirport2 = 'Billy Bishop'

print( '\n \t torAirport1:', torAirport1, ', torAirport2:', torAirport2 )
print( '\t Pearson in Upper-Case : ', torAirport1.upper() )
print( '\t Billy Bishop in Lower-Case : ', torAirport2.lower() )
print( '\t Pearson Swap Case : ', torAirport1.swapcase() )
print( '\t Billy Bishop Swap Case : ', torAirport2.swapcase() )

# Range Function

print( 'Range Function Example :')
print( 'End:' )
for i in range(5):
    print( i, end=' , ' )

print( '\n Start, End:' )
for i in range(10, 15 ):
    print( i, end=' , ' )

print( '\n Start, End, Step :' )
for i in range(30, 60, 3 ):
    print( i, end=' , ' )

print( '\n EndLine and Separator Restored to Default' )

def say_hello():
    print( 'Hello Coders!' )

# say_hello()

primeFlag = True

def prime_check():
    for i in range(4, 30 ):
        print( i )
        for j in range( 2, int(i/2)+1 ):
            print( '\t', j )
            if i % j != 0:
                primeFlag = True
                continue
            else:
                primeFlag = False
                break
        print( '=aa', j, '- ', int(i/2), '------', i )

        if j == int(i/2):      
            print( '=', i )        
        print( '=aa', j, '- ', i, '-----', primeFlag )


# prime_check()

print( 'Prime Nums 2:' )
def prime_check2():
    for i in range(2, 30 ):
        # print( i )
        for j in range( 2, int(i/2)+1 ):
            # print( '\t', j )
            if i % j != 0:
                continue
            else:
                break
        # print( '=aa', j, '- ', int(i/2), '------', i )

        if ( i == 2 or i==3 ) or j == int(i/2):
            if i == 4:
                continue
            else:
                print( '\t', i )        
prime_check2()