#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister
'''

# Brute force with coprimes

import utils.factor
import math

def triangle(n):
    return (n + 1) * n / 2

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
    factors = {}
    x = [y for y in utils.factor.gen_factors(n)]
    for y in {z for z in x}:
        factor_count = x.count(y)
        if y not in factors or factor_count > factors[y]:
            factors[y] = factor_count
    return math.prod(factors[factor] + 1 for factor in factors)

def triangle_divisors(n):
    if n % 2 == 0:
        return num_divisors(n / 2) * num_divisors(n + 1)
    return num_divisors(n) * num_divisors((n + 1) / 2)

def solution(limit):
    current = 1
    while triangle_divisors(current) <= limit:
        current += 1
    return triangle(current)

assert solution(5) == 28
print(solution(500))

count = 2
scale = 1 # sec

import utils.timing
utils.timing.table_timing([10, 500], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500], count, scale)