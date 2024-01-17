'''
Created on Feb 23, 2020

@author: johnmcalister

TODO - add unit tests
'''

def gen_factors(limit):
    current = 2
    while current < limit:
        if limit % current != 0:
            current += 1
        else:
            yield current
            limit = limit // current
    yield limit