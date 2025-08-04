import requests

url = 'https://api.exchangerate.host/latest/?base=CAD'
response = requests.get(url)
data = response.json()

print( data['base'] )

currs = data['rates']

for curr in currs:
    print( curr, ' - ', currs[curr] )