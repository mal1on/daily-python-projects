def check(number):
    '''Check if Number is Positive or Negative'''

    if number > 0:
        return f'The number {number} is positive.'
    elif number < 0:
        return f'The number {number} is negative.'
    else:
        return f'The number {number} is zero.'


def get_number():
    '''Get number to check it'''

    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print('Please enter valid number.')

    print(check(number))


if __name__ == '__main__':
    get_number()
