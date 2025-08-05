# Python Comment starts with a #

# Variable is nothing but a place to store your data
city = 'Toronto'
province = 'ON'

# print() Automatically provides spaces in between two separating values and a new line character at the end
print( 'You Live in 1:', city, ' , ', province )
print( 'You Live in 2:', city, province )

# Constant's in Capitals is a Convention
PI = 3.141592
# print( 'Constant's Value : )
print( "Constant's Value :", round( PI, 4) )

# Basic Calculator
num1 = input( 'Enter Number 1: ' )
num2 = input( 'Enter Number 2: ' )

print( 'Addition = ', num1 + num2 )

# Addition =  1213

# Because input() by default takes input as a String so it's actually Concatenating the Strings 
# Instead we need to TypeCast the Numbers to int or float

# 20 & 6 or 20 & 7

print( 'Basic Calculator:' )
num1 = float( input( '\t Enter Number 1: ' ) )
num2 = float( input( '\t Enter Number 2: ' ) )

print( '\t Addition = ', num1 + num2 )
print( '\t Subtraction = ', num1 - num2 )
print( '\t Multiplication = ', num1 * num2 )
print( '\t Division = ', num1 / num2 )
print( '\t Remainder = ', num1 % num2 )
print( '\t Power = ', num1 ** num2 )
# the floor division // rounds the result down to the nearest whole number 
print( '\t Floor Division = ', num1 // num2 )

torAirport1 = 'Pearson'
torAirport2 = 'Billy Bishop'

print( 'EndLine and Separator Changed:' )
print( 'torAirport1:', torAirport1, 'torAirport2:', torAirport2, sep=';', end='\t\t' )
print( 'torAirport1:', torAirport1, 'torAirport2:', torAirport2 )
print( 'EndLine and Separator Restored to Default' )
print( '---END---', '---Code---' )