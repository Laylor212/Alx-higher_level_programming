#!/usr/bin/python3
# 3-is_kind_of_class.py
'''Defines a class and inherited class-checking function'''


def is_kind_of_class(obj, a_class):
    '''A function that checks if an object is an instance or inherited 
    instance of a class.
    '''
    if isinstance(obj, a_class):
        return True
    return False
