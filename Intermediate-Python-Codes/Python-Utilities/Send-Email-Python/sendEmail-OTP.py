from email.message import EmailMessage
import uuid
import ssl
import smtplib
import random

# Put in your Gmail Email Address and App Password Created inside Google Account below
emailSender = 'test@gmail.com'
emailPassword = 'testAppPassword'

emailReceiver = 'test@gmail.com'

subject = "Transaction OTP || DO NOT SHARE"

# otpText = ''.join(random.choice(uuid.uuid4().__str__().replace("-","")) for i in range(10))
uuidTxt = uuid.uuid4().__str__().replace("-","")
print( 'uuid:', uuidTxt )
otpText = ''.join(random.choice(uuidTxt) for i in range(10))
print( 'otpText:', otpText )

body = 'Enter the following Text as OTP : ' +  otpText

email = EmailMessage()

email[ 'FROM' ] = emailSender
email[ 'TO' ] = emailReceiver
email[ 'SUBJECT' ] = subject
email.set_content( body )

context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com', 465, context=context ) as smtp:
    smtp.login( emailSender, emailPassword )
    smtp.sendmail(
        emailSender,
        emailReceiver,
        email.as_string()
    )