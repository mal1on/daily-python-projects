from datetime import datetime
from random import choice

'''
Program that reads a list of motivational quotes from a text file and
selects one to display every Monday (or any day the user runs the
program). It uses Python's date handling to check the current day and
ensures you’re greeted with a new quote each time you run it.
'''


def quote():
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    today = days[datetime.today().weekday()]

    with open('quotes.txt') as f:
        quotes = f.readlines()

    text = choice(quotes)

    if today == 'Monday':
        print("It's Monday! Time for some motivation!\n")
        print('Motivational quote of the day:')
        print(text)
    else:
        print(f'Today is {today}!')


if __name__ == '__main__':
    quote()
