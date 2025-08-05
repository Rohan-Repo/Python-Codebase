"""
E = MC^2 represents energy (measured in Joules),  represents mass (measured in kilograms), and 
represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) 
and then outputs the equivalent number of Joules as an integer.
"""

speed_of_light = 300000000
mass = int( input('Enter Mass:') )

print( 'Energy in Joules = ', mass*(speed_of_light**2) )