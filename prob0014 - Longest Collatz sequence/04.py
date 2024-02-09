#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 16, 2024

@author: johnmcalister

Brute force - recursive definition with optimzation that odd numbers can skip a step
'''

# return next Collatz number in sequence
def collatz(n):
    if n % 2 == 0:
        return(n // 2)
    else:
        return(3 * n + 1)

assert [collatz(x) for x in [13, 40, 20, 10, 5, 16, 8, 4, 2]] == [40, 20, 10, 5, 16, 8, 4, 2, 1]

def collatz_length(n):
    if n == 1:
        return 1
    if n % 2 > 0:
        return collatz_length((3 * n + 1) // 2) + 2
    return collatz_length(collatz(n)) + 1

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
utils.timing.plot_timing([200000, 400000, 600000, 800000, 1000000], count, scale, "prob0014.04")