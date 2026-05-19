#!/usr/bin/python
# coding=utf-8

'''
Inner-loop pruning.

Outer loop x walks from all-9s down to all-0s.  Inner loop y walks from x
down to all-0s (using ab = ba symmetry, the outer is always the larger).
Track the best palindrome seen.  As y descends, the product x*y descends
monotonically, so once x*y <= best we can break out of the inner loop -
no remaining y in this row can produce a larger palindrome.

Co-Authored-By: Claude Opus 4.7 (1M context)
'''

def is_palindrome(x):
    return str(x) == str(x)[::-1]

def solution(digits):
    high = int('9' * digits)
    low = 10 ** (digits - 1) if digits > 1 else 0
    best = 0
    for x in range(high, low - 1, -1):
        for y in range(x, low - 1, -1):
            p = x * y
            if p <= best:
                break
            if is_palindrome(p):
                best = p
    return best

assert solution(2) == 9009
print(solution(3))

count = 5
scale = 1000 # msec

import utils.timing
utils.timing.table_timing([2, 3, 4, 5, 6], count, scale)
utils.timing.plot_timing([2, 3, 4, 5, 6], count, scale)
