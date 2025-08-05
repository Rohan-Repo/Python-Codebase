"""
With Syntax is better cause here we don't need to worry about closing the file,
it gets closed automatically after the block ends
"""

from pathlib import Path
import json

fileInPath = None 

for fileInPath in Path('data\\').glob('*.json'):
    print( fileInPath )
    # Make Sure JSON File is present
    if fileInPath.is_file():
        print( "\n For : ", fileInPath.name, "\t JSON Data is \n" )
        
        # Convert JSON String into JSON Object
        print( 'DataType : ' , type( fileInPath.read_text() ) )
        jsonData = json.loads( fileInPath.read_text() )
        print( jsonData )
    elif not fileInPath.exists():
        # If it didnt find any JSON File
        print( 'JSON File Not Found' )

if fileInPath is None:
    print( 'No JSON File encountered' )