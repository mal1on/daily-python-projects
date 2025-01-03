'''
Command-line calculator that performs basic mathematical operations.
'''


def calculator():

    print('\nText-Vased Calculator')
    print('Enter a mathematical expression (e.g., 5 + 3) or type "exit" to quit.')

    while True:
        expression = input('Enter expression: ')
        if expression:
            if expression == 'exit':
                print('\nExiting...\n')
                break
            try:
                print(f'Result: {eval(expression)}')
            except ZeroDivisionError:
                print('Error: Division by zero is not allowed.')
            except Exception as e:
                print(f'Error: Invalid operation ({e}).')
        else:
            print('Expression can not be empty.\n')


if __name__ == '__main__':
    calculator()
