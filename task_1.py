"""Module `task_1` provides function `get_days_from_today(date)` that calculates number of days
between provided and today's date."""

import datetime

def get_days_from_today(date):
    """Calculates number of days between provided and today's date."""
    today = datetime.date.today()
    days_difference = None

    try:
        provided_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        days_difference = (today - provided_date).days
    except ValueError:
        print("Error: Invalid date format. Please provide date in format 'YYYY-MM-DD'.")

    return days_difference


date = input("Enter date in format 'YYYY-MM-DD': ")
diff = get_days_from_today(date)
print(f"Number of days between {date} and today is {diff}.")
