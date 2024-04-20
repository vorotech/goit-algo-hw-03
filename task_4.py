"""Module `task_04` provides function `get_upcoming_birthdays` that calculates upcoming birthdays 
for provided list of users for next 7 dasys including today."""

import datetime

def get_upcoming_birthdays(users):
    """Calculates upcoming birthdays for provided list of users for next 7 dasys including today."""
    today = datetime.date.today()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime.date(today.year, birthday.month, birthday.day)
        # 7 days including today is 6 days from today
        if today <= birthday_this_year <= (today + datetime.timedelta(days=6)):
            congratulation_date = birthday_this_year
            if birthday_this_year.weekday() in (5, 6):
                congratulation_date = birthday_this_year + \
                    datetime.timedelta(days = 7 - birthday_this_year.weekday())

            upcoming_birthdays.append(
                {
                    'name': user["name"],
                    'congratulation_date': congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.04.19"},
    {"name": "Jane Smith", "birthday": "1985.04.20"},
    {"name": "Bibop", "birthday": "1988.04.21"},
    {"name": "Picka Picka", "birthday": "2002.04.22"},
    {"name": "Mr. Anderson", "birthday": "2000.04.26"},
    {"name": "Trinity", "birthday": "1999.04.27"},
    {"name": "Morpheus", "birthday": "1980.04.28"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
