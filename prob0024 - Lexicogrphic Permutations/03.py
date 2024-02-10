#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 6, 2024

@author: johnmcalister

Use itertools to produce all permutations
'''

import itertools

testData = "012"
probData = "0123456789"

def permutations(s):
    return ["".join(x) for x in itertools.permutations(s)]

assert permutations("0") == ["0"]
assert permutations("1") == ["1"]
assert permutations("01") == ["01", "10"]
assert permutations("012") == ["012", "021", "102", "120", "201", "210"]

def solution(limit):
    return permutations(data)[limit - 1]

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
utils.timing.plot_timing([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000], count, scale, "prob0023.03")