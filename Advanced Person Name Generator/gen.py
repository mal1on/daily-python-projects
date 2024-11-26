import random


def gen():
    '''
    The program starts by showing the user a menu. The user enters a
    number (e.g., 2 to add a new name to the text file) and then
    proceeds with the instructions (e.g., adding a name such as Wimbly).
    The program adds that new name to the names.txt file and then shows
    the menu again. In addition to adding new names, the user can also
    display the total number of names, and select a random name from
    the text file.
    '''
    while True:
        print('Please select an option: ')
        print('1. Show the total number of names')
        print('2. Add new name')
        print('3. Select a random name')
        print('4. Exit')
        choice = int(input('Enter your choice (1-4): '))
        match choice:
            case 1:
                with open('names.txt') as f:
                    print(
                        f'The total number of names is: {len(f.readlines())}\n')
            case 2:
                name = input('Enter the new name to add: ').capitalize()
                with open('names.txt', 'a') as f:
                    f.write(name + '\n')
                print(f'{name} has been added to the file\n')
            case 3:
                with open('names.txt') as f:
                    names = f.readlines()
                    name = random.choice(names)
                print(f'Selected name is: {name}')
            case 4:
                print('Exiting...')
                break
            case _:
                print('Please enter valid choice (1-4)\n')


if __name__ == '__main__':
    gen()
