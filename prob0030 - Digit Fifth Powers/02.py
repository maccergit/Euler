#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 13, 2024

@author: johnmcalister

- iterate over possible digits, compute power sum, and see if result matches number built from those digits (each set of digits can produce several numbers as digits are rearranged).
'''

import itertools

def getUpperLimit(limit):
    digits = 2
    while (digits * 9 ** limit) > int("9" * digits):
        digits += 1
    return digits

def powerSums(limit):
    retval = set()
    for digits in range(2, getUpperLimit(limit) + 1):
        candidates = {*itertools.combinations_with_replacement(range(10), digits)}
        candidates_map = {candidate : sum(x ** limit for x in candidate) for candidate in candidates if len(str(sum(x ** limit for x in candidate))) > 1}
        for x in candidates_map:
            for y in {*itertools.permutations(x)}:
                trial = int("".join(str(z) for z in y))
                if candidates_map[x] == trial:
                    retval.add(trial)
    return retval

assert powerSums(4) == {1634, 8208, 9474}

def solution(limit):
    return sum(powerSums(limit))

assert solution(4) == 19316

print(solution(5))

count = 1
scale = 1

import utils.timing
utils.timing.table_timing([4, 5], count, scale)
utils.timing.plot_timing([2, 3, 4, 5, 6], count, scale)
