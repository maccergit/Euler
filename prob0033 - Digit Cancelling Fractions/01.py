#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 18, 2024

@author: johnmcalister

Direct approach
'''

import math

# find (ab)/(bc) = a/c : turns out there are no solutions for (ab)/(ca) == b/c
def getSolutions():
    results = []
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(a, 10):
                numerator = a * 10 + b
                denominator = b * 10 + c
                if numerator < denominator and numerator / denominator == a / c:
                    results.append((numerator, denominator, a, c))
    return results

assert len(getSolutions()) == 4
assert (49, 98, 4, 8) in getSolutions()

def solution(limit):
    solutions = getSolutions()
    numerator = 1
    denominator = 1
    for solution in solutions:
        numerator *= solution[2]
        denominator *= solution[3]
    gcd = math.gcd(numerator, denominator)
    return(denominator // gcd)

print(solution(0))

count = 1
scale = 1000000

import utils.timing
utils.timing.table_timing([0], count, scale)
# utils.timing.plot_timing([3, 4, 5, 6, 7, 8, 9], count, scale)
