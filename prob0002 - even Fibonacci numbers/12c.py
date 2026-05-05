#!/usr/bin/python
# coding=utf-8

'''
Created on May 3, 2026

@author: johnmcalister
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>

Same roll-our-own structure as 12a, but with dtype=object so the array cells
hold Python int objects instead of fixed-width int64.  This dodges the silent
overflow at the cost of throwing away every reason to use numpy - each multiply
now dispatches back into Python for per-element arithmetic on boxed int objects.

Correct at any limit, but slower than both 10 (pure Python tuples) and 11 (fast
doubling).
'''

import math
import numpy as np

Q = np.array([[1, 1], [1, 0]], dtype = object)
I = np.array([[1, 0], [0, 1]], dtype = object)

def mat_pow(M, n):
    result = I
    base = M
    while n > 0:
        if n & 1:
            result = result @ base
        n >>= 1
        if n > 0:
            base = base @ base
    return result

def fib(n):
    return int(mat_pow(Q, n)[0, 1])

def solution(limit):
    phi = (1 + 5 ** 0.5) / 2
    exp = 3 * int((math.log(limit) + math.log(5) / 2.0) / math.log(phi) / 3) + 2
    return (fib(exp) - 1) // 2

if __name__ == "__main__":
    assert solution(100) == 44
    print(solution(4000000))

    count = 100000
    scale = 1000000

    import utils.timing
    utils.timing.table_timing([100, 4000000], count, scale)
    utils.timing.plot_timing([10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000], count, scale)

    assert solution(10**17) == 49597426547377748
    assert solution(10**30) == 727244555616386341839153320976
    assert solution(10**100) == 12065007678944807420403981310014175239608005638595098371630805388439212255831420630608529497465143520
    print("done")
