# Loops

print('While Loop Example:')
num = 0
while num < 5:
    print( num, end=',' )
    num = num + 1

print('\n For Loop Example #1:')
for i in range(5):
    print( i, end=',' )

dayList = [ 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun' ]
print('\n For Loop Example #2:')
for i in range( 7 ):
    print( i, ' : ', dayList[i], end='\t' )

print('\n ForEach Loop Example :')
for day in dayList:
    print( day, end=' , ' )


print('\n Conditional Example:')
# Make decision based on Condition

ageList = [ 30, 15, -27 ]

for age in ageList:
    if age >= 18:
        print( "Person with age : ", age, " is Allowed to Vote" )
    elif age < 0:
        print( "Person with age : ", age, ' is Not Even born yet!' )
    else:
        print( "Person with age : ", age, " is Not Allowed to Vote " )
