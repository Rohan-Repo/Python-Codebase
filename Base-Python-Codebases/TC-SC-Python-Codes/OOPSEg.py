# Classes imitate Real-World Objects into Code

# __init__ is the Constructor Method which is called automatically as soon as an object is created
# self points to the current object we are accessing

class Headphone:
    # Attributes - Properties - Features to Describe the Class
    
    def __init__( self, hpId, hpBrand, hpColor, hpType, hpHasANC ):
        self.hpId = hpId
        self.hpBrand = hpBrand
        self.hpColor = hpColor
        self.hpType = hpType
        self.hpHasANC = hpHasANC

    def print_headphone_details( self ):
        print( 'Headphone Details: ' )
        print( '\t ID = ', self.hpId, '\t Type: ', type(self.hpId) )
        print( '\t Brand = ', self.hpBrand, '\t  Type: ', type(self.hpBrand) )
        print( '\t Type = ', self.hpType, '\t  Type: ', type(self.hpType) )
        print( '\t Color = ', self.hpColor,  '\t  Type: ', type(self.hpColor) )
        print( '\t Has-ANC = ', self.hpHasANC, '\t  Type: ', type(self.hpHasANC) )

# Create Headphone Objects
hp_1 = Headphone( hpId=1, hpBrand="Bose", hpColor="Black", hpType='Wireless', hpHasANC=True )
hp_1.print_headphone_details()
print( 'HP-1 Object Type : ', type(hp_1) )

print( 'HP-1 Brand: ', hp_1.hpBrand )
print( 'HP-1 Color: ', hp_1.hpColor )

hp_2 = Headphone( hpId=2, hpBrand="Sony", hpColor="White", hpType='Wired', hpHasANC=False )
hp_2.print_headphone_details()
print( 'HP-2 Object Type : ', type(hp_2) )

print( 'HP-2 Type: ', hp_2.hpType )
print( 'HP-1 Has-ANC: ', hp_2.hpHasANC )