import re
import os
from string import punctuation
from collections import Counter


def main():
    '''
    Takes a block of text provided by the user, analyzes it, and
    provides useful statistics about the text to the user.
    '''

    text = ''
    while not text:
        text = input('Enter text to analyze: ')

    words = Counter(text.split())
    sentences = len(re.findall('[.!?;]+ ', text)) + 1
    chars = len(text.translate(str.maketrans('', '', punctuation + ' ')))
    most_freq = ['"' + t[0].lower() + '"' for t in words.most_common(3)]
    avg_word_l = chars // len(text.split())
    avg_sent_l = len(text.split()) // sentences
    dash = '-' * os.get_terminal_size().columns

    print(dash)
    print(f'There are {len(words)} words, {sentences} sentences and \
{chars} non-blank characters in the text entered.')
    print(f'The average word length is {avg_word_l} characters and the \
average sentence length is {avg_sent_l} words.')
    if len(most_freq) > 2:
        print(f'The three most common words in the text are \
{", ".join(most_freq[:-1])} and {most_freq[-1]}.')
    else:
        print(f'The most common word in the text is {most_freq[0]}')
    print(dash)


if __name__ == '__main__':
    main()
