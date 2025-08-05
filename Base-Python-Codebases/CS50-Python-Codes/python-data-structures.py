"""
Python automatically shrinks or expands the array based on the Input provided and Memory Handling is done by the Python Interpreter
languagesKnown = [ ['C'] * 1, ['Java'] * 5, ['SQL'] * 4, ['Python'] * 2 ] - Generate Lists like this
Indexing works on all Iterable Data Structures like Strings, Lists, Dictionaries, Sets
"""
scores = [ 72, 75, 82, 95, -28, 11 ]
print( 'Sum =', sum(scores) )
print( 'Avg =', round(sum(scores)/len(scores), 2) )

provinces = ['ON', 'AB', 'BC', 'SK', 'NS' ]
print( provinces )

# province_to_search = input( 'Enter province_to_search: ' )
#
# for p in provinces:
#     if p == province_to_search:
#         print( 'province found' )
#         break
#     else:
#         print( 'province NOT found' )
#
# # This essentially does the same job as Linearly searching the value in the list
# if province_to_search in provinces:
#     print( 'province found' )
# else:
#     print( 'province NOT found' )

dict_phone_num = {
    "David":"(647) 123-9876",
    "Carter":"(617) 495-1234",
    "Joey": "(987) 654-3210",
    "Raj": "+91-1234567890",
}

print( "dict_phone_num: ", dict_phone_num )
# name = input('Enter Name to search? ')
#
# if name in dict_phone_num:
#     print( name, ' - ', dict_phone_num[name] )
# else:
#     print( 'Person NOT found' )

# Slice String to remove the $ sign and convert to a number
currVals = [ '$100', '$15', '$87', '$788' ]
for val in currVals:
    print( val, ' $ removed using val[1:]:- ', val[1:])

languagesKnown = [ ['C'] * 1, ['Java'] * 5, ['SQL'] * 4, ['Python'] * 2 ]

print( 'Provinces:', provinces )
print( 'Prices:', currVals )
print( 'languagesKnown:', languagesKnown )


