# Date Formatting
# pip install pytz 

import datetime
date_1 = datetime.datetime.now()

# Weekday, Day, Month, Year, Hour:Minutes:Seconds AM/PM Zone
print( 'Date Format # : {:%A, %d, %B, %Y %I:%M:%S %p %Z}'.format(date_1) )

# F-Strings : Specify F" or F' or F""" or f' or f" or f""" to Let Python know you are using F-Strings
# Alternative to .format Method : Can be used as Placeholder, Padding, Calculations

import time 
date_now = time.strftime('%A, %d, %B, %Y %I:%M:%S %p %Z')
print( f'F String #1 : {date_now} \n' )


from datetime import datetime
# pip install pytz
import pytz
print( pytz.all_timezones )

toronto_time = datetime.now(pytz.timezone('America/Toronto'))

print( 'Date Format # : {:%A, %d, %B, %Y %I:%M:%S %p %Z}'.format(toronto_time) )

berlin_time = datetime.now(pytz.timezone('Europe/Berlin'))

print( 'Date Format # : {:%A, %d, %B, %Y %I:%M:%S %p %Z}'.format(berlin_time) )

dubai_time = datetime.now(pytz.timezone('Asia/Muscat'))

print( 'Date Format # : {:%A, %d, %B, %Y %I:%M:%S %p %Z}'.format(dubai_time) )

seoul_time = datetime.now(pytz.timezone('Asia/Seoul'))

print( 'Date Format # : {:%A, %d, %B, %Y %I:%M:%S %p %Z}'.format(seoul_time) )

sydney_time = datetime.now(pytz.timezone('Australia/Sydney'))

print( 'Date Format # : {:%A, %d, %B, %Y %I:%M:%S %p %Z}'.format(sydney_time) )