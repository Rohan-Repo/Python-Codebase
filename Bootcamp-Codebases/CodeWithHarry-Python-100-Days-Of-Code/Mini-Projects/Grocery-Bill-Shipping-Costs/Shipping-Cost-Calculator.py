# Shipping Cost : Check the Percentage of the Destination and Add it to the Calculation
#   Eg. MB -> ON : Cost = 100 But ON tax = 13 so in total Transportation Cost = 113
#   Eg. ON -> Nunavut : Cost = 100 But Nunavut tax = 5 so total Transportation Cost = 105

# https://www.fedex.com/en-ca/news/canadian-sales-taxes.html
dict_tax_percentages = { "AB": 5, "BC": 12, "MB": 12, "NB": 15, "NFL": 15, "NWT": 5, "NS": 15, "NU": 5, 
"ON": 13, "PEI": 15, "QC": 14.98, "SK": 11, "YT": 5 }

print( 'List of Provinces:' )
for key in dict_tax_percentages:
    print( key, end=',' )
print('\n')
source = input( 'Enter Source:' )
destination = input( 'Enter Destination:' )

if source.islower() | destination.islower():
    destination = destination.upper()
    source = source.upper()


if dict_tax_percentages.get(destination) != None:
    shipping_cost = float( input('Enter Shipping Cost:') )

    import time 
    date_now = time.strftime('%A, %d, %B, %Y %I:%M:%S %p %Z')

    print( f'\n Invoice Date : {date_now}' )

    invoiceAmount = shipping_cost+dict_tax_percentages[destination]

    print( f'\n Invoice Transportation Cost to Move Shipment from {source} -> {destination} = $ {invoiceAmount:,.2f}' )
else:
    print( 'Invalid Destination Entered!!' )