"""
1. Python Information:
    Python is a dynamically typed, general purpose programming language that supports an object-oriented programming approach as well as a functional programming approach.
    Python is an interpreted and a high-level programming language.
    It was created by Guido Van Rossum in 1989.
    Python is an Open-Source, Interpreted and platform-independent language which makes debugging very easy.
2. Python Usage:
    Python is used in Data Visualization to create plots and graphical representations.
    Python helps in Data Analytics to analyze and understand raw data for insights and trends.
    It is used in AI and Machine Learning to simulate human behavior and to learn from past data without hard coding.
    It can be used to create web applications as well as to handle databases.
    It is used in business and accounting to perform complex mathematical operations along with quantitative and qualitative analysis.
    Everything in Python is an Object, that's why it is an Object-Oriented Programming Language

3. Modules are used to borrow code from some other place or the language itself as it saves time & efforts to solve complex problems
    I don't know what is inside a bike or a television Set but I can still use it  
    Pip, NPM are package Managers, they download & install code from different Modules & packages for you to use directly in your Application
    Eg. You have to make Tea at home, so U go out & buy milk from the Dairy Farm, Tea leaves & Sugar from the Grocery Store & come home to make Tea, Thus in this example, you are the Package Manager
    The house will have a Tea-Pot & Gas already so in this analogy : Milk, Tea & Sugar are External Modules whereas Gas & Tea-pot are internal modules 
    2 Types of Modules:
        Built-in Modules - Modules readily available without installing : Use code written inside the Python Programming Language, shipped with the language (Eg. str,uuid)
        External Modules - Modules imported from third-party file and needs a package manager like Pip or conda to install in our program : Use code written by somebody else (Eg. pytube, pandas)
    Usage:
        pip install moduleName or conda install moduleName: To install a module into your application
        import moduleName : To import that module into your application
4. REPL - Read Evaluate Print Loop 
"""
import pandas as pd

df2 = pd.read_fwf('words.txt')
print('DF2:', df2.size, ' Shape:', df2.shape )

print( '\n Arithmetic Operations:')
print( "Division: ", 25/5 )
print( "Multiplication: ", 25*5 )
print( "Substraction: ", 25-5 )
print( "Remainder: ", 25%5 )
print( "Addition: ", 25+5 )

n1 = input( 'Enter Number 1:')
n2 = input( 'Enter Number 2:')
print( "Addition 2 : ", n1+n2 )

n1 = input( 'Enter Number 1:')
n2 = input( 'Enter Number 2:')
print( "Addition 2 : ", int(n1)+int(n2) )

print( "String-Concat:", ('Fire'+'Ice') )

print( '\n \t Poem Title: Fire and Ice' )
print( '\t By Poet : Robert Frost' )

strPoem = '''
Some say the world will end in fire,
Some say in ice.
From what I’ve tasted of desire
I hold with those who favor fire.
But if it had to perish twice,
I think I know enough of hate
To say that for destruction ice, Is also great, And would suffice.
'''
print( strPoem )
