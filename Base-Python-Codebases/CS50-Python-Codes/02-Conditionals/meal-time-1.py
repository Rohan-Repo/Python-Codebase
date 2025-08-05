"""
Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, 
lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.

In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time 
as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, 
or anytime in between, it’s time for breakfast.
"""

def main():
    # tyms_1 = [ '7:30', '8:00', '6:12', '12:59', '13:00', '15:00', '18:12', '19:00', '20:00' ]
    # for tym in tyms_1:
    #     tymCheck_2(tym)
    
    tyms_2 = [ '11:30 A.M.', '1:00 a.m.', '12:12 am', '12:59 a.m.', '1:00 p.m.', '3:00 p.m.', '6:12 p.m.', '7:00 p.m.', '9:00 p.m.' ]
    for tym in tyms_2:
        tymCheck_1(tym)
    

def tymCheck_1(tym):
    # tyms = [ '7:30', '8:00', '6:12', '12:59', '13:00', '15:00', '18:12', '19:00', '20:00' ]

    # conv_time = convert_12_hour( input('What time is it?') )

    conv_time = convert_12_hour(tym)

    print( tym, '-', conv_time )
    if conv_time == -99:
        print( 'Invalid Time Entered' )
    else:
        if int(conv_time) == 7 or conv_time == 8.0:
            print( 'breakfast time' )
        elif int(conv_time) == 12 or conv_time == 13.0:
            print( 'lunch time' )
        elif int(conv_time) == 18 or conv_time == 19.0:
            print( 'dinner time' )

def tymCheck_2(tym):
    # tyms = [ '7:30', '8:00', '6:12', '12:59', '13:00', '15:00', '18:12', '19:00', '20:00' ]

    # conv_time = convert_24_hour( input('What time is it?') )

    conv_time = convert_24_hour(tym)

    print( tym )

    if conv_time == -99:
        print( 'Invalid Time Entered' )
    else:
        if int(conv_time) == 7 or conv_time == 8.0:
            print( 'breakfast time' )
        elif int(conv_time) == 12 or conv_time == 13.0:
            print( 'lunch time' )
        elif int(conv_time) == 18 or conv_time == 19.0:
            print( 'dinner time' )

def convert_24_hour(time):
    
    # hours:minutes Split - Separate Hours & Minutes
    time_sp = time.split(':')
    
    mins = float(time_sp[1])
    hours = float(time_sp[0])

    if  mins > 59:
        return (-99)
    else:
        if mins == 0.0:
            mins = 0
        elif mins == 30:
            mins = 0.5
        elif mins < 30:
            mins = 0.2
        else:
            mins = 0.8
        
        return hours + mins

def convert_12_hour(time):
    
    # hours:minutes meridiem Split - Separate AM/PM
    time = time.split()
    
    # hours:minutes Split - Separate Hours & Minutes
    time_sp = time[0].split(':')
    
    mins = float(time_sp[1])
    hours = float(time_sp[0])

    # Add 12 Hours for Post meridiem
    if time[1] == 'PM' or time[1] == 'P.M.' or time[1] == 'p.m.':
        # Adding 12 to 12 makes it 24 so exclude that 
        if hours != 12:
            hours = hours + 12.0

    # Delete 12 Hours for 12 AM
    if time[1] == 'AM' or time[1] == 'A.M.' or time[1] == 'a.m.':
        # Subtractng 12 for 12AM
        if hours == 12:
            hours = hours - 12.0

    if  mins > 59:
        return (-99)
    else:
        if mins == 0.0:
            mins = 0
        elif mins == 30.0:
            mins = 0.5
        elif mins < 30.0:
            mins = 0.2
        else:
            mins = 0.8
        
        return hours + mins

if __name__ == "__main__":
    main()