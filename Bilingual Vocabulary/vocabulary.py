import csv
import os


def vocabulary():
    '''
    Program where users can add a word and the translation for that
    word through a command line interface. The program saves the
    results in a CSV file.
    '''
    words = [('Language 1', 'Language 2')]
    while True:
        word = input('Enter a word in language 1 (or type "done" to finish): ')
        if word.lower() != 'done':
            trans = input(f'Enter the translation of "{word}" in language 2: ')
            words.append((word.lower(), trans.lower()))
            print(
                f'"{word.lower()}" with translation "{trans.lower()}" has been added')
        else:
            break

    with open('data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(words)

    dash = '-' * os.get_terminal_size().columns
    print('Bilingual vocabulary created: ')
    print(dash)
    for word, trans in words[1:]:
        print(f'{word}: {trans}')
    print(dash)


if __name__ == '__main__':
    vocabulary()
