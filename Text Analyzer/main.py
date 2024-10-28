import re
from string import punctuation
from collections import Counter



def main():
    '''Takes a block of text provided by the user, analyzes it, and
     provides useful statistics about the text to the user.'''

    # text = input('Enter text to analyze: ')
    text = "Musk, in particular, has a relationship with Erdoğan, whom The Atlantic described as making Turkey authoritarian again. The pair met in 2017, The Washington Post reported, and SpaceX signed a deal with Turkey in 2021. The next year at the World Cup, Musk and Erdoğan shook hands, the Post reported. Just last month, Insider reported, SpaceX assisted Turkey in a satellite launch, and critics believe that Musk's dealings with Erdoğan may have prompted Twitter's easy compliance with the most recent takedown request, seemingly intended to silence Erdoğan's detractors ahead of his re-election bid."

    words = Counter(text.split())
    sentences = len(re.findall('[.!?;]+ ', text)) + 1
    chars = len(text.translate(str.maketrans('', '', punctuation + ' ')))
    most_freq = ['"' + t[0].lower() + '"' for t in words.most_common(3)]
    avg_word_l = chars // len(text.split())
    avg_sent_l = len(text.split()) // sentences

    print(f'There are {len(words)} words, {sentences} sentences and \
{chars} non-blank characters in the text entered.')
    print(f'The three most frequent words in the text are \
{", ".join(most_freq[:-1])} and {most_freq[-1]}.')
    print(f'The average word length is {avg_word_l} and the average \
sentence length is {avg_sent_l}.')


if __name__ == '__main__':
    main()
