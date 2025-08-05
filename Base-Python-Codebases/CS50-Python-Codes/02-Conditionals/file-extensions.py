"""
https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types

In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that 
file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
.gif .jpg .jpeg .png .pdf .txt .zip 

If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, 
which is a common default.
"""

file_name = input( 'File Name: ' )

# Case-Check
file_name = file_name.lower()

# White Spaces Check
file_name = file_name.strip()

"""
if file_name.endswith('.gif'):
    print( 'MIME Type: image/gif' )
elif file_name.endswith('.jpeg') or file_name.endswith('.jpg'):
    print( 'MIME Type: image/jpeg' )
elif file_name.endswith('.png'):
    print( 'MIME Type: image/png' )
elif file_name.endswith('.pdf'):
      print( 'MIME Type: application/pdf' )
elif file_name.endswith('.txt'):
    print( 'MIME Type: text/plain' )
elif file_name.endswith('.zip'):
    print( 'MIME Type: application/zip' )
else:
    print( 'MIME Type: application/octet-stream' )

"""

# File Extension with two or more dots
invalid_file_extension = False

if file_name.count('.') > 1:
    invalid_file_extension = True
    print( 'Invalid File Extension with' , file_name.count('.'), 'dots' )

# [ 'name', 'extension' ]
match( file_name.split('.')[1] ):
    case 'gif':
        print( 'MIME Type: image/gif' )
    case 'jpeg':
        print( 'MIME Type: image/jpeg' )
    case 'jpg':
        print( 'MIME Type: image/jpeg' )
    case 'png':
        print( 'MIME Type: image/png' )
    case 'pdf':
        print( 'MIME Type: application/pdf' )
    case 'txt':
        print( 'MIME Type: text/plain' )
    case 'zip':
        print( 'MIME Type: application/zip' )
    case _:
        if invalid_file_extension is False:
            print( 'MIME Type: application/octet-stream' )
        