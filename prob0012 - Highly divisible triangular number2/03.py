#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister
'''

# pyprimesieve

import pyprimesieve
import math

def triangle(n):
    return (n + 1) * n // 2

assert triangle(1) == 1
assert triangle(2) == 3
assert triangle(3) == 6
assert triangle(4) == 10
assert triangle(5) == 15
assert triangle(6) == 21
assert triangle(7) == 28
assert triangle(8) == 36
assert triangle(9) == 45
assert triangle(10) == 55

def num_divisors(n):
    return math.prod(x[1] + 1 for x in pyprimesieve.factorize(n))

def solution(limit):
    current = 1
    while num_divisors(triangle(current)) <= limit:
        current += 1
    return triangle(current)

assert solution(5) == 28
print(solution(500))

count = 100
scale = 1000 # msec

import utils.timing
utils.timing.table_timing([10, 500], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500], count, scale)