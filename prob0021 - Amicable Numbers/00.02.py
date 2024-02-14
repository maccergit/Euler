#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 13, 2024

@author: johnmcalister

run timing tests on trial division, returning 2 divisors per hit, and stopping at sqrt(n)
'''

def gen_divisors(limit):
    current = 1
    while (current * current) < (limit + 1):
        if limit % current == 0:
            yield current
            if current != limit // current:
                yield limit // current
        current += 1

def solution(limit):
    return [*gen_divisors(limit)]

print(solution(10000))

count = 1000
scale = 1000000

import utils.timing
utils.timing.table_timing([1000, 10000], count, scale)
utils.timing.plot_timing([1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000], count, scale)