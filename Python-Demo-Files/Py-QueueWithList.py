# Queue using List
queueList = [ 'Jessica', 'Harvey', 'Louis' ]
print( 'Original Queue : ', queueList )

print( 'Enqueue - Add to the Last or append()' )
queueList.append( 'Mike' )
print( 'After Person #1 : ', queueList )
queueList.append( 'Robert' )
print( 'After Person #2 : ', queueList )

print( 'Dequeue - Remove the first or pop(0)' )
for i in range( len(queueList)+1 ):
    print( 'Round #:', i, ' : ', queueList )
    if len(queueList) != 0 :
        queueList.pop( 0 )