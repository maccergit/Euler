#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

pyprimesieve
'''

import pyprimesieve

def solution(limit):
    return pyprimesieve.primes_sum(limit)

assert solution(10) == 17
print(solution(2000000))

count = 1000
scale = 1000000

import utils.timing
utils.timing.table_timing([10, 2000000], count, scale)
utils.timing.plot_timing([500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000, 5000000], count, scale)