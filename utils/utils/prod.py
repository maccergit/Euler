'''
Created on Feb 23, 2020

@author: johnmcalister

TODO - add unit tests
'''

import operator
from functools import reduce

# NOTE - from Python 3.8 on, use math.prod() instead
def prod(iterable):
    return reduce(operator.mul, iterable, 1)