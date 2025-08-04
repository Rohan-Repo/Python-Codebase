from email.message import EmailMessage
import ssl
import smtplib

# Put in your Gmail Email Address and App Password Created inside Google Account below
emailSender = 'test@gmail.com'
emailPassword = 'testAppPassword'

emailReceiver = 'test@gmail.com'

subject = "Test Email from Python Code"

body = 'Sample Body Text'

email = EmailMessage()

email[ 'FROM' ] = emailSender
email[ 'TO' ] = emailReceiver
email[ 'SUBJECT' ] = subject
email.set_content( body )

context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com', 465, context=context ) as smtp:
    smtp.login( emailSender, emailPassword )
    s = smtp.sendmail(
        emailSender,
        emailReceiver,
        email.as_string()
    )