import os
# pip install qrcode
# pip install pillow
import qrcode
import uuid

link = input('Enter URL:')

if link.startswith('http://') | link.startswith("https://"):
    img = qrcode.make(link)

    imgName = 'data\\' + str(uuid.uuid4()) + '.jpg'

    img.save( imgName )

else:
    print( 'Invalid Input' )
# print( str(uuid.uuid4()) + '.jpg' )

# str2 = "open " + imgName
#
# print( str2, type(str2) )
#
# os.system( str )