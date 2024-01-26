#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Variant Euclid's formula of generating Pythagorean triplets, testing only Pythagorean triplets until one
with the correct perimeter is found.

for p and q, natural numbers that must both be odd, p > q > 0:

    a = pq
    b = (p² - q²) / 2
    c = (p² + q²) / 2

Difference from previous is both must be odd, so outer loop also skips every other integer.
'''

def solution(limit):
    for p in range(3, limit // 2 + 2, 2):
        for q in range(1, p + 2, 2):
            a = p * q
            b = (p * p - q * q) // 2
            c = (p * p + q * q) // 2
            if (a + b + c) == limit:
                return a * b * c
    return 0

assert solution(12) == 60
print(solution(1000))

count = 100
scale = 1000

import utils.timing
utils.timing.table_timing([12, 1000], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale, "prob0009.05")