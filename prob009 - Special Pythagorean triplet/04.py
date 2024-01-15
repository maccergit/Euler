#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Use Euclid's formula of generating Pythagorean triplets, testing only Pythagorean triplets until
we hit the one that has the correct perimeter.

for p and q, natural numbers that cannot both be odd:

    a = 2pq
    b = p² - q²
    c = p² + q²
'''

def solution(limit):
    for p in range(1, int(limit / 4) + 2):
        for q in range(p % 2 + 1, int(limit / 4) + 2, 2):
            a = 2 * p * q
            b = p * p - q * q
            if b < 0:
                b = -b
            c = p * p + q * q
            if (a + b + c) == limit:
                return a * b * c
    return 0

assert solution(12) == 60
print(solution(1000))

count = 1000
scale = 1000000

import utils.timing
utils.timing.table_timing([12, 1000], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale, "prob0009.04")