"""
Strings: Sequence of textual characters
    Instead of using Escape Sequences we can use single quotes ' to include Special characters into String 
    Define Multiline Strings using 3 Double Quotes or 3 Single Quotes
"""

# str1 = "GOT, famous line : "Winter is coming""
str1 = "GOT, famous line : \"Winter is coming\""
print( "Double-Quotes String with Escape Sequences:", str1 )
str1 = 'GOT, famous line : "Winter is coming"'
print( "Single-Quotes String:", str1 )

str2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
"sed do eiusmod tempor incididunt"
ut labore et dolore magna aliqua."""
print( "Multi-Line String with Double Quotes:\n" , str2 )

str2 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
"sed do eiusmod tempor incididunt"
ut labore et dolore magna aliqua.'''
print( "Multi-Line String with Single Quotes:\n" , str2 )

str4 = "Technical University of Munich"
print( 'Base String: \t', str4, ' Length of String: ', len(str4) )
print( 'Character at Position : ', 0, ' is : \t', str4[0] )
print( 'Character at Position : ', 10, ' is : \t', str4[10] )
# 
print( 'Character at Position : ', 25, ' is : \t', str4[24] )

# End Index is Non-Inclusive - Default Values in Slicing [ 0 : len(string)-1 ]
print( '\t String Slicing:' )
str3 = "University Of Toronto"
print( 'Base String: \t', str3, ' Length of String: ', len(str3) )
print( 'Character at Position : ', 0, ' is : \t', str3[0] )
print( 'Characters at Position :', '11 & 12 ', 'are : ', str3[11:13] )
print( 'Character at Position : ', 14, ' is : \t', str3[14] )

print( 'Print all characters except last three: \t', str3[:-3] )
print( 'Print first 10 characters: \t', str3[0:10] )
print( 'Print first 5 characters: \t', str3[:5] )
print( 'Print All Charcters from 11th characters: \t', str3[11:] )

# Throws an Error : IndexError: string index out of range
# print( 'Character at Position : ', 25, ' is : \t', str3[25] )

# Slicing [start:end:stepCount] Default : start=0 ; end = len(str)-1 ; step = 1
str5 = 'Bloor–Yonge'
#  B     l   o   o   r   –   Y   o   n   g   e
#  0     1   2   3   4   5   6   7   8   9   10
# -11   -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 
print( 'Base String: \t', str5, ' Length of String: ', len(str5) )
print( 'Print Last Character: \t\t', str5 [ -1 ] )
print( 'Print Alternate Characters: \t', str5 [ : : 2 ] )
print( 'Print len-11 Character: \t', str5 [ -11 ] ) # (len-11) = 11-11 = 0
print( 'Print len-7 Character: \t\t', str5 [ -7 ] ) # (len-7) = 11-7 = 4
print( 'Print [-10:-2:3] Character: \t', str5 [ -10:-2:3 ] ) # (len-10):(len-2) with step-count = 3 [1:9:3]

str6 = 'https://www.google.ca/'
print( 'Base String: \t', str6, ' Length of String: ', len(str6) )
print( 'Reversed URL: \t\t', str6 [ : : -1 ] )
print( 'Get Protocol Value:', str6[:5] )
print( 'Get Domain Value:', str6[-4:-1] ) 
print( 'Get URL without https and ending /:', str6[8:-1] )