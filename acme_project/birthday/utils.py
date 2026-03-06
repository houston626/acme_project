from datetime import datetime

def calculate_birthday_countdown(birthday):

    today = datetime.now().date()

    next_birthday = birthday.replace(year=today.year)

    if next_birthday < today:
        next_birthday = birthday.replace(year=today.year + 1)

    return (next_birthday - today).days