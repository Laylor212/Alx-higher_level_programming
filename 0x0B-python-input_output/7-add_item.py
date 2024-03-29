#!/usr/bin/python3
'''A script that adds all arguments to a Python list, and then save them 
to a file
'''

import sys
import os
from importlib import import_module as using

'''The functions for saving and loading lists'''
save_to_json_file, load_from_json_file = (
    using('5-save_to_json_file').save_to_json_file,
    using('6-load_from_json_file').load_from_json_file
)

'''The list of arguments'''
args_list = []

'''The file containing the list of arguments.'''
args_list_file_name = 'add_item.json'

def run():
    '''Function that runs the routines of the script'''
    
    if not os.path.exists(args_list_file_name):
        with open(args_list_file_name, mode='w', encoding='utf-8') as file:
            file.write('[]')
    json_list = load_from_json_file(args_list_file_name)
    if (type(json_list) is list) and all(type(s) is str for s in json_list):
        args_list.extend(json_list)
    args_list.extend(sys.argv[1:])
    save_to_json_file(args_list, args_list_file_name)

if __name__ == '__main__':
    run()
