import json
    
# Read JSON using Default json Library
with open('users.json') as jsonFile:
    
    jsonData = json.load( jsonFile )
    print( jsonData )
    
    print( '\n User Details:' )
    for user in jsonData:
        print( "\t Name : ", (user['firstName'] + " " +  user['lastName']) )
        print( "\t Phone : ", user['contactDetails']['phoneNumber'] )    
        print( "\t Email-ID : ", user['contactDetails']['emailAddress'] )    
        print( "\t Hobbies : ", user['hobbies'] )
        print( "\t Developer : ", user['isProgrammer'] )
        print( "\t Tester : ", user['isTester'], '\n' )
