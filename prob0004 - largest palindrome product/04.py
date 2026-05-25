#!/usr/bin/python
# coding=utf-8

'''
Pruning + multiples-of-11 inner loop.

Every even-digit palindrome is divisible by 11 (and the answer for our
problem is always an even-digit palindrome).  11 is prime, so for a
product x*y to be divisible by 11, at least one of x or y must be.
This gives three classes of palindromic products :
  (1) outer multiple of 11, inner not
  (2) inner multiple of 11, outer not
  (3) both multiples of 11

If we forced the outer to step by 11, we'd cover classes 1 and 3 but
miss class 2.  The fix is to keep the outer step at -1 and adapt the
inner step based on whether the outer is already a multiple of 11 :
  - outer divisible by 11 : the 11-divisibility requirement is already
    satisfied; the inner is unconstrained, so step -1 (covers classes 1
    and 3 from this pass).
  - outer not divisible by 11 : the inner must be divisible by 11;
    step -11 starting from the largest multiple of 11 <= x (covers
    class 2 from this pass).

Symmetry (y <= x) is preserved in both branches, so the outer prune
from section 03 still applies.

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
        if x % 11 == 0:
            y_range = range(x, low - 1, -1)
        else:
            y_range = range(x - x % 11, low - 1, -11)
        for y in y_range:
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
