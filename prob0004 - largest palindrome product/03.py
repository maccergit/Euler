#!/usr/bin/python
# coding=utf-8

'''
Inner-loop and outer-loop pruning.

Section 02 added an inner-loop break : once x*y <= best, no remaining y
in this row can beat best.  The same idea applies one level out.  The
outer loop x descends, and the inner loop y is always <= x, so the
largest product still reachable from the current x onward is x*x.  Once
x*x <= best, no remaining (x, y) pair can beat best - we can break out
of the outer loop entirely.

In practice the win is incremental, not dramatic.  The rows being skipped
by the outer break are exactly the rows where the inner break would have
fired almost immediately anyway, so we are mostly saving outer-loop
bookkeeping rather than real work.

Co-Authored-By: Claude Opus 4.7 (1M context)
'''

def is_palindrome(x):
    return str(x) == str(x)[::-1]

def solution(digits):
    high = int('9' * digits)
    low = 10 ** (digits - 1) if digits > 1 else 0
    best = 0
    for x in range(high, low - 1, -1):
        if x * x <= best:
            break
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
