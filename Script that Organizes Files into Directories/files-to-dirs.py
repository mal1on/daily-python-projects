from glob import glob
from os import mkdir


def sorter():
    '''Python script that organizes files in a directory into folders
    based on file type. For example, all .txt files go into a
    "Text Files" folder, all .jpg and .png files go into an "Images"
    folder, and so on.'''

    dirs_and_fts = {'docs': ['txt', 'rtf', 'docx'],
                    'imgs': ['jpg', 'png', 'gif']}
    dirs = {k: [] for k in dirs_and_fts}

    for d, fts in dirs_and_fts.items():
        for l in [glob('*.' + ft) for ft in fts]:
            dirs[d].extend(l)
            try:
                mkdir(d)
            except FileExistsError:
                pass




sorter()
