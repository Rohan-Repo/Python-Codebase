# Lists : Values can be updated
listEg = [ 'A', 'E', 'I', 'O', 'U' ]
print( 'Value : ', listEg, '\t Type : ', type(listEg) )

listEg.append( 'E' )
listEg.append( 'A' )
print( 'Value : ', listEg, '\t Type : ', type(listEg) )

# Tuples : Values are unchangeable
tupleEg = tuple( listEg )
print( 'Value : ', tupleEg, '\t Type : ', type(tupleEg) )

# tupleEg.count() and tupleEg.index() are the only methods present in Tuples no add() or append()

# If we want to add Values to tuples - Workaround - Create a new Tuple and Concatenate 
temp = ('I', 'O')
tupleEg = tupleEg + temp
print( 'Value : ', tupleEg, '\t Type : ', type(tupleEg) )

# Sets : Stores Unique Values together
setEg = set( tupleEg )
print( 'Value : ', setEg, '\t Type : ', type(setEg) )

# Dictionary : Stores Key Value Pairs
dictEg = { 'city': 'Toronto', 'province': 'Ontario', 'Country': 'Canada' }

print( 'DS Type: ', type(dictEg) )

print( 'Items: ' )
for key, value in dictEg.items():
    print( '\t', key, ' : ', value )