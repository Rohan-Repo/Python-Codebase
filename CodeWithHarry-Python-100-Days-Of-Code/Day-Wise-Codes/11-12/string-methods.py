"""
Mutable - Can be modified ||| Immutable - Cannot be modified
Strings in Python are Immutable
"""
str1 = 'Artificial Intelligence'
print( 'Value : ', str1, ' ID: ', id(str1) )
print( 'Length of String: ', len(str1) )
str1_upper = str1.upper() # .lower() for lower-case
print( 'Value : ', str1_upper, ' ID: ', id(str1_upper) )


str2 = '    Artificial Intelligence    '
print( 'Value : ', str2, '-ID: ', id(str2), ' Length: ', len(str2) )

# .strip() - Removes White Spaces before and after the String
str2_stripped = str2.strip()
print( 'Value : ', str2_stripped, '-ID: ', id(str2_stripped), ' Length: ', len(str2_stripped) )

# .replace() - Replaces all occurences of the String with another string 
str3 = '''
Machine Learning is a part of Artificial Intelligence
Deep Learning is a part of Artificial Intelligence
Reinforcement Learning is a part of Artificial Intelligence
'''
print( 'Value 1: ', str3, ' ID: ', id(str3), 'Length: ', len(str3) )
str3_replaced = str3.replace( "Artificial Intelligence", "AI" )
print( 'Value 2: ', str3_replaced, 'ID: ', id(str3_replaced), ' Length: ', len(str3_replaced) )
str3_replaced = str3_replaced.replace( "Machine Learning", "ML" )
print( 'Value 3: ', str3_replaced, 'ID: ', id(str3_replaced), ' Length: ', len(str3_replaced) )
str3_replaced = str3_replaced.replace( "Deep Learning", "DL" )
print( 'Value 4: ', str3_replaced, 'ID: ', id(str3_replaced), ' Length: ', len(str3_replaced) )
str3_replaced = str3_replaced.replace( "Reinforcement Learning", "RL" )
print( 'Value 5: ', str3_replaced, 'ID: ', id(str3_replaced), ' Length: ', len(str3_replaced) )

# .split() - Separates the Strings based on the specified Delimiter
# print( str3_replaced.split('\n') ) - Staring and Ending had White Spaces 
str3_split = str3_replaced.strip().split('\n')
print( "Split String:",  str3_split, ' Type: ', type(str3_split), ' Split-Count:', len(str3_split) )

# .join() - Join all Iteams in a collection into a String
str3_joined = '/'.join(str3_split)
print( "Joined String:",  str3_joined, ' Type: ', type(str3_joined), ' ID:', id(str3_joined) )

str4 = 'https://www.google.ca'
# .count() - Count the occurrences of the given String in the String
print( 'In the String:', str4, ' - dot occurred ', str4.count('.'), ' times!' ) 

# startswith() & endswith()
# startswith() - Does the String start with a given string
print( 'URL: ', str4, ' startsWith https: ', str4.startswith('https') )
# We can also search for starting string in between 
# print( str4[8:] )
print( 'URL: ', str4, ' startsWith www: ', str4.startswith('www',8) )

# endswith() - Does the String end with a given string
print( 'URL: ', str4, ' endsWith .ca: ', str4.endswith('.ca') )
# We can also search for ending string in between  
# print( str4[0:-3] )
print( str4.endswith('google',0,-3) )

# .find() finds the first occurrence of the given string else returns -1
print( 'In the String:', str4, ' Length: ', len(str4) )
print( '.ca was found at postion', str4.find('.ca'), ' and .com was found at postion', str4.find('.com') )

str6 = 'StudentID7'
str7 = 'Student-ID-7'
# .isalnum() - Will Check for Alphanumeric [A-Z a-z 0-9] Characters otherwise returns False
print( str6, ' is Alphanumeric : ', str6.isalnum() )
print( str7, ' is Alphanumeric : ', str7.isalnum() )

# .swapcase() - Chage Upper-Case to Lower & Vice-Versa
print( 'Original : ', str7, ' Swapped-Case: ', str7.swapcase() )

