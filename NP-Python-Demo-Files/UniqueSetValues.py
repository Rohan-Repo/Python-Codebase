# Normal:
listEg = [ 'Canada', 'India', 'USA', 'Germany', 'UK' ]
listEg_2 = list( listEg ) + listEg
print( 'List Values : ', listEg_2 )
print( 'Set Values : ', set(listEg_2) )

# Extra 
languagesKnown = [ ['C'] * 1, ['Java'] * 5, ['SQL'] * 4, ['Python'] * 2 ]

print( languagesKnown )

uniqueVals = []

for lang in languagesKnown:
    print( 'For Lang : ', lang )
    print( 'Set = ', set(lang) )

