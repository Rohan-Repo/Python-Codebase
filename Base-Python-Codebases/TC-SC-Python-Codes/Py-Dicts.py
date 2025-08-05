phone_contacts_dict = {
    'john' : '+1-987-654-3210',
    'jane' : '+1-123-456-7890',
    'mary' : '+1-086-421-3579'
}

def print_keys_method():
    print( 'keys() method:' )
    for key in phone_contacts_dict.keys():
        print( '\t', key, ' : ', phone_contacts_dict[key] )

def print_items_method():
    print( 'items() method:' )
    for key, value in phone_contacts_dict.items():
        print( '\t', key, ' : ', value )

# def print_dict_values( dictionary ):
#     for key, value in dictionary.items():
#         print( '\t', key, ' : ', value )

print_keys_method()
print_items_method()

def check_if_user_exists( name ):
    if name in phone_contacts_dict:
        return True
    else:
        return False

print( 'Add User: ' )
add_name = input( '\t Enter User to Add: ' )
add_num = input( '\t Enter Number to Add: ' )

phone_contacts_dict[ add_name ] = add_num

print_keys_method()

print( 'Update Operation: ' )
update_name = input( '\t Enter User to Update: ' )

if check_if_user_exists(update_name):
    update_num = input( '\t Enter User-Number to Update: ' )
    phone_contacts_dict.update( { update_name: update_num } )
else:
    print( '\t User not Found, Enter a Valid Name!' ) 

print_keys_method()

print( 'Delete Operation:' )
del_name = input( '\t Enter User to Delete: ' )
if check_if_user_exists(del_name):
    phone_contacts_dict.pop( del_name )
    # del phone_contacts_dict[ del_name ]
else:
    print( '\t User not Found, Enter a Valid Name!' ) 

print_items_method()

print( 'Sorted By Key: ')
dict_sorted_key = sorted( phone_contacts_dict.items() )

print( '\t', dict_sorted_key )

print( 'Sorted By Value: ')
list_sorted_value = sorted( phone_contacts_dict, key=phone_contacts_dict.get )

for key in list_sorted_value:
    print( '\t', key, ' : ', phone_contacts_dict[key] )