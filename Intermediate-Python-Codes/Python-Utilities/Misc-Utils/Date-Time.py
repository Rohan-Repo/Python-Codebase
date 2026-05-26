# Date Formatting
# pip install pytz 

import datetime


date_now = datetime.datetime.now()

print( 'Default DateTime Format : ', date_now )
# Weekday, Day-Month(Str)-Year, Hour:Minutes:Seconds
print( '\n Date Format 1 : {:%A, %d-%B-%Y %I:%M:%S}'.format(date_now) )


# Weekday, Day, Month, Year, Hour:Minutes:Seconds AM/PM Zone
print( '\n Date Format 2 : {:%A, %d, %B, %Y %I:%M:%S %p %Z}'.format(date_now) )

# F-Strings : Specify F" or F' or F""" or f' or f" or f""" to Let Python know you are using F-Strings
# Alternative to .format Method : Can be used as Placeholder, Padding, Calculations

import time 

time_now = time.asctime()
print( '\n Default Time Format : ', time_now )

# Weekday, Year/Month(Num)/Day, Hour:Minutes:Seconds AM/PM Zone
time_now = time.strftime('%A, %Y/%m/%d,  %I:%M:%S %p %Z')
print( '\n Time Format 1 : {} \n'.format(time_now) )

# Weekday, Day, Month, Year, Hour:Minutes:Seconds AM/PM Zone
date_now = time.strftime('%A, %d, %B, %Y %I:%M:%S %p %Z')
print( f'Time Format 2 : {date_now} \n' )


from datetime import datetime
# pip install pytz
import pytz
print( pytz.all_timezones )

toronto_time = datetime.now(pytz.timezone('America/Toronto'))

print( 'Toronto : {:%A, %d, %B, %Y %I:%M:%S %p %Z}'.format(toronto_time) )

berlin_time = datetime.now(pytz.timezone('Europe/Berlin'))

print( 'Berlin : {:%A, %d, %B, %Y %I:%M:%S %p %Z}'.format(berlin_time) )

dubai_time = datetime.now(pytz.timezone('Asia/Muscat'))

print( 'Muscat : {:%A, %d, %B, %Y %I:%M:%S %p %Z}'.format(dubai_time) )

seoul_time = datetime.now(pytz.timezone('Asia/Seoul'))

print( 'Seoul : {:%A, %d, %B, %Y %I:%M:%S %p %Z}'.format(seoul_time) )

sydney_time = datetime.now(pytz.timezone('Australia/Sydney'))

print( 'Sydney : {:%A, %d, %B, %Y %I:%M:%S %p %Z}'.format(sydney_time) )