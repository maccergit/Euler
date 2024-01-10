'''
Created on Feb 23, 2020

@author: johnmcalister

TODO - add unit tests
'''

import operator

def prod(iterable):
    return reduce(operator.mul, iterable, 1)