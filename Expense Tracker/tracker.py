from datetime import datetime


'''
Command-line app to track daily expenses. The app allows users to add
expenses, view a summary of all expenses, and calculate total spending
for a given period.
'''


def menu():
    print('\nWelcome to the Expense Tracker!')
    print('1. Add an expense')
    print('2. View all expenses')
    print('3. Search expense by date')
    print('4. Calculate total spending')
    print('5. Exit')
    while True:
        try:
            choice = int(input('Choose an option: '))
            if choice in range(1, 6):
                break
            else:
                print('Choose available option (1-5).')
        except ValueError:
            print('Choose available option (1-5).')

    return choice


def tracker():

    with open('expenses.txt', 'a+') as file:
        file.seek(0)
        expenses = file.readlines()
        while True:
            option = menu()
            match option:
                case 1:
                    while True:
                        date = input('Enter date (YYYY-MM-DD): ')
                        try:
                            date_o = datetime.strptime(date, '%Y-%m-%d')
                            break
                        except ValueError:
                            print('Enter correct date (YYYY-MM-DD)')

                    date = datetime.strftime(date_o, '%Y-%m-%d')
                    cat = input('Enter category: ')
                    desc = input('Enter description: ')
                    while True:
                        try:
                            amount = float(input('Enter amount: '))
                            break
                        except ValueError:
                            print('Enter correct amount (int or float).')
                    expenses.append(f'{date},{cat},{desc},{amount}')
                    file.write(f'\n{date},{cat},{desc},{amount}')
                    print('Expense added successfully!')
                case 2:
                    print('\n--- All Expenses ---')
                    print(
                        f'{"Date":<15}| {"Category":<10}| {"Description":<20}| {"Amount":<10}|')
                    print(
                        '--------------------------------------------------------------')
                    for e in expenses:
                        if e != '\n':
                            e = e.split(',')
                            print(
                                f'{e[0]:<15}| {e[1]:<10}| {e[2]:<20}| {float(e[3]):<10.2f}|')
                case 3:
                    date = input('Enter date (YYYY-MM-DD): ')
                    found = []
                    for e in expenses:
                        e = e.split(',')
                        if e[0] == date:
                            found.append(e)
                    if found:
                        print(f'\n--- Expenses for {date} ---')
                        print(
                            f'{"Category":<10}| {"Description":<20}| {"Amount":<10}|')
                        print(
                            '---------------------------------------------')
                        for e in found:
                            print(
                                f'{e[1]:<10}| {e[2]:<20}| {float(e[3]):<10.2f}|')
                case 4:
                    total = sum([float(e.split(',')[3])
                                 for e in expenses if e != '\n'])
                    print(f'\nTotal spending: ${total:.2f}')
                case 5:
                    print('Exiting...\n')
                    break


if __name__ == '__main__':
    tracker()
