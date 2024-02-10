#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 16, 2024

@author: johnmcalister

Use memoization to improve recursive approach
'''

memo = {}

# Return next Collatz number
def collatz(n):
    if n % 2 == 0:
        return(n // 2)
    else:
        return(3 * n + 1)

# Generate the sequence of Collatz numbers from a starting number
def collatz_gen(n):
    while n!= 1:
        yield(n)
        n = collatz(n)
    yield(n)

assert [x for x in collatz_gen(13)] == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

def collatz_length(n):
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = 1 + collatz_length(collatz(n))
    return(memo[n])

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
    memo = {}
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

count = 5
scale = 1000

import utils.timing
utils.timing.table_timing([13, 1000000], count, scale)
utils.timing.plot_timing([100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000], count, scale)