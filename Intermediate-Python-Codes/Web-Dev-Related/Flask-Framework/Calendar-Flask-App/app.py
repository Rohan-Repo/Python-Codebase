import calendar
import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Grab current year and render full year calendar template
    now = datetime.datetime.now()
    year = now.year

    html_cal = calendar.HTMLCalendar(firstweekday=calendar.SUNDAY)
    raw_calendar_html = html_cal.formatyear(year, width=3)

    return render_template('index.html', calendar_table=raw_calendar_html, current_year=year)

@app.route('/currMonth')
def current_month():
    # Grab current year and month and render single month template
    now = datetime.datetime.now()
    year = now.year
    month = now.month

    html_cal = calendar.HTMLCalendar(firstweekday=calendar.SUNDAY)
    raw_calendar_html = html_cal.formatmonth(year, month)

    return render_template('index-currMonth.html', calendar_table=raw_calendar_html)

if __name__ == '__main__':
    app.run(debug=True, extra_files=['templates/index.html', 'templates/index-currMonth.html'])