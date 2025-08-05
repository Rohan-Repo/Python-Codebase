"""
Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, 
lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.

In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time 
as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, 
or anytime in between, it’s time for breakfast.
"""

def main():

    tym = convert( input('What time is it? ') )

    # breakfast: 7 to 8
    if int(tym) == 7 or tym == 8.0:
        print( 'breakfast time')
    # lunch: 12 to 13
    if int(tym) == 12 or tym == 13.0:
        print( 'lunch time')
    # dinner: 18 to 19
    if int(tym) == 18 or tym == 19.0:
        print( 'dinner time')

def convert(time):
    time_sp = time.split(":")

    hours = float( time_sp[0] )
    mins = float( time_sp[1] )

    # To convert minutes into a float value we divide it by 60
    mins = mins / 60

    return hours + mins

if __name__ == "__main__":
    main()