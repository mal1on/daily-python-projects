'''Basic console-based banking system'''


class Account:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        self.balance += amount

    def view_balance(self):
        print(f'Account holder: {self.name}, balance: {self.balance}')


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input('Enter your name: ')
        if not name:
            print('You should enter your name.')
            return
        try:
            deposit = float(input('Enter initial deposit: '))
        except ValueError:
            print('Enter correct deposit value.')
            return
        self.accounts[name] = Account(name, deposit)
        print(f'Account created for {name} with balance {deposit:.1f}')

    def deposit_money(self):
        name = input('Enter your name: ')
        if name in self.accounts:
            try:
                deposit = float(input('Enter amount to deposit: '))
            except ValueError:
                print('Enter correct deposit value.')
            self.accounts[name].deposit(deposit)
            print(
                f'{deposit:.1f} deposited. New balance: {self.accounts[name].balance}')
        else:
            print('Account not found.')

    def view_balance(self):
        name = input('Enter your name: ')
        if name in self.accounts:
            self.accounts[name].view_balance()
        else:
            print('Account not found.')

    def run(self):
        while True:
            print("\n1. Create Account\n2. Deposit Money\n3. View Balance\n4. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.deposit_money()
            elif choice == '3':
                self.view_balance()
            elif choice == '4':
                print('\nExiting...\n')
                break
            else:
                print('Enter valid menu choice (1-4).')


if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.run()
