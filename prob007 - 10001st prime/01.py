#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Brute force
'''

def nextPrime():
    current = 1
    primes = []
    while True:
        current += 1
        for prime in primes:
            if current % prime == 0:
                break
        else:
            primes.append(current)
            yield current

def solution(limit):
    nexPrimeGen = nextPrime()
    for _ in range(limit):
        value = next(nexPrimeGen)
    return value

assert solution(6) == 13
print(solution(10001))

count = 1
scale = 1000000 # µsec

import utils.timing
utils.timing.table_timing([6, 10001], count, scale)
utils.timing.plot_timing([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], count, scale)