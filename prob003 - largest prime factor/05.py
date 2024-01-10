#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister
'''

# pyprimesieve - factorize

from pyprimesieve import factorize

def solution(limit):
    return max(x[0] for x in factorize(limit))

assert solution(13195) == 29
print(solution(600851475143))

count = 1000000
scale = 1000000 # µsec

import utils.timing
utils.timing.table_timing([101, 4000001], count, scale)
utils.timing.plot_timing([10000001, 20000003, 30000001, 40000001, 50000003, 60000001, 70000001, 80000003, 90000001, 100000001], count, scale)