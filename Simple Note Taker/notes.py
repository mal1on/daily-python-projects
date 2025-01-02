'''
Terminal-based note manager that allows users to add or view notes
stored in a text file.
'''


def menu():
    print('\nMenu: ')
    print('1. Add note')
    print('2. View all notes')
    print('3. Exit')
    choice = input('Choose an option (1, 2 or 3): ')
    return choice


def add_note(notes_list, file):
    note = input('Enter your note: ')
    notes_list.append(note)
    file.write(note + '\n')
    print('Note added.')


def view_notes(notes_list):
    if notes_list:
        print('Notes list: ')
        for note in notes_list:
            print('- ' + note.strip())
    else:
        print('No notes')


def main():
    with open('notes.txt', 'a+') as file:
        file.seek(0)
        notes = file.readlines()

        while True:
            choice = menu()
            match choice:
                case '1':
                    add_note(notes, file)
                case '2':
                    view_notes(notes)
                case '3':
                    print('\nExiting...\n')
                    break
                case _:
                    print('Enter valid choice - 1-3')


if __name__ == '__main__':
    main()
