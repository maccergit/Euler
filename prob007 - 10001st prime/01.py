#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister
'''

# SymPy

from sympy import prime

def solution(limit):
    return prime(limit)

assert solution(6) == 13
print solution(10001)

count = 1
scale = 1000000 # µsec

import util.timing
util.timing.table_timing([6, 10001], count, scale)
util.timing.plot_timing([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], count, scale)