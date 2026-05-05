#!/usr/bin/python
# coding=utf-8

'''
Created on May 3, 2026

@author: johnmcalister
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>

Let numpy do the exp-by-squaring for us via np.linalg.matrix_power, default
int64 dtype.  Shorter code, and the squaring loop runs in C instead of Python.

Still has the same int64 silent-overflow problem as 12a - the numpy library
call does not detect or handle overflow.
'''

import math
import numpy as np

Q = np.array([[1, 1], [1, 0]], dtype = np.int64)

def fib(n):
    return int(np.linalg.matrix_power(Q, n)[0, 1])

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

    # Same int64 silent-overflow problem as 12a - demonstrate rather than assert.
    print("solution(10**17) =", solution(10**17), "  (correct: 49597426547377748)")
    print("solution(10**30) =", solution(10**30), "  (correct: 727244555616386341839153320976)")
    print("done")
