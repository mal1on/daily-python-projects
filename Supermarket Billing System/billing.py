'''
Command line program that simulates a basic billing system for a
supermarket. The user can input items purchased (e.g., butter, eggs,
etc), their prices, and quantities. The app will calculate the total
bill, apply any applicable discounts, and display an itemized bill
summary.
'''


def billing():

    print('Welcome to the Supermarket Billing System')
    while True:
        try:
            items = int(input('Enter the number of items: '))
            if items in range(1, 100):
                break
            else:
                print('\nEnter valid choice (1-100).\n')
        except ValueError:
            print('\nEnter valid choice (1-100).\n')

    bill = []

    for i in range(1, items + 1):
        item = {}
        print(f'\nItem {i}: ')
        name = input('Name: ')
        item['name'] = name
        price = float(input('Price per unit: '))
        item['price'] = price
        quantity = int(input('Quantity: '))
        item['quantity'] = quantity
        bill.append(item)

    total = 0
    print('\n--- Bill summary ---')
    for i in bill:
        i_total = i['quantity'] * i['price']
        total += i_total
        print(f"{i['name']}: {i['quantity']} x ${i['price']:.2f} = ${i_total:.2f}")
    print(f'Subtotal: ${total:.2f}')
    print('Discount: $0.00')
    tax = total * 0.05
    total += tax
    print(f'Sales Tax (5%): {tax:.2f}')
    print(f'Total: ${total:.2f}')
    print('\nThank you for shopping with us!')


if __name__ == '__main__':
    billing()
