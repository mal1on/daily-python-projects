'''
Program that takes a list of words and finds the most frequently
occurring one.
'''


from collections import Counter


words = ["love", "peace", "joy", "love", "happiness", "love", "joy"]


def main():
    '''Main function'''
    word, count = Counter(words).most_common(1)[0]
    print(f'The most frequent word is "{word}" appearing {count} times.')


if __name__ == '__main__':
    main()
