import sys
import os 
from additional_funcs import *

def root_dir():
    '''
    this function defines root directory in system
    '''
    path = sys.executable
    while os.path.split(path)[1]:
        path = os.path.split(path)[0]
    return path

def change_folder(old_path, this_dir):
    '''
    it takes the old path and changes to the new path adding '/'
    '''
    # print('old_path = ', old_path, ' this_dir = ', this_dir)
    new_path = old_path + this_dir + '/'
    return new_path
    
def show_content(path):
    '''
    it takes path on input and changes to the next(deeper) level in file system
    '''
    this_path = os.listdir(path)
    print(path)
    content = []
    for folder in this_path:
        if not folder.startswith('.'):
            content.append(folder)
    content = sorted(content, key=str.casefold) # this key shows the same sort sa in the system
    print(content)
    return content

def directories(prev_adress, content):
    '''
    it shows only directories in the certain path
    '''
    folders = []
    for elem in content:
        if os.path.isdir(prev_adress + elem):
            folders.append(elem)
    print(folders)
    return folders

def iterator(prev_adress, folders_list):
    for folder in folders_list:
        print(show_content(prev_adress + folder))

root = show_content(root_dir())



dirs = directories(root_dir(),root)
iterator(root_dir(), dirs)
