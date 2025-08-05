"""
IDEA - Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, 
a la YouTube’s 0.75 playback speed, or even by having them pause between words.

Implement a program in Python that prompts the user for input and then outputs that same input, 
replacing each space with ... (i.e., three periods).
"""

inp_str = input('Enter Input:')
print('Original String:', inp_str)
print('Replaced String:', inp_str.replace(" ", "...") )