#!/usr/bin/python
# coding=utf-8

'''
Created on May 3, 2026

@author: johnmcalister
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>

Optimize the matrix exponentiation from 10.py by observing that Q^n is symmetric
(its top-right and bottom-left entries are both F(n)), so the matrix has only
two independent values.  Track (F(n), F(n+1)) directly using the Fibonacci
doubling identities :

    F(2k)   = F(k) * (2 * F(k+1) - F(k))
    F(2k+1) = F(k)^2 + F(k+1)^2

This replaces 8 multiplies + 4 adds + tuple allocation per matrix multiply with
3 multiplies + ~3 adds per step, no tuple allocation.  Same O(log n) scaling,
much smaller constant factor.  Still pure integer arithmetic - exact at any limit.
'''

import math

def fib(n):
    # Iterate bits of n high-to-low, carrying (a, b) = (F(m), F(m+1)) where
    # m is the integer formed by the bits seen so far.  Each bit doubles m and
    # then optionally increments it by 1.
    a, b = 0, 1
    for bit in bin(n)[2:]:
        c = a * (2 * b - a)     # F(2m)
        d = a * a + b * b       # F(2m+1)
        if bit == '1':
            a, b = d, c + d     # (F(2m+1), F(2m+2))
        else:
            a, b = c, d         # (F(2m),   F(2m+1))
    return a

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
