#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 1, 2024

@author: johnmcalister

Direct approach with utils.fastfactor version of divisors.  Similar to utils.factor version, but uses fast libraries to generate factors.

NOTE: utils.fastfactor.gen_divisors() generates all divisors, not just proper divisors - so we need to remove the number being factored from the list of divisors.
'''

import utils.fastfactor

assert {x for x in utils.fastfactor.gen_divisors(220)} - {220} == {1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110}
assert {x for x in utils.fastfactor.gen_divisors(284)} - {284} == {1, 2, 4, 71, 142}

def isAmicable(x):
    divSum = sum(utils.fastfactor.gen_divisors(x)) - x
    return x == sum(utils.fastfactor.gen_divisors(divSum)) - divSum and x != divSum

assert isAmicable(220)
assert isAmicable(284)

def solution(limit):
    return sum(x for x in range(limit) if isAmicable(x))

print(solution(10000))

count = 3
scale = 1000

import utils.timing
utils.timing.table_timing([1000, 10000], count, scale)
utils.timing.plot_timing([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], count, scale, "prob0021.04")