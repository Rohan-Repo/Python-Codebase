"""
Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( 

Implement a function called convert that accepts a str as input and returns that same input with any 
:) converted to 🙂 (otherwise known as a slightly smiling face) and any 
:( converted to 🙁 (otherwise known as a slightly frowning face). 
All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, 
and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own 
as an argument to input. Be sure to call main at the bottom of your file.

Install Module - pip install emoji
"""

# Code needed these exact Smileys so we searched the CLDR Unicodes
def convert_cldr( str ):
    
    if str.find(':)') | str.find(':('):
        
        if str.find(':)') != -1:
            # str = str.replace( ':)', '\N{grinning face}' )
            str = str.replace( ':)', '\N{slightly smiling face}' )
            
            
        if str.find(':(') != -1:
            # str = str.replace( ':(', '\N{crying face}' )
            str = str.replace( ':(', '\N{slightly frowning face}' )
            
        print( 'Using CLDR :', str )

# Emoji Module was not expected so we commented the Function-Call

def convert_emoji_module( str ):
    
    import emoji 
    
    if str.find(':)') | str.find(':('):
        if str.find(':)') != -1:
            str = str.replace( ':)', emoji.emojize(':grinning_face_with_big_eyes:') )
            
        if str.find(':(') != -1:
            str = str.replace( ':(', emoji.emojize(':crying_face:') )
            
        print( 'Using Emoji Module :', str )

    
def main():
    inp_str = input('Enter Text:')
    convert_cldr( inp_str )
    convert_emoji_module( inp_str )
    
if __name__ == "__main__":
    main()