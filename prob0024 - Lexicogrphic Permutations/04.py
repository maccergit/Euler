#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 6, 2024

@author: johnmcalister

Don't generate all permutations - calculate the Nth permutation directly
'''

import math

testData = "012"
probData = "0123456789"

def factoradic(n):
    # find first factorial larger than N
    fact = 0
    place = -1
    while n >= fact:
        place += 1
        fact = math.factorial(place)
    place -= 1
    
    digits = []
    while place > 0:
        fact = math.factorial(place)
        digits.append(n // fact)
        n %= fact
        place -= 1
    return digits

def testFactoradic(n, expected):
    assert factoradic(n) == expected

testFactoradic(0, [])
testFactoradic(1, [1])
testFactoradic(2, [1, 0])
testFactoradic(3, [1, 1])
testFactoradic(4, [2, 0])
testFactoradic(5, [2, 1])
testFactoradic(6, [1, 0, 0])
testFactoradic(7, [1, 0, 1])
testFactoradic(21, [3, 1, 1])
testFactoradic(22, [3, 2, 0])
testFactoradic(23, [3, 2, 1])
testFactoradic(24, [1, 0, 0, 0])
testFactoradic(25, [1, 0, 0, 1])
testFactoradic(5038, [6, 5, 4, 3, 2, 0])
testFactoradic(5039, [6, 5, 4, 3, 2, 1])
testFactoradic(5040, [1, 0, 0, 0, 0, 0, 0])
testFactoradic(999998, [2, 6, 6, 2, 5, 1, 2, 1, 0])
testFactoradic(999999, [2, 6, 6, 2, 5, 1, 2, 1, 1])
testFactoradic(1000000, [2, 6, 6, 2, 5, 1, 2, 2, 0])
testFactoradic(1000001, [2, 6, 6, 2, 5, 1, 2, 2, 1])

def permutation(elems, limit):
    f = factoradic(limit)
    # need to pad leading 0's and include final trailing 0 to handle all elements
    maxlen = len(factoradic(math.factorial(len(elems)) - 1))
    f = (maxlen - len(f)) * [0] + f + [0]
    result = []
    for findex in f:
        result.append(elems[findex])
        elems = elems[:findex] + elems[findex + 1:]
    return "".join(result)

def solution(limit):
    return permutation(data, limit - 1)

data = testData

assert solution(1) == "012"
assert solution(2) == "021"
assert solution(3) == "102"
assert solution(4) == "120"
assert solution(5) == "201"
assert solution(6) == "210"

data = probData

print(solution(1000000))

count = 10000
scale = 1000000

import utils.timing
utils.timing.table_timing([1000000], count, scale)
utils.timing.plot_timing([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000], count, scale, "prob0023.04")