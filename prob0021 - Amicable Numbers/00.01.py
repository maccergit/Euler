#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 13, 2024

@author: johnmcalister

run timing tests on factor.gen_divisors
'''

def divisors(n):
    return ([x for x in range(1, n // 2 + 1) if n % x == 0])

def solution(limit):
    return divisors(limit)

print(solution(10000))

count = 2
scale = 1000

import utils.timing
utils.timing.table_timing([1000, 10000], count, scale)
utils.timing.plot_timing([1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000], count, scale)