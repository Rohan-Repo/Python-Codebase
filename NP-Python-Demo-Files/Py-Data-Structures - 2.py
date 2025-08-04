# Lists : Values can be updated
listEg = [ 'Canada', 'India', 'USA', 'Germany', 'UK' ]
print( 'Value : ', listEg, '\t Type : ', type(listEg) )

listEg.append( 'UAE' )
listEg.append( 'South Korea' )
print( 'Value : ', listEg, '\t Type : ', type(listEg) )

# Tuples : Values are unchangeable
# tupleEg.count() and tupleEg.index() are the only methods present in Tuples no add() or append()
tupleEg = ( 'A', 'E', 'I', 'O', 'U' )
print( 'Value : ', tupleEg, '\t Type : ', type(tupleEg) )

# Sets : Stores Values in an unordered way together but Stores Unique Values
setEg = { 'ON', 'NS', 'AB', 'QC', 'BC', 'MB', 'ON', 'NS', 'AB', 'QC', 'BC', 'MB', 'ON', 'NS', 'AB', 'QC', 'BC', 'MB' }
print( 'Value : ', setEg, '\t Type : ', type(setEg) )

# Dictionary : Stores Key Value Pairs
dictEg = { 'Canada': 'CAD', 'India' : 'INR', 'USA' : 'USD', 'UK' : 'GBP' }

print( 'DS Type: ', type(dictEg) )

print( 'Items: ' )
for key, value in dictEg.items():
    print( '\t', key, ' : ', value )