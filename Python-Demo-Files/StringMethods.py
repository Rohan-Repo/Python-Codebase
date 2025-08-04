data = '1,JohnDoe,sales,Toronto,Canada,$100000'

print( 'Normal Print : ', data )
print( 'String Length : ', len(data) )
print( 'Upper-Case : ', data.upper() )
print( 'Lower-Case : ', data.lower() )
print( 'Swap-Case : ', data.swapcase() )
dataSplit = data.split(',')
print( 'Split-String : ', dataSplit )
print( 'Capitalize : ', dataSplit[2].capitalize() )
print( 'Join via Delimiter : ', '-'.join(dataSplit) )
print( 'Replace $ with C$ : ', data.replace( '$', 'C$' ) )
print( 'Position of J : ', data.find('J') )
print( 'Position of Z : ', data.find('Z') )