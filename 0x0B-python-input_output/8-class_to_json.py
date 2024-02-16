#!/usr/bin/python3
'''A function that returns the dictionary description of an object'''

def class_to_json(obj):
    '''A function that returns the dictionary description of an object.'''
    
    if '__dict__' in dir(obj):
        return obj.__dict__
