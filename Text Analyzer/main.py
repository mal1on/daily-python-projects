from collections import Counter


def main():
    '''Takes a block of text provided by the user, analyzes it, and
     provides useful statistics about the text to the user.'''

    text = input('Enter text to analyze: ')

    words = Counter(text.split())
    sentences = text.split('.')[:-1]
    chars = len(text.replace(' ', ''))
    most_freq = ['"' + t[0].lower() + '"' for t in words.most_common(3)]
    avg_word_l = chars // len(text.split())
    avg_sent_l = len(text.split()) // len(sentences)

    print(f'There are {len(words)} words, {len(sentences)} sentences and \
{chars} non-blank characters in the text entered.')
    print(f'The three most frequent words in the text are \
{", ".join(most_freq[:-1])} and {most_freq[-1]}.')
    print(f'The average word length is {avg_word_l} and the average \
sentence length is {avg_sent_l}.')


if __name__ == '__main__':
    main()
