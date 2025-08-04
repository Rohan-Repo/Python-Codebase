"""
1. Comments are used to explain what a piece of code does to be shown to future developers or testers
    Python Interpreter Ignores the comments, not execute
    In Python we have two types of Comments:
        Single-Line Comments start with hash '#' Symbol (Eg. # My comment )
        Multi-Line Comments start with triple double-quotes '\"""\' Symbol
        Eg. \"""
                Multi-Line
                Comment
            """
"""
2. Escape Sequences are used To insert characters that cannot be directly used in a string
    An escape sequence character is a backslash \ followed by the character you want to insert.
    Egs. \n, \t or \
"""

# Single Line String can be created using "abc" or 'abc'
"""
Multi-line Strings are created using 
'''
abc
def
''' 
""" 
import sys

"""
This wont work, it will give SyntaxError: unterminated string literal, so we use escape sequences to over come this 
print( 'Province: Ontario
Country:Canada' )
"""

print( 'Province: Ontario \n Country:Canada' )

"""
This will give an Error
print( 'I can't see you' )  
SyntaxError: unterminated string literal
"""
print( 'I can\'t see you' )

# For print(), seperator, end, file are optional parameters
# Default Values : Seperator = Space,  End = New Line, file = sys.stdout (i.e. Console) 
print( "Multi-Param Print Stmt. 1: ", "ON", "QC", 3, 12 ) 
print( "Multi-Param Print Stmt. 2: ", "ON", "QC", 25.5, sep='\t', end=',' ) # Seperator = Tab & End = Comma
print( "Multi-Param Print Stmt. 3: ", "AB", "BC", True, sep='\t', end='\b' ) # Seperator = Tab & End = Backspace
print( 'Multi-Param Print Stmt. 4', 5, 'Stmt. 4', sep='' ) 
# No-specified so Seperator and End go back to default values
print( 'Print Statement #5', 7*8 )