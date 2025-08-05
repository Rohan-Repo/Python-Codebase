# words = dict()
# We don't need to do that cause we don't want to check the meaning just the word so a Set will suffice
words = set()

# Check if the word is a part of the dictionary of words
def checkWord( word ):
    if word.lower() in words:
        return True
    else:
        return False

# Load the Dictionary Values
def loadDictionary( dictionary ):
    file = open( dictionary, "+r" )

    for line in file:
        # words.add( line ) will keep the \n
        # {'arcotherapy\n', 'urite\n', 'chemigraphically\n', 'atafter\n', 'unpublicized\n', 'hoggers\n'}
        # Strip the /n from eachline using rstrip() 
        # {'arcotherapy', 'urite', 'chemigraphically', 'atafter', 'unpublicized', 'hoggers'}
        
        word = line.rstrip() 
        words.add( word )

    file.close()

def getDictionarySize():
    return len( words )

def printWordsInDictionary():
    print( words )

loadDictionary( "data\\words.txt" )
print( 'Dict Size: ' , getDictionarySize() )

# printWordsInDictionary()
wordList = ['Abnormal', 'Misguided', 'I/O']
for word in wordList:
    print( word, ' is present in the dictionary: ', checkWord(word) )

# Free Memory to give back to the OS
# No need because Interpreter handles the Automatic Memory Management so no malloc or anything