#!/usr/bin/python
# coding=utf-8

'''
Created on Sep 23, 2026

@author: johnmcalister
Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>

Same prime-power formula as 11.py, with the sieve handed to NumPy.

11.py split the work in two : a sieve over small machine integers, then one
bignum multiply per prime.  The multiply half is inherently sequential - each
step needs the previous result - so there is nothing there for NumPy to
vectorize.  The sieve half is the opposite : crossing off the multiples of a
prime is a strided write over a flat array, which is exactly the shape NumPy is
built for.  One slice assignment replaces the inner Python loop :

    sieve[p * p :: p] = False

So this is the narrow case where NumPy genuinely helps on this problem - not on
the LCM itself, where 06.py went wrong, but on the cheap half that never needed
big integers in the first place.

The catch is that NumPy hands the primes back as int64, and int64 is what broke
06.py.  Multiplying a Python int by an np.int64 produces an np.int64, so the
running product would wrap around silently all over again - the overflow trap
follows the dtype, not the library call.  int(p) below is what keeps this
correct, and it is not optional.
'''

import math
import numpy as np

def solution(limit):
    if limit < 2:
        return 1

    # Sieve of Eratosthenes, vectorized.  Each pass is a single strided write
    # into the array rather than a Python loop over the multiples.
    sieve = np.ones(limit + 1, dtype = bool)
    sieve[0] = sieve[1] = False
    for i in range(2, math.isqrt(limit) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False

    # flatnonzero() returns the indices that are still True - the primes - in
    # one pass, instead of walking all "limit" indices in Python testing the
    # flag.  Worth ~20% on its own at moderate limits, since the composites are
    # never visited at all.
    result = 1
    for p in np.flatnonzero(sieve):
        # int(p) deliberately : p is an np.int64, and leaving it as one would
        # make the product below an int64 multiply that wraps past 2^63.
        p = int(p)
        power = p
        while power * p <= limit:
            power *= p
        result *= power

    return result

if __name__ == "__main__":
    assert solution(10) == 2520
    print(solution(20))

    count = 10000
    scale = 1000000

    import utils.timing
    utils.timing.table_timing([10, 20], count, scale)
    utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], count, scale)

    # Same checks as 11.py - 43 is where 06.py first wraps around in int64, and
    # is the limit that would catch the np.int64 product described above.
    assert solution(43) == 9419588158802421600
    assert solution(100) == 69720375229712477164533808935312303556800
    print("done")
