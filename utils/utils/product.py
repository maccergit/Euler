# coding: utf8
"""
Compute the ∏ product of a passed in iterable.
"""

import operator

def product(data):
    return reduce(operator.mul, data)