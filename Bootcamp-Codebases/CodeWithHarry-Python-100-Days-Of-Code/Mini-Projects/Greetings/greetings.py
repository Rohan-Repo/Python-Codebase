import time
# print( 'Current Time: ', time.strftime('Day:%d, Month:%b Year:%Y Hour:%H Minutes:%M Seconds:%S Zone:%Z' ) )
print( 'Current Time: ', time.strftime('%d, %b %Y | %H:%M:%S | %Z' ) )

time_in_hours = int(time.strftime('%H'))

print( 'Alexa Greet Me:' )

if time_in_hours>6 and time_in_hours<=11:
    print( 'Good Morning' )
elif time_in_hours == 12:
    print( 'Happy Noon' )
elif time_in_hours>=13 and time_in_hours<=15:
    print( 'Good Afternoon' )
elif time_in_hours>=16 and time_in_hours <=21:
    print( 'Good Evening' )
else:
    print( 'Good Night' )

hourList = [ 4, 7, 12, 14, 17, 21, 23]

for hour in hourList:
    if hour>6 and hour<=11:
        print( hour, ' : ', 'Good Morning' )
    elif hour == 12:
        print( hour, ' : ', 'Happy Noon' )
    elif hour>=13 and hour<=15:
        print( hour, ' : ', 'Good Afternoon' )
    elif hour>=16 and hour <=21:
        print( hour, ' : ', 'Good Evening' )
    else:
        print( hour, ' : ', 'Good Night' )
