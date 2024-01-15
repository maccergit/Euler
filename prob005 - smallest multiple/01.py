#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Solved by inspection - 2520 is LCM of 1..10, so just need to multiply by primes missing from 11..20
NOTE: 2 is needed because 16 is 2⁴, and 2520 only contains 2³ : 2520 is divisible by 8 (= 2³), but not by 16 (= 2⁴), but limit includes 16.
NOTE: This obviously does not scale well, but can be a launch pad for better solutions.
'''

def solution(limit):
    return 2520 * 11 * 13 * 2 * 17 * 19

print(solution(20))

count = 1000
scale = 1000000 # µsec

import utils.timing
utils.timing.table_timing([20], count, scale)