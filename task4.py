import datetime
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Ann Brown", "birthday": "1995.01.30"},
    {"name": "Joe Davis", "birthday": "2000.02.02"},
    {"name": "Alice White", "birthday": "2005.02.05"},
    {"name": "Bob Green", "birthday": "2010.10.06"},
]


def get_upcoming_birthdays(users):
    today = datetime.date.today()
    next_week = today + datetime.timedelta(days=7)
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
    
    if birthday_this_year < today:
        birthday_this_year = birthday_this_year.replace(year=today.year + 1)
    
    if today <= birthday_this_year <= next_week:
        
        if birthday_this_year.weekday() >=4:
            days_to_monday = 7 - birthday_this_year.weekday()
            congrats_day= birthday_this_year + datetime.timedelta(days=days_to_monday)
        else:
            congrats_day = birthday_this_year

        upcoming_birthdays.append({"name": user["name"], "birthday": congrats_day.strftime("%Y.%m.%d")})
    
    return upcoming_birthdays
print(get_upcoming_birthdays(users))