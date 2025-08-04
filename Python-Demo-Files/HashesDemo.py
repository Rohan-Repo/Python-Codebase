import hashlib;

city = input( 'Enter your favourite City : ' )

print( 'String: ', city )

md5Val = hashlib.md5( city.encode() )

print( ' The hexadecimal equivalent of ', city ,' in MD5 is : = ', md5Val.hexdigest() )

sha1Val = hashlib.sha1( city.encode() )

print( ' The hexadecimal equivalent of ', city ,' in SHA1 is : = ', sha1Val.hexdigest() )

sha256Val = hashlib.sha256( city.encode() )

print( ' The hexadecimal equivalent of ', city ,' in SHA256 is : = ', sha256Val.hexdigest() )

#Extra
sha512Val = hashlib.sha512( city.encode() )

print( ' The hexadecimal equivalent of ', city ,' in SHA512 is : = ', sha512Val.hexdigest() )