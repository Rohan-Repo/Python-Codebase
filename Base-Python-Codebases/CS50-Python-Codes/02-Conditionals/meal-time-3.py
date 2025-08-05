"""
Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, 
lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.

In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time 
as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, 
or anytime in between, it’s time for breakfast.
"""

def main():

    conv_time = convert( input('What time is it? ') )

    # breakfast: 7 to 8
    if int(conv_time) == 7 or conv_time == 8.0:
        print( 'breakfast time')
    # lunch: 12 to 13
    if int(conv_time) == 12 or conv_time == 13.0:
        print( 'lunch time')
    # dinner: 18 to 19
    if int(conv_time) == 18 or conv_time == 19.0:
        print( 'dinner time')

def convert(time):

    # hours:minutes meridiem Split - Separate AM/PM
    time = time.strip().split()

    # hours:minutes Split - Separate Hours & Minutes
    time_sp = time[0].split(":")

    hours = float( time_sp[0] )
    mins = float( time_sp[1] )

    # Add 12 Hours for Post meridiem
    time[1] = time[1].lower()

    if time[1] == 'pm' or time[1] == 'p.m.':
        # Adding 12 to 12 makes it 24 so exclude that 
        if hours != 12:
            hours = hours + 12.0

    # Delete 12 Hours for 12 AM
    if time[1] == 'am' or time[1] == 'a.m.':
        # Subtractng 12 for 12AM
        if hours == 12:
            hours = hours - 12.0

    # To convert minutes into a float value we divide it by 60
    mins = mins / 60

    return hours + mins

if __name__ == "__main__":
    main()