"""
#1 : Typecasting: 
    Conversion of one data-type into other data-type is called type-casting or type-conversion
    Examples: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict() etc.

#2: Data-Type Conversion:
    Implicit Data-Type Conversion: 
        Automatic Data Conversion handled by the Compiler [By Compiler]
        A lower-order data-type gets converted into a higher-order data-type Eg. int to float
    Explicit Data-Type Conversion: Instruct the compiler to change the data-type [By Developer]

#3: User-Input:
    We take user input using the input() function. This returns a String
    Waits for User Input via Keyboard
"""

print( ' Taking User Input:' )

inpVal = input( 'Enter your home-town:' )
print( '\t Home-town is: ', inpVal, '\t\t Type:', type(inpVal) )

print( 'Type-Casting or Type-Conversion:')

c = 5
d = 7
res = c+d
print( '#1 : \t\t', c, '+', d, '=', res )
print( 'Type of C: ', type(c), '\t Type of D:', type(d), '\t Type of result:', type(res)  )

a = input( 'Enter Number #1:' )
b = input( 'Enter Number #2:' )
res = a+b

# String Concatenation
print( '#2 : \t\t', a, '+', b, '=', res )
print( 'Type of A: ', type(a), '\t Type of B:', type(b), '\t Type of result:', type(res)  )

# Typecasting addition
res = int(a+b)
print( '#3 : \t\t', a, '+', b, '=', res )
print( 'Type of A: ', type(a), '\t Type of B:', type(b), '\t Type of result:', type(res)  )

# Individual Number Typecasting
res = int(a)+int(b)
print( '#4 : \t\t', a, '+', b, '=', res )
print( 'Type of A: ', type(a), '\t Type of B:', type(b), '\t Type of result:', type(res)  )

# Implicit & Explicit Typecasting
intRes = 5 * 9
floatRes = 6.2 - 1.2

# Implicit Data-Type Conversion
numRes = intRes/floatRes
print( '\n Implicit Data-Type Conversion:' )
print( '#5 : \t\t', intRes, '/', floatRes, '=', numRes )
print( 'Type of intRes: ', type(intRes), '\t Type of floatRes:', type(floatRes), '\t Type of numRes:', type(numRes)  )

print( '\n Explicit Data-Type Conversion:' )

stringVal = 'Canada'
# Explicit Data-Type Conversion

# strRes2 = stringVal + '->' + numRes
# TypeError: can only concatenate str (not "float") to str

strRes2 = stringVal + '->' + str(numRes)
print( '#6 : \t\t', stringVal, '+', numRes, '=', strRes2 )
print( 'Type of stringVal: ', type(stringVal), '\t Type of numRes:', type(numRes), '\t Type of strRes2:', type(strRes2)  )
