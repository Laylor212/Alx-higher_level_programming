#!/usr/bin/python3
'''A class MyList that inherits from list'''

def is_same_class(obj, a_class):
	'''Returns True if the object is exactly an instance'''
	
    if type(obj) == a_class:
        return True
    return False
