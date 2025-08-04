import sqlite3

connection = sqlite3.connect( 'suits.db' )

print( connection )

print( 'CRUD Operations! \n' )

cursor = connection.cursor()

def printUserDetails():
    print( '\n READ Operation: \n' )
    cursor.execute( 'SELECT * FROM Employee' )    
    print( '\t User Details : ',  cursor.fetchall() )

printUserDetails()

def create_user():
    print( '\n\t CREATE Operation - Add User: \n' )

    add_name = input( "\t Enter User's Name   : " )
    add_dept = input( "\t Enter User's Department : " )
    add_sal = float( input( "\t Enter User's Salary : " ) )
    add_city = input( "\t Enter User's City : " )
    add_country = input( "\t Enter User's Country : " )

    if add_name  and add_dept and add_sal and add_city and add_country :
        
        print( '\t Name : ', add_name, ' Department: ', add_dept, ' Salary: ', add_sal, ' City : ', add_city, ' Country : ', add_country )
        
        cursor.execute( 
            'INSERT INTO Employee(empName,empDept,empSalary,empCity,empCountry) VALUES ( ?, ?, ?, ?, ? )',
            ( add_name, add_dept, add_sal, add_city, add_country )
        )
    else:
        print( 'Invalid Data! ' )

create_user()
connection.commit()
printUserDetails()

print( '\n\t Sorting Operation: \n' )
cursor.execute( 'SELECT * FROM Employee ORDER BY empSalary DESC' )
print( '\t', cursor.fetchall() )

print( '\t Update Operation - Update User: \n' )
def update_user():
    update_id = int( input( "\t Enter User's ID to Update : " ) )
    update_sal = float( input( "\t Enter Salary Increment : " ) )
    if update_id and update_sal:
        cursorVal = cursor.execute( 'UPDATE Employee SET empSalary = ? WHERE empId = ? ', (update_sal, update_id) )
        if cursorVal.rowcount > 0:
            print( '\t UPDATE was successful!' )
        else:
            print( '\t UPDATE FAILED!' )
    else:
        print( 'Invalid Data! ' )

update_user()
connection.commit()
printUserDetails()

print( '\t Delete Operation: \n' )
def delete_user():
    update_id = int( input( "\t Enter User's ID to Delete: " ) )

    if update_id:
        cursorVal = cursor.execute( 'DELETE FROM Employee WHERE empId = ? ', (update_id,) )
        if cursorVal.rowcount > 0:
            print( '\t Delete was successful!' )
        else:
            print( '\t Delete FAILED!' )
    else:
        print( 'Invalid Data! ' )

delete_user()
connection.commit()
printUserDetails()

connection.close()