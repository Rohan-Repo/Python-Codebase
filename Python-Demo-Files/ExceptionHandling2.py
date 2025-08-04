def printFile( fileName ):

    try:
        # Code that can raise an Error - Opening a File
        # Every file we open should be closed so we use the with block 
        # So the file gets closed immediately after the  execution of with block
        print( '\n For file - ', fileName )
        with open( fileName, 'r' ) as myFile:
            
            print( '\t File Contents:'  )
            for line in myFile.readlines():
                print( '\t', line  )

    # Handle IOError
    except IOError:
        print( '\t Unable to open or read data from the file!' )

    # Handle all othe types of Errors
    except Exception as e:
        print( '\t Some other error occurred - ', str(e) )

    # Execute at the End
    finally:
        print( 'Code finished!' )

printFile( 'Info.txt' )
printFile( 'Info1.txt' )