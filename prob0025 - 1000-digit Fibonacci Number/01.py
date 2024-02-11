#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 6, 2024

@author: johnmcalister

Direct approach
'''

def fib_gen(limit):
    f0 = 0
    fnext = 1
    while fnext <= limit:
        yield fnext
        f0, fnext = fnext, fnext + f0

def solution(limit):
    return len([*fib_gen(10 ** (limit - 1))]) + 1

assert solution(2) == 7
assert solution(3) == 12
assert solution(4) == 17
assert solution(5) == 21
assert solution(6) == 26
assert solution(7) == 31
assert solution(8) == 36
assert solution(9) == 40
assert solution(10) == 45
assert solution(20) == 93
assert solution(30) == 141
assert solution(40) == 189

print(solution(1000))

count = 100
scale = 1000000

import utils.timing
utils.timing.table_timing([1000], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale)