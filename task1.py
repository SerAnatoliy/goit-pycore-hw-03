import datetime

def get_days_from_today(date):
    today = datetime.date.today()
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    delta = today - date
    return delta.days

print (get_days_from_today("2021-05-05"))