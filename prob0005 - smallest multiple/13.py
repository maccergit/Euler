#!/usr/bin/python
# coding=utf-8

'''
Created on Sep 23, 2026

@author: johnmcalister
Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>

Same prime-power formula again, with the sieve handed to the primesieve C
library instead of being written by hand.

12.py made the sieve 12-25x faster with NumPy and gained almost nothing
overall, because by a limit of a million the sieve is only 2% of the runtime.
This pushes that to its logical end : primesieve is a segmented wheel sieve
tuned for cache behaviour - the same library used in 03.py - and it returns the
primes directly, so the sieve stops being a meaningful cost at all.  If making
the sieve nearly free still does not help, the sieve was never the problem, and
we can stop looking at it.

One incidental benefit over 12.py : primesieve.primes() hands back an
array('Q', ...), and indexing an array.array yields a real Python int rather
than an np.int64.  So the overflow trap that 12.py needed an explicit int()
cast to avoid does not exist here - the arbitrary-precision product is arbitrary
precision by default.
'''

import primesieve

def solution(limit):
    if limit < 2:
        return 1

    result = 1
    for p in primesieve.primes(limit):
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

    # Same checks as 11.py and 12.py - 43 is where 06.py first wraps around in
    # int64, and where 12.py would have without its int() cast.
    assert solution(43) == 9419588158802421600
    assert solution(100) == 69720375229712477164533808935312303556800
    print("done")
