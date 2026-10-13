import calendar
import datetime

# 1. Detect current year and month
now = datetime.datetime.now()
current_year = now.year
current_month = now.month

# 2. Initialize the HTML Calendar class
# You can set the first day of the week here (e.g., calendar.SUNDAY)
html_cal = calendar.HTMLCalendar(firstweekday=calendar.SUNDAY)

# 3. Generate the raw HTML table for the month
html_output = html_cal.formatmonth(current_year, current_month)

# 4. Save the layout to an HTML file on your system
file_name = f"calendar_{current_year}_{current_month}.html"

with open(file_name, "w") as file:
    file.write(html_output)

print(f"Successfully generated and saved: {file_name}")