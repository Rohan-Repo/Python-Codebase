# Calculate Grocery Bill Based on Province Percentage
# Grocery - Add the proper Percentages to the final bill amount

# dict_tax_percentages = { "Alberta": 5, "British Columbia": 12, "Manitoba": 12, "New Brunswick": 15, "Newfoundland and Labrador": 15,
# "Northwest Territories": 5, "Nova Scotia": 15, "Nunavut": 5, "Ontario": 13, "Prince Edward Island": 15, "Quebec": 14.98,
# "Saskatchewan": 11, "Yukon": 5 }

dict_tax_percentages = { "AB": 5, "BC": 12, "MB": 12, "NB": 15, "NFL": 15, "NWT": 5, "NS": 15, "NU": 5, 
"ON": 13, "PEI": 15, "QC": 14.98, "SK": 11, "YT": 5 }

dict_grocery_items = { "Milk": 7, "Bread": 3.5, "Eggs": 10, "Wine": 20, "Flour": 15, "Sugar": 5, "Pop": 6.5, "Pasta": 6.9, "Oil": 13, "Cereal": 9.99,
"Cheese": 11, "Veg": 10, "Fruits": 10 }

dict_grocery_items_quantity = { "Milk": 0, "Bread": 0, "Eggs": 0, "Wine": 0, "Flour": 0, "Sugar": 0, "Pop": 0, "Pasta": 0, "Oil": 0, "Cereal": 0,
"Cheese": 0, "Veg": 0, "Fruits": 0 }

dict_grocery_items_price = { "Milk": 0, "Bread": 0, "Eggs": 0, "Wine": 0, "Flour": 0, "Sugar": 0, "Pop": 0, "Pasta": 0, "Oil": 0, "Cereal": 0,
"Cheese": 0, "Veg": 0, "Fruits": 0 }

for key in dict_tax_percentages:
    print( key, end=',')

print('\n')
province = input('Select Province:')

if province.islower():
    province = province.upper()

print( 'Item: \t Quantity:')
for key in dict_grocery_items.keys():
    print( key, end='\t\t' )
    itemQty = float(input())
    itemPrice = float(dict_grocery_items.get(key))
    dict_grocery_items_quantity.update( { key: itemQty } )
    dict_grocery_items_price.update( { key: itemPrice*itemQty } )
    
totalBillAmount = 0

print( 'Item: \t\t Quantity: \t\t Amount:')
for key in dict_grocery_items_price.keys():
    print( key, '\t\t', dict_grocery_items_quantity[key], '\t\t\t', dict_grocery_items_price[key] )
    totalBillAmount = totalBillAmount + dict_grocery_items_price[key]

totalTaxAmount = totalBillAmount * float( dict_tax_percentages[province]/(100) )

print( F'Your Tax Amounts to = {totalTaxAmount:.2f}'  )
print( F'Your Final Bill Amount = {(totalBillAmount + totalTaxAmount):.2f}'  )