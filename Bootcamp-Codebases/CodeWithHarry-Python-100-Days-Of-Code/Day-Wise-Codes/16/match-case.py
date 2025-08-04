"""
Match-Case Statements:
    Introduced in Python 3.10 + 
    Similar to Switch Case which we use in C, C++ or Java except we dont need to specify break, Python checks for case
    A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. 
    The main idea is to keep on comparing the variable with all the present patterns until it fits into one.
    The match case consists of three main entities :
        The match keyword
        One or more case clauses
        Expression for each case
        Default Case : Underscore _
    The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches. 
"""

dict_tax_percentages = { "AB": 5, "BC": 12, "MB": 12, "NB": 15, "NFL": 15, "NWT": 5, "NS": 15, "NU": 5, 
"ON": 13, "PEI": 15, "QC": 14.98, "SK": 11, "YT": 5 }

print( 'List of Provinces:' )
for key in dict_tax_percentages:
    print( key, end=',' )
print('\n')
source = input( 'Enter Source:' )
destination = input( 'Enter Destination:' )
shipping_cost = float( input('Enter Shipping Cost:') )

taxAmount = 0

if source.islower() | destination.islower():
    destination = destination.upper()
    source = source.upper()

match destination:
    case 'AB':
        taxAmount = 5
    case 'BC':
        taxAmount = 12
    case 'MB':
        taxAmount = 12
    case 'NB':
        taxAmount = 15
    case 'NFL':
        taxAmount = 15
    case 'NWT':
        taxAmount = 5
    case 'NS':
        taxAmount = 15
    case 'NU':
        taxAmount = 5
    case 'ON':
        taxAmount = 13
    case 'PEI':
        taxAmount = 15
    case 'QC':
        taxAmount = 14.98
    case 'SK':
        taxAmount = 11
    case 'YT':
        taxAmount = 5
    case _: # Default Case
        taxAmount = 0

if( taxAmount != 0 ):
    import time 
    date_now = time.strftime('%A, %d, %B, %Y %I:%M:%S %p %Z')

    print( f'\n Invoice Date : {date_now}' )

    # print( f'\n CAD Transportation Cost to Move Shipment from {source} -> {destination} = $ { shipping_cost+taxAmount :.2f}' )
    
    invoiceAmt = shipping_cost+taxAmount

    import locale
    
    locale.setlocale( locale.LC_ALL, 'de_DE')
    print( f'\n EUR Germany Transportation Cost to Move Shipment from {source} -> {destination} = ', locale.currency (invoiceAmt) )
    locale.setlocale( locale.LC_ALL, 'en_CA')
    print( f'\n CAD Transportation Cost to Move Shipment from {source} -> {destination} = ', locale.currency (invoiceAmt) )
    locale.setlocale( locale.LC_ALL, 'en_GB')
    print( f'\n GBP Transportation Cost to Move Shipment from {source} -> {destination} = ', locale.currency (invoiceAmt) )
    locale.setlocale( locale.LC_ALL, 'en_IN')
    print( f'\n INR Transportation Cost to Move Shipment from {source} -> {destination} = ', locale.currency (invoiceAmt) )
    locale.setlocale( locale.LC_ALL, 'en_JP')
    print( f'\n Yen Transportation Cost to Move Shipment from {source} -> {destination} = ', locale.currency (invoiceAmt) )
    locale.setlocale( locale.LC_ALL, 'en_FR')
    print( f'\n EUR France Transportation Cost to Move Shipment from {source} -> {destination} = ', locale.currency (invoiceAmt) )
    
else:
    print( 'Invalid Destination Entered!!' )