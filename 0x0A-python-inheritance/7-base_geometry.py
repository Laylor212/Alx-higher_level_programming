#!/usr/bin/python3
# 7-base_geometry.py
'''A class BaseGeometry (based on 6-base_geometry.py)'''

class BaseGeometry:
    '''A class BaseGeometry'''

    def area(self):
        '''A function that raises an Exception with the message area() is 
        not implemented
		'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''A function that validates values'''
		
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
