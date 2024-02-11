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

def solution(limit):
    return 0

assert solution(1) == 0
assert solution(2) == 0
assert solution(3) == 0
assert solution(4) == 0
assert solution(5) == 0
assert solution(6) == 0
assert solution(7) == 0
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

# count = 1
# scale = 1

# import utils.timing
# utils.timing.table_timing([1000], count, scale)
# utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale)