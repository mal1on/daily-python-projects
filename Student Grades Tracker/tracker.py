'''
Program that runs on the terminal and lets the user store student names
and their grades.
'''


def tracker():

    grades = {}

    while True:
        print('\nMenu:')
        print('1. Add a student and their grade')
        print('2. View all students and their grades')
        print('3. Exit')

        option = input('Choose an option (1-3): ')

        match option:
            case '1':
                name = input("Enter the student's name: ")
                grade = input(f"Enter {name}'s grade: ")
                if name and grade:
                    grades[name] = grade
                    print(f"{name}'s grade has been added.")
                else:
                    print('\nYou should enter name and grade')
            case '2':
                if not grades:
                    print('\nNo grades are entered')
                for name, grade in grades.items():
                    print(f"{name}'s grade is {grade}")
            case '3':
                print('\nExiting...\n')
                break
            case _:
                print('\nChoose available menu option')


if __name__ == '__main__':
    tracker()
