#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 6, 2024

@author: johnmcalister

Direct approach - but use Binet's formula to compute current number, rather than recursive definition.

Use gmpy2.mpfr type.  Note that PyDev will indicate a false error unless gmpy2 is added to "forced builtins" setting (see PyDev docs on "forced builtins").
Code will run, but redline is ugly until fixed.

As with Decimal, reducing precision does not have much impact, and can even reduce performance or cause asserts to fail.  Increasing precision hurts performance.
'''

import gmpy2

# compute constants only once
root5 = gmpy2.mpfr(5 ** 0.5)
phi = (1 + root5) / 2
upsilon = 1 - phi

# return the Nth Fibonacci number
def fib(index):
    return int(round((phi ** index - upsilon ** index) / root5))

assert fib(0) == 0
print(fib(1))
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
assert fib(7) == 13
assert fib(8) == 21
assert fib(9) == 34
assert fib(10) == 55
assert fib(11) == 89
assert fib(12) == 144

# return index of the largest Fibonacci number less than or equal to some limit
def fibLimit(limit):
    index = 0
    while fib(index) <= limit:
        index += 1
    return index - 1

assert fibLimit(10) == 6
assert fibLimit(20) == 7
assert fibLimit(30) == 8
assert fibLimit(100) == 11

def solution(limit):
    return fibLimit(10 ** (limit - 1)) + 1

assert solution(2) == 7
assert solution(3) == 12
assert solution(4) == 17
assert solution(5) == 21
assert solution(6) == 26
assert solution(7) == 31
assert solution(8) == 36
assert solution(9) == 40
assert solution(10) == 45
assert solution(20) == 93
assert solution(30) == 141
assert solution(40) == 189

print(solution(1000))

count = 10
scale = 1000

import utils.timing
utils.timing.table_timing([1000], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale)