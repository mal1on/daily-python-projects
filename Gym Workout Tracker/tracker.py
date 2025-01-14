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
        try:
            name = input('Enter exercise name: ').lower()
        except Exception as e:
            print(f'Please enter correct exercise name. Error: {e}')
        if name not in self.workout:
            self.workout[name] = dict()
        else:
            print(f'{name.capitalize()} is already added.\n')

    def log_workout(self):
        try:
            name = input('Enter exercise name: ').lower()
        except Exception as e:
            print(f'Please enter correct exercise name. Error: {e}')
        if name in self.workout:
            try:
                sets = int(input('Enter number of sets: '))
                reps = int(input('Enter number of reps: '))
                weight = float(input('Enter weight in kg: '))
            except ValueError:
                print('Please enter correct value.')
            self.workout[name]['sets'] = sets
            self.workout[name]['reps'] = reps
            self.workout[name]['wight'] = weight
        else:
            print(f'{name.capitalize()} is not added to the workout.')


test = Tracker()
test.add_exercise()
print(test.workout)
test.log_workout()
print(test.workout)
