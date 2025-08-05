# 1 - Phonebook using List's 
contact_names = [ 'John', 'Jane', 'Mary' ]
phone_nums = [ '+1-987-6543210', '+977-1234567890', '+91-9876543210' ]

print( 'contact_names : ', contact_names )
print( 'phone_nums : ', phone_nums )

name = input('Enter Name: ' )

if name in contact_names:
    pos = contact_names.index( name )
    print( contact_names[pos], ' - ', phone_nums[pos] )
else:
    print( 'User not Found, Enter a Valid Name!' )


# 2 - Phonebook using Dictionaries
phone_contacts_dict = {
    'John' : '+1-987-6543210',
    'Jane' : '+977-1234567890',
    'Mary' : '+91-9876543210'
}

if name in phone_contacts_dict:
    print( '3: ', name , ' - ', phone_contacts_dict[name] )
else:
    print( 'User not Found, Enter a Valid Name!' ) 

# 3 - Phonebook using List of Dictionaries
phone_contacts = [
    {
        'name': 'John',
        'phoneNum': '+1-987-6543210'
    },
    {
        'name': 'Jane',
        'phoneNum': '+977-1234567890'
    },
    {
        'name': 'Mary',
        'phoneNum': '+91-9876543210'
    }
]

print( 'Dict_Values : ', phone_contacts )

for contact in phone_contacts:
    if name in contact['name']:
        print( contact['name'], ' - ', contact['phoneNum'] )
        break
    else:
        continue
else:
    print( 'User not Found, Enter a Valid Name!' )