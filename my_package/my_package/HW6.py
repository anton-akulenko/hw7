import os
import sys
import shutil

from pathlib import Path

path = None
try:
    path = sys.argv[1]
except IndexError:
    print('No parameter')

workfolder = Path(path) #Path(r"D:\test_folder_for_sorting")  # path to the dir

CATEGORIES = {
    'video': ['.mp4', '.mov', '.avi', '.mpeg', '.vob'],
    'audio': ['.mp3', '.wav'],
    'images': ['.jpg', '.png', '.bmp'],
    'archives': ['.zip', '.7z'],
    'documents': ['.pdf', '.txt', '.doc', '.docx', '.xls'],
    'other': ['.exe']
}


def normalize(file_name) -> str:
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ/@^|"
    TRANSLATION = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
        "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", '_', "_", "_", "_")
    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    return file_name.translate(TRANS)


def create_folders(workfolder):
    for i in CATEGORIES.keys():
        if not workfolder.joinpath(i).exists():
            workfolder.joinpath(i).mkdir(parents=True, exist_ok=True)


def sort_files(workfolder):
    ext = list(CATEGORIES.items())

    for item in workfolder.glob('**/*'):
        if item.is_file():  # для файла .is_file() и т.д
            for ext_sort in range(len(ext)):
                for extension in ext[ext_sort][1]:

                    if item.suffix in extension:
                        f = Path(item)
                        new_name = f"{normalize(item.stem)}{item.suffix}"
                        new_dir = workfolder / ext[ext_sort][0]
                        try:
                            shutil.move(f, new_dir.joinpath(new_name))
                            print(f'Moving {item.name} in {ext[ext_sort][0]} folder')
                        except:
                            print("skipped")
                    else:
                        new_dir = workfolder / ext[5][0]
                        try:
                            shutil.move(item, new_dir.joinpath(item.name))
                        except:
                            continue



def del_empty_folder(path):
    if not os.path.isdir(path):
        return
    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                del_empty_folder(fullpath)

    files = os.listdir(path)
    if len(files) == 0:
        os.rmdir(path)

def unpack():
    arch_dir = workfolder / "archives"
    for entry in arch_dir.iterdir():
        unpack_dir = arch_dir / entry.name.split('.')[0]
        shutil.unpack_archive(entry, unpack_dir)


if __name__ == "__main__":
    create_folders(workfolder)
    sort_files(workfolder)
    del_empty_folder(workfolder)
    unpack()

def main(path):
    create_folders(workfolder)
    sort_files(workfolder)
    del_empty_folder(workfolder)
    unpack()