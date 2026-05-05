#!/usr/bin/python
# coding=utf-8

'''
Created on May 3, 2026

@author: johnmcalister
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>

Roll-our-own matrix exponentiation with numpy arrays and the @ operator,
default int64 dtype.  Same exp-by-squaring skeleton as 10.py - only the
multiply mechanism changes (numpy @ instead of hand-rolled tuple multiply).

int64 silently overflows once Fibonacci values exceed about 9.22 * 10^18
(F(92) and beyond), so this version is only correct at the problem's 4M
scale.  Larger limits return silently-wrong values - see the print statements
at the end of __main__ for a demonstration.
'''

import math
import numpy as np

Q = np.array([[1, 1], [1, 0]], dtype = np.int64)
I = np.eye(2, dtype = np.int64)

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

    # int64 silently overflows once Fibonacci entries exceed ~9.22 * 10^18.
    # Print rather than assert so the silent-wrap failure is visible.
    print("solution(10**17) =", solution(10**17), "  (correct: 49597426547377748)")
    print("solution(10**30) =", solution(10**30), "  (correct: 727244555616386341839153320976)")
    print("done")
