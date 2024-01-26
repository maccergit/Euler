#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Use NumPy and matrix multiply to generate triplets from Berggrens's tree.  See wikipedia "Tree of primitive Pythagorean triples"
'''

import numpy as np

arrayA = np.array([[1, -2, 2], [2, -1, 2], [2, -2, 3]])
arrayB = np.array([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
arrayC = np.array([[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]])

def findNextTriplet(current, limit):
    if np.sum(current) == limit:
        return current
    print(arrayA @ current)
    print(arrayB @ current)
    print(arrayC @ current)
    return current

def findFinalTriplet(limit):
    return np.prod(findNextTriplet(np.array([3, 4, 5]), limit))
    

def solution(limit):
    return findFinalTriplet(limit)

assert solution(12) == 60
print(solution(1000))

count = 100
scale = 1000

# import utils.timing
# utils.timing.table_timing([12, 1000], count, scale)
# utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale, "prob0009.04")