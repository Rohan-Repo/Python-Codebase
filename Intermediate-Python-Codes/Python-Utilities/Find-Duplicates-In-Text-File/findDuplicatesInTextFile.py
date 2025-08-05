links = list()

def loadFile( fileName ):
    file = open( fileName, "+r" )

    for line in file:
        
        # Strip the /n from eachline using rstrip() 
        word = line.rstrip()

        # Ignore the lines with just a full-stop
        # otherwise add it to the list 
        if word != '.':
            links.append( word )

    file.close()

def getWordSize():
    return len( links )

def printWordsInFile():
    print( links )

# Compare each fileName to all the other fileNames in the folder
def printDuplicates():
    print( '\n Duplicates are:')
    for i in range( len(links) ):
        for j in range( i+1, len(links) ):
            if links[i] == links[j]:
                print( '\t', links[i], ':', links[j] )
                break

# Load the required text file
loadFile( "sampleFile.txt" )
# printWordsInFile()
print( '\n Word Size: ' , getWordSize() )

printDuplicates()