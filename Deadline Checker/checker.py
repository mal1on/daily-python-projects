from datetime import datetime

'''
This program helps you keep track of deadlines by allowing you to input
a specific date and time. It calculates whether the deadline has already
passed, is happening today, or how many days remain until the deadline.
'''


def checker():
    while True:
        deadline = input('Enter the deadline (e.g., 2024-11-15 17:00): ')
        try:
            deadline_dto = datetime.strptime(deadline, '%Y-%m-%d %H:%M')
            break
        except ValueError:
            print('The date you entered is not in the correct format.')
    td = deadline_dto - datetime.now()
    days = td.days

    if days < 0:
        print(f'The deadline has passed! 😢')
    elif days == 0:
        hours = td.seconds / 3600
        print(f'You have {hours:.2f} hours left! 😰')
    else:
        print(f'The deadline is in {days} day(s). Keep working! 🚀')


if __name__ == '__main__':
    checker()
