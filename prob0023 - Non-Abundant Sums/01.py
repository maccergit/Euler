#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 6, 2024

@author: johnmcalister

Direct approach
'''

def solution(limit):
    return 0

# all numbers less than 24 are not sums of abundant numbers, as smallest abundant number is 12, and smallest sum of abundants is 24
for i in range(1, 24):
    assert solution(i) == sum(x for x in range(i + 1))

# 24 is first sum of abundants, and thus would not be included in the solution
assert solution(24) == sum(x for x in range(25)) - sum([24])

# next abundant number is 18, so next possible sum is 12 + 18 = 30
assert solution(30) == sum(x for x in range(31)) - sum([24, 30])

print(solution(28123))

count = 100
scale = 1000

# import utils.timing
# utils.timing.table_timing([0], count, scale)
# utils.timing.plot_timing([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], count, scale, "prob0022.01")