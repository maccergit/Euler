#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 1, 2024

@author: johnmcalister

Direct approach
'''

def divisors(n):
    return ([x for x in range(1, n // 2 + 1) if n % x == 0])

assert divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
assert divisors(284) == [1, 2, 4, 71, 142]

def isAmicable(x):
    divSum = sum(divisors(x))
    return x == sum(divisors(divSum)) and x != divSum

assert isAmicable(220)
assert isAmicable(284)

def solution(limit):
    return sum(x for x in range(limit) if isAmicable(x))

print(solution(10000))

count = 1
scale = 1

import utils.timing
utils.timing.table_timing([1000, 10000], count, scale)
utils.timing.plot_timing([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], count, scale, "prob0021.01")