import datetime as dt

lera_birthday = dt.date(2015, 5, 16)
maxim_birthday = dt.date(2011, 12, 16)


def get_days_to_birthday(date_birthday):
    today = dt.date.today()
    today_year = today.year
    date_birthday = date_birthday.replace(year=today_year)

    if date_birthday < today:
        date_birthday = date_birthday.replace(year=today_year + 1)

    days_left = (date_birthday - today).days
    return days_left


print(get_days_to_birthday(lera_birthday))
print(get_days_to_birthday(maxim_birthday))