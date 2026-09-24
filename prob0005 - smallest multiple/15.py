#!/usr/bin/python
# coding=utf-8

'''
Created on Sep 23, 2026

@author: johnmcalister
Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>

Hand the whole problem to gmpy2, the same way 05.py handed it to SymPy, 06.py to
NumPy, and 10.py to the standard library.

14.py ended by naming its own ceiling : CPython implements schoolbook and
Karatsuba multiplication and nothing beyond, so n^1.585 is the floor for this
problem in pure Python.  gmpy2 wraps GMP, which has Toom-Cook and FFT
multiplication as well, so there should be another order of magnitude available.

The obvious way to collect it is the one-liner.  gmpy2.lcm() is variadic, so the
entire problem is one call :

    gmpy2.lcm(*range(2, limit + 1))

This is the fairest possible test of "is a faster library the answer", because it
is exactly the approach 06.py and 10.py took, with the fastest bignum library
available underneath.  It is also, deliberately, the approach that ignores
everything sections 11 through 14 worked out.
'''

import gmpy2

def solution(limit):
    if limit < 2:
        return 1
    return gmpy2.lcm(*range(2, limit + 1))

if __name__ == "__main__":
    assert solution(10) == 2520
    print(solution(20))

    count = 10000
    scale = 1000000

    import utils.timing
    utils.timing.table_timing([10, 20], count, scale)
    utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], count, scale)

    # gmpy2 returns an mpz, so compare against int() to keep the assertion honest
    # about the value rather than the type.
    assert int(solution(43)) == 9419588158802421600
    assert int(solution(100)) == 69720375229712477164533808935312303556800
    print("done")
