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
    choice = int(input('Choose an option: '))

    return choice

a = menu()
print('\ntest\n')
print(a)
