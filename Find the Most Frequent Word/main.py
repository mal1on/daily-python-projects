'''
Program that takes a list of words and finds the most frequently
occurring one.
'''


words = ["love", "peace", "joy", "love", "happiness", "love", "joy", "joy"]


def main():
    '''Main function'''
    word = max(words, key=lambda word: words.count(word))
    count = words.count(word)
    print(f'The most frequent word is "{word}" appearing {count} times.')


if __name__ == '__main__':
    main()
