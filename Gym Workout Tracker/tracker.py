'''
This program helps you track your workout routines, sets, reps, and
weights. It lets you add exercises, record your progress, and review
past workouts.
'''


class Tracker():
    '''Gym tracker class'''

    def __init__(self):
        self.workout = dict()

    def add_exercise(self):

        name = input('Enter exercise name: ').strip().lower()
        if not name:
            print('Exercise name cannot be empty.')
            return
        if name not in self.workout:
            self.workout[name] = []
            print(f'Added exercise: {name.capitalize()}')
        else:
            print(f'{name.capitalize()} is already added.\n')

    def log_workout(self):
        name = input('Enter exercise name: ').strip().lower()
        if not name:
            print('Exercise name cannot be empty.')
            return
        if name in self.workout:
            try:
                sets = int(input('Enter number of sets: '))
                reps = int(input('Enter number of reps: '))
                weight = float(input('Enter weight in kg: '))
                self.workout[name].append((sets, reps, weight))
                print(
                    f'Logged {sets} sets of {reps} reps at {weight} kg for {name.capitalize()}')
            except ValueError:
                print('Please enter correct numeric values.')
                return
        else:
            print(f'{name.capitalize()} is not added to the workout.')

    def view_progress(self):
        if self.workout:
            for exercise, sessions in self.workout.items():
                print(f'\nProgress for {exercise.capitalize()}: ')
                if sessions:
                    for ind, session in enumerate(sessions, start=1):
                        sets, reps, weight = session
                        print(
                            f'Session {ind}: {sets} sets of {reps} reps at {weight} kg')
                else:
                    print(f'No sessions recorded for {exercise.capitalize()}')
        else:
            print('No workout data available.')


def main():
    '''Main function'''

    app = Tracker()
    while True:
        print('\n🏋🏻‍ Gym Tracker Options:')
        print('1. Add Exercise')
        print('2. Log Workout')
        print('3. View Progress')
        print('4. Exit')
        option = input('Choose an option: ')
        match option:
            case '1':
                app.add_exercise()
            case '2':
                app.log_workout()
            case '3':
                app.view_progress()
            case '4':
                print('Exiting...')
                break
            case _:
                print('Please enter valid choice (1-4).')


if __name__ == '__main__':
    main()
