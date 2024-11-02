import csv


def vocabulary():
    '''
    Program where users can add a word and the translation for that
    word through a command line interface. The program saves the
    results in a CSV file.
    '''
    words = [('Language 1', 'Language 2')]
    while True:
        word = input('Enter a word in language 1 (or type "done" to finish): ')
        if word != 'done':
            trans = input(f'Enter the translation of "{word}" in language 2: ')
            words.append((word.lower(), trans.lower()))
        else:
            break

    with open('data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(words)


if __name__ == '__main__':
    vocabulary()
