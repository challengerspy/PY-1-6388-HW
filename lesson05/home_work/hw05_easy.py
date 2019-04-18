# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

# 1 скрипт создание папки
for x in range(1,10):
    os.mkdir(f'dir_{x}')

# 2 скрипт
for x in range(1,10):
    os.rmdir(f'dir_{x}')

def create_dir(direct):
    print('Создание директории ')
    direct = input('Укажите название директории ')
    os.mkdir(direct)

def delete_dir(direct):
    print('Удаление директории ')
    direct = input('Укажите название директории ')
    os.rmdir(direct)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def print_path(direct):
    print(os.listdir(os.getcwd()))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os,shutil

def diplicate_file(filename):
    if os.path.isfile(filename):
        newfile=filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print('Файл ', newfile, ' был успешно создан')
            return True
        else:
            print('Возникли проблемы копирования')
            return False
diplicate_file('hw05_easy.py')
