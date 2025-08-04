# Stack using List
stackList = [ 'Shell Scripting', 'Enterprise Infrastructure' ]
print( '\nOriginal Stack : ', stackList )

print( 'PUSH - Add to the Last or append()' )
stackList.append( 'Linux Kernel' )
print( 'After Book #1 : ', stackList )
stackList.append( 'Windows OS' )
print( 'After Book #2 : ', stackList )

print( 'POP - Remove from top of the Stack or pop()' )
for i in range( len(stackList)+1 ):
    print( 'Round #:', i, ' : ', stackList )
    if len(stackList) != 0 :
        stackList.pop()

