#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Use SymPy to compute Fibonacci numbers, skipping odd ones
'''

from sympy import fibonacci

def fib_even(limit):
    n = 3
    f = fibonacci(3)
    while f < limit:
        yield f
        n += 3
        f = fibonacci(n)

def solution(limit):
    return sum(x for x in fib_even(limit))

assert solution(100) == 44
print(solution(4000000))

count = 10000
scale = 1000000

import utils.timing
utils.timing.table_timing([100, 4000000], count, scale)
utils.timing.plot_timing([10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000], count, scale, "prob0002.05")