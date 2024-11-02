import os


def vocabulary():
    '''
    The program allows users to add a word and the translation for that
    word through a command line interface and saves the results in a
    text file.
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

    with open('data.txt', 'w') as file:
        for word, trans in words:
            file.write(word + ' - ' + trans + '\n')

    dash = '-' * os.get_terminal_size().columns
    print('Bilingual vocabulary created: ')
    print(dash)
    for word, trans in words[1:]:
        print(f'{word}: {trans}')
    print(dash)
    print(
        f'The vocabulary has been saved to: {os.path.join(os.getcwd(), "data.txt")}')


if __name__ == '__main__':
    vocabulary()
