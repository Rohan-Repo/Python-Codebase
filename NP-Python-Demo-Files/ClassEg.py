class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details( self ):
        print(F"Person's Detais: \n \t Name = {self.name} \n \t Age = {self.age} years old")

person1 = Person( 'John Doe', 25 )
person1.print_details()

person2 = Person( 'Jane Doe', 18 )
person2.print_details()

# Get List of Functions and variables associated with the class with dir - dir( person1 )