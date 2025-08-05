import hashlib;
import uuid;


print('hashlib.algorithms_available:', hashlib.algorithms_available)
print('hashlib.algorithms_guaranteed:', hashlib.algorithms_guaranteed)

city = "Toronto"

print( 'String: ', city )

md5Val = hashlib.md5( city.encode() )

print( 'md5 Value = ', md5Val, ' The hexadecimal equivalent of MD5 is : = ', md5Val.hexdigest() )

sha1Val = hashlib.sha1( city.encode() )

print( 'sha1 Value = ', sha1Val, ' The hexadecimal equivalent of SHA1 is : = ', sha1Val.hexdigest() )

print( 'UUID v1 = ', uuid.uuid1() )
print( 'UUID v3 = ', uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org') )
print( 'UUID v4 = ', uuid.uuid4() )
print( 'UUID v5 = ', uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org') )

"""
SELECT "Toronto", sha1("Toronto"), md5("Toronto"), uuid(), uuid_short();
                sha1("Toronto")                             md5("Toronto")                          uuid()                          uuid_short()
Toronto	b7e31fe1791fdf0862019d14b0c6a15854ddb477	948ce72be6c871b84f6d0dab24f209ed	4bd6d12c-dd85-11ed-bd2a-9cb6d0bdf978	100273143016325120
"""