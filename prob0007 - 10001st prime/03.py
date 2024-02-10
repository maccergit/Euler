#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

pyprimeseive
'''

from pyprimesieve import primes_nth

def solution(limit):
    return primes_nth(limit)

assert solution(6) == 13
print(solution(10001))

count = 10000
scale = 1000000

import utils.timing
utils.timing.table_timing([6, 10001], count, scale)
utils.timing.plot_timing([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], count, scale)