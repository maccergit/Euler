#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 6, 2024

@author: johnmcalister

Direct approach - note that the examples can be rewritten as : 

1/0  = 0.(0)
1/1  = 1.(0) = 0.(9)
1/2  = 0.5(0) = 0.4(9)
1/3  = 0.(3)
1/4  = 0.25(0) = 0.24(9)
1/5  = 0.2(0) = 0.1(9)
1/6  = 0.1(6)
1/7  = 0.(142857)
1/8  = 0.125(0) = 0.124(9)
1/9  = 0.(1)
1/10 = 0.1(0) = 0.0(9)

so every rational has an infinite repeat.  In case of duplicate lengths, we will use the first one we find.
'''

# return the repetend of the reciprocal of a provided number
def repetendLen(x):
    dividend = 1
    digits = []
    remainders = []
    while dividend not in remainders:
        remainders.append(dividend)
        while dividend > 0 and dividend < x:
            digits.append(0)
            dividend *= 10
        digits.append(dividend // x)
        dividend %= x
    index = 0
    while digits[index] == 0:
        index += 1
    return len(remainders) - remainders.index(dividend)

assert repetendLen(1) == 1
assert repetendLen(2) == 1
assert repetendLen(3) == 1
assert repetendLen(4) == 1
assert repetendLen(5) == 1
assert repetendLen(6) == 1
assert repetendLen(7) == 6
assert repetendLen(8) == 1
assert repetendLen(9) == 1
assert repetendLen(10) == 1

def solution(limit):
    repetendLens = [repetendLen(x) for x in range(1, limit)]
    return repetendLens.index(max(repetendLens)) + 1

assert solution(2) == 1
assert solution(3) == 1
assert solution(4) == 1
assert solution(5) == 1
assert solution(6) == 1
assert solution(7) == 1
assert solution(8) == 7
assert solution(9) == 7
assert solution(10) == 7
assert solution(11) == 7
# the ones below come from wikipedia article "repeated decimals"
assert solution(18) == 17
assert solution(20) == 19
assert solution(25) == 23
assert solution(30) == 29
assert solution(50) -- 47

print(solution(1000))

count = 3
scale = 1000

import utils.timing
utils.timing.table_timing([1000], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale)
