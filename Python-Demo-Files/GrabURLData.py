import requests

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)
data = response.json()

print(data)

for user in data:
    print( '\n For User ID : ', user['id'] )
    print( '\t Name: ', user['name'] )
    print( '\t Email: ', user['email'] )
    print( '\t Phone: ', user['phone'] )
    print( '\t City: ', user['address']['city'] )
    print( '\t WebSite : ', user['website'] )
    print( '\t Company Name: ', user['company']['name'] )
       