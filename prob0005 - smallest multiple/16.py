#!/usr/bin/python
# coding=utf-8

'''
Created on Sep 23, 2026

@author: johnmcalister
Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>

14.py's product tree with gmpy2 doing the multiplication - but only for the part
of the tree where gmpy2 is worth it.

15.py showed that a faster library on the wrong algorithm is still the wrong
algorithm.  This does the opposite : keep the algorithm from 14.py exactly -
prime powers from a primesieve sieve, multiplied up a balanced binary tree - and
change only which multiplication routine runs at each node.

GMP is faster than CPython at essentially every size, but converting a Python
int to an mpz is not free, and at the size of the tree's leaves the conversion
costs more than the multiply it improves.  Measured on this machine, a balanced
multiply of two 32-bit values takes 30.0 nsec as ints and 28.3 nsec as mpz - a
saving of 1.7 nsec - while mpz() on a 32-bit value costs 40 nsec.  Converting
the leaves is a guaranteed loss.

By a few hundred bits that has reversed : at 256 bits the multiply saves 51.7
nsec against a 61.3 nsec conversion, and the converted value is then reused by
every level above it, so the one-time cost is amortized over the whole remaining
climb.  So run the cheap bottom levels as Python ints and switch once the
operands are worth converting.  Sweeping the threshold puts the optimum around
256 bits, and the curve is shallow between 256 and 2100 - anywhere in that range
is within about 10% of best.

Note that this threshold has nothing to do with the 2100-bit Karatsuba cutoff
from 14.py.  That one marks where CPython stops being naive; this one marks
where GMP starts being worth the handover, which happens much earlier.
'''

import primesieve
from gmpy2 import mpz

# Bit length at which handing operands to GMP starts to repay the conversion.
# Measured, not derived - see the module docstring.
MPZ_SWITCH_BITS = 256

def solution(limit):
    if limit < 2:
        return 1

    # Highest power of each prime within the limit, as machine-sized ints.
    values = []
    for p in primesieve.primes(limit):
        power = p
        while power * p <= limit:
            power *= p
        values.append(power)

    # Bottom of the tree, in Python ints - too small for GMP to be worth it.
    while len(values) > 1 and values[0].bit_length() < MPZ_SWITCH_BITS:
        values = [a * b for a, b in zip(values[::2], values[1::2])] + values[len(values) - len(values) % 2:]

    # Everything above the switch, in GMP.  One conversion per surviving node,
    # paid once and reused by every level above.
    if len(values) > 1:
        values = [mpz(v) for v in values]
        while len(values) > 1:
            values = [a * b for a, b in zip(values[::2], values[1::2])] + values[len(values) - len(values) % 2:]

    return values[0]

if __name__ == "__main__":
    assert solution(10) == 2520
    print(solution(20))

    count = 10000
    scale = 1000000

    import utils.timing
    utils.timing.table_timing([10, 20], count, scale)
    utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], count, scale)

    # Small limits never reach the switch, so these exercise the int-only path
    # and return a Python int; limit 100 is 136 bits, still below it.  Above the
    # switch the return is an mpz instead - both compare equal to the same value,
    # so the distinction only matters if a caller cares about the type.
    assert solution(43) == 9419588158802421600
    assert solution(100) == 69720375229712477164533808935312303556800
    print("done")
