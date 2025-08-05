"""
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression 
and then calculates and outputs the result as a floating-point value formatted to one decimal place. 
Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein
x is an integer  AND y is +, -, *, or / AND  z is an integer
"""
calc_val = input('Enter I/P:').strip().split() # Remove Whitespaces before Split & Default Separator = Space

if len(calc_val) > 3:
    print( 'Invalid Input' )
else:
    calc = 0

    match( calc_val[1] ):
        case '+':
            calc = float(calc_val[0]) + float(calc_val[2]) 
        case '-':
            calc = float(calc_val[0]) - float(calc_val[2])
        case '*':
            calc = float(calc_val[0]) * float(calc_val[2])
        case '/':
            if float(calc_val[2]) == 0:
                calc = -99999
                print( 'ZeroDivisionError: Division By Zero Not allowed' )
            else:
                calc = float(calc_val[0]) / float(calc_val[2])
    
    if calc != -99999:
        print( F'{calc:.1f}' )