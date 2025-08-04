"""
Arithmetic Operations:
    + : Addition
    - : Subtraction
    * : Multiplication
    / : Division
    % : Remainder
    // : Floor-Division (Remove the decimal part of the Division and Print the Value)
    ** : Exponential (Power)
"""
num1 = float( input( 'Enter Number #1:' ) )
num2 = float( input( 'Enter Number #2:' ) )

print( "The Numbers you entered are : Number #1: ", num1, " & Number #2: ", num2 )
print( "Addition:\t\t", num1, " + ", num2, " = ", num1+num2 )
print( "Subtraction:\t\t", num1, " - ", num2, " = ", num1-num2 )
print( "Multiplication:\t\t", num1, " * ", num2, " = ", num1*num2 )

if num2 != 0:
    print( "Division:\t\t", num1, " / ", num2, " = ", num1/num2 )
    print( "Floor-Division:\t\t", num1, " // ", num2, " = ", num1//num2 )
    print( "Modulus/Remainder:\t", num1, " % ", num2, " = ", num1%num2 )
else:
    print( "Division by Zero, Not allowed, Skipping Division Operations" )

print( "Exponential/Power:\t", num1, " ** ", num2, " = ", num1**num2 )