str8 = 'Mutable - can be modified ||| Immutable - cannot be modified'
# .title() - Capitalizes each letter of the word within String
print( 'Original : ', str8, ' -> Title-Case: ', str8.title() )

# .format() - Use {} as Placeholders
# We can pass in Strings, Class Attributes, Dictonary Values, Unpacking Dictionary values 
# Number Formatting : let's it know that formatting is going on
# :02 - Making it a two digit value || :.2f - Reduce to two decimal places || :., - To add commas for a Large Number
# Date Formatting - Based upon Directives on datetime Python page
str_city = 'Toronto'
str_province = 'Ontario'

str_format_1 = 'I live in {}, {}!'.format( str_city, str_province )
print( 'Formtted String #1:', str_format_1 )

address_dict = { 'city': 'Toronto', 'province': 'Ontario', 'Country': 'Canada' }

"""
str_format_2 = 'I live in {}, {}, {}'.format( address_dict['city'], address_dict['province'], address_dict['Country'] )
This is similar to the Statement below
"""

str_format_2 = 'I live in {0}, {1}, {2}'.format( address_dict['city'], address_dict['province'], address_dict['Country'] )
print( 'Formtted String #2 Way #1:', str_format_2 )

str_format_2 = 'I live in {0[city]}, {0[province]}, {0[Country]}'.format( address_dict )
print( 'Formtted String #2 Way #2:', str_format_2 )

str_tag = 'title'
str_text = 'My Personal Website'

str_html = '<{0}> {1} </{0}>'.format( str_tag, str_text )
print( 'HTML Format Eg.: ', str_html )

class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p_obj_1 = Person( 'John', 25 )

str_class_vals = "Person's Name is {0.name} and he is {0.age} years old".format(p_obj_1)
print( str_class_vals )

# list_vowels = [ 'A', 'E', 'I', 'O', 'U' ]

print( 'Address Dictionary: ', address_dict )
str_unpacked_dict = 'I live in {city}, {province}, {Country}'.format( **address_dict )
print( 'Unpacked Dictionary:', str_unpacked_dict )
# print( 'Vals'.format(**list_vowels) )

# Normal Numbers Added
list_nums_1 = []

for i in range(11):
    list_nums_1.append( '{}'.format(i) )

# Zero Padded Number
list_nums_2 = []

for i in range(11):
    list_nums_2.append( '{:02}'.format(i) )

print( 'Nums List #1 : ', list_nums_1 )
print( 'Nums List #2 : ', list_nums_2 )

# Reduce to two or four decimal places
pi = 3.14159265

print( '2 Decimal Pi value is {:.2f}'.format(pi) )
print( '4 Decimal Pi value is {:.4f}'.format(pi) )

# Provide Commas for a Bigger Numerical Value | 1,000,000 Instead of 1000000
print( '1 MB = {:,}'.format(1000**2) )

# Date Formatting
import datetime
date_1 = datetime.datetime( 2021, 12, 31, 13, 45, 59)

# Weekday, Day, Month, Year, Hour:Minutes:Seconds AM/PM Zone
print( 'Date Format #1 : {:%A, %d, %B, %Y %I:%M:%S %p}'.format(date_1) )

# F-Strings : Specify F" or F' or F""" or f' or f" or f""" to Let Python know you are using F-Strings
# Alternative to .format Method : Can be used as Placeholder, Padding, Calculations

import time 
date_now = time.strftime('%A, %d, %B, %Y %I:%M:%S %p %Z')
print( f'F String #1 : {date_now}' )
print( f'F String #2 : {(1000**2) / pi} OR {1000 - pi}' )

list_nums_3 = []

for i in range(11):
    list_nums_3.append( f'{i:02}' )

print( 'F String #3 : ', list_nums_3 )

date_3 = datetime.datetime( 2020, 3, 20, 11, 59, 41)
print( f'F String #4 : {date_3: %d, %B, %Y %H:%M:%S %p}' )