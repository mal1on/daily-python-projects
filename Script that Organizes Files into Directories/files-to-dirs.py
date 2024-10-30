import os
from glob import glob
from shutil import move


def sorter():
    '''
    Python script that organizes files in a directory into folders
    based on file type. For example, all .txt files go into a
    "Text Files" folder, all .jpg and .png files go into an "Images"
    folder, and so on.
    '''

    dir_to_organize = ''
    while not dir_to_organize:
        dir_to_organize = input('Please enter a directory path to organize: ')
        if not os.path.exists(dir_to_organize):
            dir_to_organize = ''
            print('Please enter existing directory')

    dirs_and_fts = {'docs': ['txt', 'rtf', 'docx'],
                    'imgs': ['jpg', 'png', 'gif']}

    file_types = ['txt', 'rtf', 'docx', 'jpg', 'png', 'gif']

    for d, fts in dirs_and_fts.items():
        fp = os.path.join(dir_to_organize, d)
        if not os.path.exists(fp):
            os.mkdir(fp)
        for files in [glob(os.path.join(dir_to_organize, '*.' + ft)) for ft in fts]:
            for file in files:
                file_name = os.path.basename(file)
                new_path = os.path.join(fp, file_name)
                if not os.path.isfile(new_path):
                    move(file, fp)
                else:
                    print(f'{file_name} already exists in {d}')

    others = [f for f in glob(os.path.join(
        dir_to_organize, '*.*')) if f != __file__ and f.split('.')[-1] not in file_types]

    others_dir = os.path.join(dir_to_organize, 'others')
    for file in others:
        if not os.path.exists(others_dir):
            os.mkdir(others_dir)
        file_name = os.path.basename(file)
        new_path = os.path.join(others_dir, file_name)
        if not os.path.exists(new_path):
            move(file, others_dir)
        else:
            print(f'{file_name} already exists in others')


if __name__ == "__main__":
    sorter()
