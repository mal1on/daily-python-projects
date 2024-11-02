import os


def manager():
    '''
    Program that lets the user submit names and phone numbers through
    the console and stores those numbers in a text file.
    '''
    contacts = []
    while True:
        name = input('Enter contact name (or type "done" to finish): ')
        if name.lower() != 'done':
            number = input(f'Enter phone number for {name}: ')
            contacts.append((name, number))
            print(
                f'"{name}" with phone number "{number}" has been added')
        else:
            break

    with open('contacts.txt', 'w') as file:
        for name, number in contacts:
            file.write(name + ': ' + number + '\n')

    dash = '-' * os.get_terminal_size().columns
    print('Contacts list created: ')
    print(dash)
    for name, number in contacts:
        print(f'{name}: {number}')
    print(dash)
    print(
        f'The contact list has been saved to: {os.path.join(os.getcwd(), "contacts.txt")}')


if __name__ == '__main__':
    manager()
