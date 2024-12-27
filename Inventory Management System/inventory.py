'''
Command-line app that allows a small business to manage their inventory.
'''


def inventory():

    stock = []

    while True:
        print('\nWelcome to the Inventory Management System!')
        print('1. Add new item')
        print('2. Update stock')
        print('3. View inventory')
        print('4. Search for an item')
        print('5. Exit')
        while True:
            option = int(input('Choose an option: '))
            if option in range(1, 6):
                break
            else:
                print('Choose correct option (1-5)')

        match option:
            case 1:
                item = dict()
                item['name'] = input('Enter item name: ')
                while True:
                    try:
                        item['quantity'] = int(input('Enter quantity: '))
                        item['price'] = float(input('Enter price: '))
                        break
                    except ValueError:
                        print('Enter correct value (int or float)')
                stock.append(item)
                print('Item added successfully!')
            case 2:
                name = input('Enter item name to update: ')
                check = False
                for item in stock:
                    if item['name'] == name:
                        check = True
                        item['quantity'] = int(input('Enter new quantity: '))
                if check:
                    print('Item updated successfully!')
                else:
                    print('Item not found.')
            case 3:
                print('Inventory: ')
                count = 0
                for item in stock:
                    count += 1
                    print(
                        f"{count}. {item['name']} - Quantity: {item['quantity']}, Price: ${item['price']:.2f}")
            case 4:
                term = input('Enter item name to search: ')
                check = False
                for item in stock:
                    if item['name'] == term:
                        check = True
                        print(
                            f"Found: {item['name']} - Quantity: {item['quantity']}, Price: ${item['price']:.2f}")
                if not check:
                    print('Item not found.')
            case 5:
                print('Exiting...')
                break


if __name__ == '__main__':
    inventory()
