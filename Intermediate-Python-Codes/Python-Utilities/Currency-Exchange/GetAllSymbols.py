import requests

url = 'https://api.exchangerate.host/symbols'
response = requests.get(url)
data = response.json()

print(data)
       