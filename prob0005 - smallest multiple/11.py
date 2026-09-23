#!/usr/bin/python
# coding=utf-8

'''
Created on Sep 22, 2026

@author: johnmcalister
Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>

Build the LCM directly from prime powers instead of accumulating it pairwise.

Every approach from 04.py onward walks the range 2..limit doing one operation
per value, on a running result that keeps growing - so the cost is dominated by
bignum arithmetic on a number with O(limit) bits.  But the answer only needs
each prime to appear once, at its highest power in range :

    LCM(1..limit) = product of p^k for each prime p <= limit,
                    where p^k is the largest power of p that is <= limit

For limit = 10 that is 2^3 * 3^2 * 5 * 7 = 2520 - eight values collapse to four
multiplies.  The multiply count drops from "limit" to pi(limit), the number of
primes below the limit, which thins out as the limit grows.

The sieve is O(n log log n) on small machine integers, and the expensive bignum
work is now proportional to pi(limit) rather than limit.
'''

import math

def solution(limit):
    if limit < 2:
        return 1

    # Sieve of Eratosthenes.  math.isqrt() rather than int(limit ** 0.5) - the
    # float version starts misreporting the root for limits past 2^53.
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime[i]:
            # Start at i*i - anything smaller has a smaller prime factor and so
            # was already marked by an earlier pass.
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # Walk the primes, raising each to the highest power still within the limit.
    # Stopping any lower would leave a multiple of that power undivided : 2^3
    # divides 8 but not 16, so a limit of 16 needs the full 2^4.
    result = 1
    for p in range(2, limit + 1):
        if is_prime[p]:
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

    # Limits where 06.py silently wraps around in int64 - 43 is the first, and
    # is where the NumPy version first reports a negative result.
    assert solution(43) == 9419588158802421600
    assert solution(100) == 69720375229712477164533808935312303556800
    print("done")
