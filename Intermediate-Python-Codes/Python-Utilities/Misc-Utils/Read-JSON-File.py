"""
With Syntax is better cause here we don't need to worry about closing the file,
it gets closed automatically after the block ends
"""
# File As it is
#with open('data\CanadianCompanies.json') as jsonFile:
 #   fileData = jsonFile.read()
  #  print( fileData )
    
with open('data\AdminUsers.json') as jsonFile:
    fileData = jsonFile.read()
    print( fileData[1], '-----' )

import json

def getCompanyRating(company):
    return company.get('rating')
    
# In a Straight line
with open('data\CanadianCompanies.json') as jsonFile:
   parsedJSON = json.load( jsonFile )
   print( 'before : ', parsedJSON, '\n' )
   
   parsedJSON.sort( key=getCompanyRating, reverse=True )
   print( 'after : ', parsedJSON )
    
# with open('data\AdminUsers.json') as jsonFile:
    # parsedJSON = json.load( jsonFile )
    # print( parsedJSON )
    # for v in parsedJSON:
        # print( v['userActive'] )
        
