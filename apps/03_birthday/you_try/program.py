import datetime


def print_header():
    print('--------------------------')
    print('     BIRTHDAY APP')
    print('--------------------------')


def get_birth_date():
    print('When were you born')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))
    return datetime.date(year, month, day)


def compute_days_between_dates(user_date, target_date):
    new_date = datetime.date(target_date.year, user_date.month, user_date.day)
    return (new_date - target_date).days


def print_birthday_information(days):
    if days < 0:
        print('Your birthday was {0} days ago'.format(-days))
    elif days > 0:
        print('Your birthday is in {0} days time'.format(days))
    else:
        print('Happy birthday')


def main():
    print_header()
    bday = get_birth_date()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)


if __name__ == '__main__':
    main()
