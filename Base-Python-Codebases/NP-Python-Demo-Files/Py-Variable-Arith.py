# Install Python - Blog: https://www.wikihow.com/Install-Python

# Python Comment starts with a # and comments are never executed they are used for information

# Variable is nothing but a place to store your data

# Store integers
num = 123 
print( 'Value : ', num, '\t Type : ', type(num) )

# Constant's in Capitals is a Convention
# Store floating point values
PI = 3.141592 
print( 'Value : ', PI, '\t Type : ', type(PI) )

# Store Strings - Series of Characters
city = 'Toronto' 
print( 'Value : ', city, '\t Type : ', type(city) )

# Store Boolean Values True or False
isValid = True 
print( 'Value : ', isValid, '\t Type : ', type(isValid) )

# Basic Calculator - Arithmetic Operations
# Take user Input in String Format with input(msg)
num1 = input( 'Enter Number 1: ' )
num2 = input( 'Enter Number 2: ' )
# num1 = 20
# num2 = 7

# Since I/P is String this is String Concatenation not Addition
print( 'Not Addition of Numbers but Concatenation = ', num1+num2) 

# let's typecast[Convert] to Integer
num1 = int( num1 )
num2 = int( num2 )

print( 'Basic Calculator:' )
print( '\t Addition = ', num1 + num2 )
print( '\t Subtraction = ', num1 - num2 )
print( '\t Multiplication = ', num1 * num2 )
print( '\t Division = ', num1 / num2 )
print( '\t Division Rounded to 2 Decimal Places = ', round( (num1/num2), 2 ) )
print( '\t Remainder = ', num1 % num2 )
print( '\t Power = ', num1 ** num2 )
# the floor division // rounds the result down to the nearest whole number 
print( '\t Floor Division = ', num1 // num2 )