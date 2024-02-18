#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 18, 2024

@author: johnmcalister

Direct approach
'''

import itertools

def pandigital(limit):
    retval = set()
    perms = itertools.permutations([*range(1, limit + 1)])
    for perm in perms:
        permString = "".join(str(x) for x in perm)
        for div1 in range(1, (len(permString) - 1) // 2 + 1):
            first = int(permString[:div1])
            for div2 in range(div1 + 1, div1 + (len(permString) - div1) // 2 + 1):
                second = int(permString[div1:div2])
                third = int(permString[div2:])
                if (first * second == third):
                    retval |= {third}
    return retval

assert pandigital(4) == {12}
assert pandigital(5) == {52}
assert pandigital(6) == {162}

def solution(limit):
    return sum(pandigital(limit))

assert solution(4) == 12
assert solution(5) == 52
assert solution(6) == 162
print(solution(9))

count = 1
scale = 1

import utils.timing
utils.timing.table_timing([9], count, scale)
utils.timing.plot_timing([3, 4, 5, 6, 7, 8, 9], count, scale)
