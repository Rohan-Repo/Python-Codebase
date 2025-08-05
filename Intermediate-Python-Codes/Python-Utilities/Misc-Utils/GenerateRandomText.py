# Importing random to generate
# random string sequence
import random, uuid

# Importing string library function
import string


def rand_pass(size):
    # Takes random choices from
    # ascii_letters and digits
    generate_pass = ''.join([random.choice( string.ascii_uppercase +
                                            string.ascii_lowercase +
                                            string.hexdigits +
                                            string.octdigits +
                                            string.digits)
                             for n in range(size)])

    return generate_pass

print( 'UUID v1 = ', uuid.uuid1().__str__() )
print( 'UUID v3 = ', uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org') )
print( 'UUID v4 = ', uuid.uuid4() )
print( 'UUID v5 = ', uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org') )


def rand_pass2(size):
    # Takes random choices from
    # ascii_letters and digits
    generate_pass = ''.join([random.choice(
                                            uuid.uuid4().__str__().replace("-","")
                                            )
                             for n in range(size)])


# Driver Code
password = rand_pass(10)
print(password)

password = rand_pass2(10)
print(password)

print ( ''.join(random.choice(uuid.uuid4().__str__().replace("-","")) for i in range(10)) )


uuidTxt = uuid.uuid4().__str__().replace("-","") + uuid.uuid5(uuid.NAMESPACE_DNS, 'asasasa').__str__().replace("-","")
print( 'uuid:', uuidTxt )
# otpText = ''.join(random.choice(uuid.uuid4().__str__().replace("-","")) for i in range(10))
otpText = ''.join(random.choice(uuidTxt) for i in range(10))
print( 'otpText:', otpText )