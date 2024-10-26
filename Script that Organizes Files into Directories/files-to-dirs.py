from glob import glob
from os import mkdir
from shutil import move


def sorter():
    '''Python script that organizes files in a directory into folders
    based on file type. For example, all .txt files go into a
    "Text Files" folder, all .jpg and .png files go into an "Images"
    folder, and so on.'''

    dirs_and_fts = {'docs': ['txt', 'rtf', 'docx'],
                    'imgs': ['jpg', 'png', 'gif']}

    for d, fts in dirs_and_fts.items():
        for files in [glob('*.' + ft) for ft in fts]:
            try:
                mkdir(d)
            except FileExistsError:
                pass
            for file in files:
                move(file, d)


if __name__ == "__main__":
    sorter()
