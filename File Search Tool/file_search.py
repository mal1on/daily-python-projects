import os
from glob import glob


def search():
    '''
    Python script that searches for files in a specified directory
    based on a search term. The search tool allows the user to look for
    files by name or extension and display matching results with their
    full file paths.
    '''
    path = ''
    while not path:
        path = input('Please enter directory path to search: ')
        if not os.path.isdir(path):
            path = ''
            print('Please enter existing directory')

    term = ''
    while not term:
        term = input('Please enter the search term or file extension: ')

    result = glob(os.path.join(path, '*' + term + '*'))

    if result:
        print('Files matching your search: ')
        [print(file) for file in result]
    else:
        print('No files matching your search')


if __name__ == '__main__':
    search()
