#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 6, 2024

@author: johnmcalister

Don't generate all permutations - calculate the Nth permutation directly
'''

testData = "012"
probData = "0123456789"

def factoradic(n):
    return 0

def solution(limit):
    return ""

data = testData

assert solution(1) == "012"
assert solution(2) == "021"
assert solution(3) == "102"
assert solution(4) == "120"
assert solution(5) == "201"
assert solution(6) == "210"

data = probData

print(solution(1000000))

count = 3
scale = 1

import utils.timing
utils.timing.table_timing([1000000], count, scale)
utils.timing.plot_timing([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000], count, scale, "prob0022.01")