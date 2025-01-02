'''
Allows the user to input a list of words in the terminal.
Identifies the longest word(s) in the list, including multiple words
with the same maximum length and prints out a message that includes the
number of characters of that word.
'''


def finder():

    words = input('Enter a list of words separated by spaces: ').split()

    if not words:
        print('No words entered')
        return

    longest = len(max(words, key=len))

    print(f'The longest words(s) with {longest} characters: ')
    for word in words:
        if len(word) == longest:
            print(f'- {word}')


if __name__ == '__main__':
    finder()
