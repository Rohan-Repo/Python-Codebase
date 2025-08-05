#  pip install qrcode

import os
import qrcode

img = qrcode.make( 'https://www.youtube.com/watch?v=7sWn9MAuJFM' )

img.save( 'qr.png', 'PNG' )