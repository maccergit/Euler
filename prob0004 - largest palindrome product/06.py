#!/usr/bin/python
# coding=utf-8

'''
Palindrome construction with multiples-of-11 trial division.

Section 05 generated palindromes in descending order and trial-divided
each one to find a d-digit factorization.  This section keeps the same
generate-and-test structure but tightens the inner trial-division loop
using the 11-rule.

Every even-digit palindrome is divisible by 11.  11 is prime, so for a
factorization p = i * cofactor with both factors d-digit, at least one
of i or cofactor must be a multiple of 11.  Walking i over multiples of
11 only - rather than every integer - covers both cases (whichever side
the multiple-of-11 factor lands on).

The cutoff is different from section 05.  Section 05 used i >= ceil(sqrt(p))
because anything below sqrt(p) had already appeared as a cofactor of a
larger i.  That argument needs i to walk every integer.  Here, with i
restricted to multiples of 11, the multiple-of-11 factor might be the
smaller one - whose cofactor (a non-multiple of 11) we never test.  The
correct cutoff is i >= ceil(p / high) : below that, the cofactor exceeds
high and cannot be a valid d-digit factor.

Co-Authored-By: Claude Opus 4.7 (1M context)
'''

def solution(digits):
    high = 10 ** digits - 1
    low = 10 ** (digits - 1) if digits > 1 else 0
    for half in range(high, low - 1, -1):
        s = str(half)
        p = int(s + s[::-1])
        i_start = high - high % 11
        i_min = max(low, -(-p // high))  # ceil(p / high)
        for i in range(i_start, i_min - 1, -11):
            if p % i == 0:
                cofactor = p // i
                if cofactor <= high:
                    return p
    return 0

assert solution(2) == 9009
print(solution(3))

count = 5
scale = 1000 # msec

import utils.timing
utils.timing.table_timing([2, 3, 4, 5, 6], count, scale)
