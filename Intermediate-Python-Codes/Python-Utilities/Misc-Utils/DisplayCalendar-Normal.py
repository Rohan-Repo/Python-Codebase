import datetime
import calendar

# 1. Detect the current system year and month
now = datetime.datetime.now()
current_year = now.year
current_month = now.month

# 2. Print the current values
print(f"Current Year: {current_year}")
print(f"Current Month: {current_month} ({calendar.month_name[current_month]})\n")

# 3. Generate and display the formatted monthly calendar
print(calendar.month(current_year, current_month))

# 4. Print the Calendar for the whole year
print( '\n Calendar for the Whole Year:')
print( calendar.calendar( current_year) )