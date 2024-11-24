def atm():
    '''
    Simplified ATM Simulation program where the user interacts with an
    ATM-like interface through the command line. The user can perform
    basic transactions, such as checking their balance, depositing
    money, and withdrawing money.
    '''
    balance = 100
    print('Welcome to the ATM!\n')

    while True:
        print(f'Current Balance: ${balance}')
        print('1. Check Balance')
        print('2. Deposit Money')
        print('3. Withdraw Money')
        print('4. Exit')
        option = int(input('Choose an option: '))
        match option:
            case 1:
                print(f'Your balance is: ${balance}\n')
            case 2:
                deposit = int(input('Enter amount to deposit: '))
                if deposit > 0:
                    balance += deposit
                    print(
                        f'Deposit successful! Your new balance is: ${balance}\n')
                else:
                    print('Please enter valid deposit amount\n')
            case 3:
                withdraw = int(input('Enter amount to withdraw: '))
                if 0 < withdraw <= balance:
                    balance -= withdraw
                    print(
                        f'Withdraw successful! Your new balance is: ${balance}\n')
                else:
                    print('Please enter valid withdraw amount\n')
            case 4:
                break
            case _:
                print('Please enter a valid choice\n')


if __name__ == '__main__':
    atm()
