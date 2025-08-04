"""
1. Variables Store Data and Identify the value:
    Variables: We create a placeholder in memory and then assign it some value
    Data-Types: Specifies the Type of Value a variable holds
    Built-in data-structures come packaged with your Python Distribution i.e. Shipped with Python Language, they are of two types:
    Primitive Data-Structures : integers, float, string, boolean
    Non-Primitive Data-Structures : list, tuple, arrays, dictionary, sets, files
        Mutable - Can be modified ||| Immutable - Cannot be modified
        Lists - Ordered and Mutable Collection of Items
        Tuples - Ordered and Immutable Collection of Items
        Sets - Ordered and Mutable Collection of Items
        Dictionary - Mapped Collection of Items : Key-Value Pairs  
"""

intVal = 5
floatVal = 2.5
stringVal = 'Canada'
boolVal = True
noneVal = None
print( 'Built-in Data-Types:' )
print( '\t Integer Value: ', intVal, '\t Type:', type(intVal) )
print( '\t Float Value: ', floatVal, '\t Type:', type(floatVal) )
print( '\t String Value: ', stringVal, '\t Type:', type(stringVal) )
print( '\t Boolean Value: ', boolVal, '\t Type:', type(boolVal) )
print( '\t None Value: ', noneVal, '\t Type:', type(noneVal) )

intRes = intVal * 9
print( '\t Result Value: ', intRes, '\t\t Type:', type(intRes) )

floatRes = floatVal + 0.5
print( '\t Result Value: ', floatRes, '\t\t Type:', type(floatRes) )

strRes = 'Toronto,' + stringVal
print( '\t Result Value: ', strRes, '\t Type:', type(strRes) )

listVal = [ 18, 12.3, [10,-5], "Manitoba" ]
print( '\t Value 1 : ', listVal, '\t\t Type:', type(listVal) )

# Mutable Lists 
listVal[3] = "Yukon"
print( '\t Value 2 : ', listVal )

tupleVal = ( 18, 12.3, [10,-5], "Manitoba" )
print( '\t Value: ', tupleVal, '\t\t Type:', type(tupleVal) )

# 
# tupleVal[3] = "Yukon"
# print( '\t Value: ', tupleVal, '\t\t Type:', type(tupleVal) )
# Error - TypeError: 'tuple' object does not support item assignment

setVal = { "Markham", "Brampton", "Etobicoke", "Aurora" }
print( '\t Value 1: ', setVal, '\t Type:', type(setVal) )
# setVal.remove("Dundas")
# print( '\t Value 2 : ', setVal )
# setVal.add("Vaughan")
# print( '\t Value 3 : ', setVal )
# setVal.add("Osgoode")
# print( '\t Value 4 : ', setVal )
# setVal.add("Dundas")
# print( '\t Value 5 : ', setVal )

dictVal1 = { "brand": "Sony", "type": "Wireless", "hasANC": True }
dictVal2 = { "brand": "JBL", "type": "Wired", "hasANC": False }

print( '\t Dictionary Value 1: ', dictVal1, '\t Type:', type(dictVal1) )
print( '\t Dictionary Value 2: ', dictVal2, '\t Type:', type(dictVal2) )