#0
print( 'Conditional Example:' )
name = input('\t Name: ')
age = int( input('\t Age: ') )

if age >= 18:
    print( '\t', name, 'with age: ', age, 'is Eligible for Voting!' )
elif age <= 0:
    print( '\t', name, 'with age: ', age, 'is Not Even born yet!' )
else:
    print( '\t', name, 'with age: ', age, 'is Not Eligible for Voting' )

#1
coldOutside = True

if coldOutside:
    print( 'Wear a Coat' )
else:
    print( 'Enjoy the Sun' )
  
# 2  
temp = 120

if temp < 40:
    print( temp, 'A little cold' )
else:
    print( temp, 'Nice Weather' )

# 3
marks = [ 75, 65, 55, 45, 95 ]

for i in marks:
    if i == 100:
        print( i, ': PERFECT' )
    elif i >= 90:
        print( i, ': A Grade' )
    elif i>= 80:
        print( i, ': B Grade' )
    elif i>= 70:
        print( i, ': C Grade' )
    elif i>= 60:
        print( i, ': D Grade' )
    elif i < 60:
        print( i, ': F Grade' )

# 4
# sal = [ 75000, 65000, 25000, 15000, 95000 ]
# yearOnJob = [ 2, 1, 3, 1, 5 ]

sal = float( input('Sal:') )
yearOnJob = int( input('Year:') )

if sal >= 30000:
    if yearOnJob >= 2:
        print( 'Qualify for Loan' )
    else:
        print( 'Min Two Years Req to Qualify for Loan' )
else:
    print( 'Less Salary, Not Eligible' )
    
# 5

opt = [ 'y', 'Y',  'yeah', 'No', 'NO', 'Nope' ] 

print( 'If-Else' )
for op in opt:
    if op == 'Y' or op == 'y' or op == 'yes' or op == 'YES':
        print( '\t', op, 'Yeah!' )
    elif op == 'n' or op == 'N' or op == 'NO' or op == 'no':
        print( '\t', op, 'Nope!' )
    else:
        print( '\t', op, 'N/A!' )

print( 'Solution 1' )

option_y = [ 'y', 'Y',  'yes', 'YES', 'yES', 'YeS', 'YEs', 'yeS', 'Yes', 'yEs' ]

option_n = [ 'N', 'n', 'No', 'NO', 'no', 'nO', ]

for op in opt:
    if op in option_y:
        print( '\t', op, 'Yeah!' )
    elif op in option_n:
        print( '\t', op, 'Nope!' )
    else:
        print( '\t', op, 'N/A!' )
    
print( 'Solution 2' )

for op in opt:
    
    op = op.lower()
    
    if op == 'y' or op == 'yes':
        print( '\t', op, 'Yeah!' )
    elif op == 'n' or op == 'no':
        print( '\t', op, 'Nope!' )
    else:
        print( '\t', op, 'N/A!' )
        