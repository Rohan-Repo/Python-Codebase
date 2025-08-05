links = list()

def loadFile( fileName ):
    file = open( fileName, "+r" )

    for line in file:
        # Strip the /n from eachline using rstrip() 
        
        word = line.rstrip()
        if word != '.':
            links.append( word )

    file.close()

def getWordSize():
    return len( links )

def printWordsInFile():
    print( links )

def printDuplicates():
    print( '\n Duplicates are:')
    for i in range( len(links) ):
        for j in range( i+1, len(links) ):
            if links[i] == links[j]:
                print( '\t', links[i], ':', links[j] )
                break


loadFile( "sample.txt" )
# printWordsInFile()
print( '\n Word Size: ' , getWordSize() )

printDuplicates()