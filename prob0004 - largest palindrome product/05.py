#!/usr/bin/python
# coding=utf-8

'''
Palindrome construction.

Sections 02-04 searched the product space of two d-digit numbers,
with progressively smarter pruning.  This is a different approach :
generate even-digit palindromes in descending order and factor each
one until we find a valid d-digit factorization.

A 2d-digit palindrome is fully determined by its first half (d digits).
There are 9 * 10^(d-1) such palindromes - linear in the per-factor range,
not quadratic.  For d = 3 that is 900 palindromes vs. ~405000 product
pairs in section 04 (with symmetry).

For each palindrome p in descending order, trial-divide by i from
high = 10^d - 1 down to ceil(sqrt(p)).  If i divides p and the cofactor
p // i lands in [10^(d-1), 10^d - 1], we have a valid factorization.
The first palindrome with such a factorization is the answer - no
running `best` needed, since we generate in descending order.

Co-Authored-By: Claude Opus 4.7 (1M context)
'''

from math import isqrt

def solution(digits):
    high = 10 ** digits - 1
    low = 10 ** (digits - 1) if digits > 1 else 0
    for half in range(high, low - 1, -1):
        s = str(half)
        p = int(s + s[::-1])
        # Trial-divide from high down to ceil(sqrt(p)), looking for a
        # d-digit divisor whose cofactor is also d-digit.
        i_min = isqrt(p)
        if i_min * i_min < p:
            i_min += 1
        if i_min < low:
            i_min = low
        for i in range(high, i_min - 1, -1):
            if p % i == 0:
                cofactor = p // i
                if low <= cofactor <= high:
                    return p
                # Cofactor too small - any smaller i gives larger
                # cofactor, so keep looking.  Cofactor too large is
                # impossible because i >= sqrt(p) means cofactor <= sqrt(p) <= i.
    return 0

assert solution(2) == 9009
print(solution(3))

count = 5
scale = 1000 # msec

import utils.timing
utils.timing.table_timing([2, 3, 4, 5, 6], count, scale)
