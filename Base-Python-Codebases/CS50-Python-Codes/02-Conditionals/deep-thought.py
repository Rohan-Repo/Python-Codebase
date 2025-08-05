"""
Implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""

inpVal = input( 'Answer to the Great Question of Life, the Universe and Everything: ' )

# If input is FouRtY tWo It might return No so, we need to lower-case the whole thing
inpVal = inpVal.lower()

if inpVal.find('42') != -1 or inpVal.find('forty-two') != -1 or inpVal.find('forty two') != -1:
    print( 'Yes' )
else:
    print( 'No' ) 