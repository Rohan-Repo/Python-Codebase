# The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5?
PI = 3.141592
rad = 5

volume = (4/3) * PI * (rad ** 3)
print( 'Problem #1:' )
print( '\t Volume of Sphere with Radius 5 = ', round( volume, 4) )

print( 'Problem #2:' )
# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
org_price = 24.95
disc_price = org_price - (org_price * (40/100))
disc_price = round( disc_price, 3)

print( '\t org_price = $', org_price )
print( '\t disc_price = $', disc_price )
total_shipping_cost = 3 + (0.75 * 59)
print( '\t total_shipping_cost = $', total_shipping_cost )
total_wholesale_cost = (disc_price * 60) + total_shipping_cost
print( '\t total_wholesale_cost = $', total_wholesale_cost )

"""
This is a classic problem in running. To solve this problem, 
we need to calculate the total time taken to run the given distance 
and then add it to the start time to get the end time.

First, let's calculate the time taken to run 1 mile at an easy pace 
of 8 minutes and 15 seconds per mile. We can convert the pace to seconds 
per mile by multiplying 8 minutes by 60 seconds and adding 15 seconds to 
get 495 seconds per mile. Therefore, the time taken to run 1 mile at an 
easy pace is 495 seconds.

Next, let's calculate the time taken to run 3 miles at a tempo pace of 
7 minutes and 12 seconds per mile. We can convert the pace to 
seconds per mile by multiplying 7 minutes by 60 seconds and adding 12 seconds 
to get 432 seconds per mile. Therefore, the time taken to run 3 miles at 
a tempo pace is 1296 seconds.

Finally, let's calculate the time taken to run 1 mile at an easy pace of 
8 minutes and 15 seconds per mile. We already know that the time taken to
 run 1 mile at an easy pace is 495 seconds.

To calculate the total time taken, we add the time taken to run each segment: 
495 seconds + 1296 seconds + 495 seconds = 2286 seconds.

Now, we need to convert the total time taken from seconds to minutes and seconds. 
We can do this by dividing the total time taken by 60 to get the number of minutes 
and taking the remainder to get the number of seconds. Therefore, the 
total time taken is 38 minutes and 6 seconds.

Adding 38 minutes and 6 seconds to the start time of 6:52 am, we get the end time of 7:30:06 am.

Therefore, you will get home at **7:30:06 am** for breakfast.

I hope this helps! Let me know if you have any other questions.
"""

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

# Convert to Seconds per Mile
easy_pace_run = 8 * 60 + 15

tempo_pace_run = 7 * 60 + 12

total_time_taken_seconds = 1 * easy_pace_run + 3 * tempo_pace_run + 1 * easy_pace_run

total_time_taken_in_mins = total_time_taken_seconds // 60

total_time_taken_in_secs = total_time_taken_seconds % 60

print( 'Problem #3 : ' )
print( '\t easy_pace_run 1 Mile in seconds : ', easy_pace_run )
print( '\t tempo_pace_run 1 Mile in seconds : ', tempo_pace_run )
print( '\t total_time_taken_seconds: ', total_time_taken_seconds )
print( '\t total_time_taken_in_mins: ', total_time_taken_in_mins )
print( '\t total_time_taken_in_secs: ', total_time_taken_in_secs )

import datetime

date_time_val = datetime.datetime( 2023, 11, 21, 7,52,0 )

print( '\t Start Time: ', date_time_val )

time_change = datetime.timedelta(minutes=total_time_taken_in_mins, seconds=total_time_taken_in_secs)
final_time = date_time_val + time_change

print( '\t End Time: ', final_time )
