#!/usr/bin/python3
'''A class MyList that inherits from list'''

class MyList(list):
    '''A class of a list'''
    def print_sorted(self):
        '''A function that prints a sorted ascending list'''
		print(sorted(self))
