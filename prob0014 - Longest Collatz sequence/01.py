#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 16, 2024

@author: johnmcalister

Brute force

TODO - start optimizing :
- memoize already computed values
- take advantage of fact that even values are (1 + a memoized) value (although if memoization is being done, this may not provide any gain)
- can working in reverse help?  Starr with 1, then can be derived only from 2 (cuz odds add 1).  From 2, prev has to be 4 (cuz odds multiple by 3).  From 4, prev could be 8 or 1 - but 1 is
the exit condition.  From 8, prev must be 16, cuz (8 - 1) not divisible by 3.  From 16, next could be 32 or 5.  Not sure if this is useful.
- look for other tips from the problem overview.
'''

# Generator to build Collatz sequence from a starting number
def collatz(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield n

assert [x for x in collatz(13)] == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

def collatz_length(n):
    return len([x for x in collatz(n)])

assert collatz_length(1) == 1
assert collatz_length(2) == 2
assert collatz_length(3) == 8
assert collatz_length(4) == 3
assert collatz_length(5) == 6
assert collatz_length(6) == 9
assert collatz_length(7) == 17
assert collatz_length(8) == 4
assert collatz_length(9) == 20
assert collatz_length(10) == 7
assert collatz_length(11) == 15
assert collatz_length(12) == 10
assert collatz_length(13) == 10

def solution(limit):
    max_length = 0
    current = 0
    for n in range(1, limit + 1):
        length = collatz_length(n)
        if length > max_length:
            current = n
            max_length = length
    return current

assert solution(13) == 9
print(solution(1000000))

count = 1
scale = 1

import utils.timing
utils.timing.table_timing([13, 1000000], count, scale)
utils.timing.plot_timing([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], count, scale)