#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 18, 2020

@author: johnmcalister

Brute force, but use skip amount to avoid trial division.  Need to include offset to avoid double inclusion of multiples of both values.
'''

def sumRange(n, end):
    return sum(x for x in range(n, end, n))

def solution(limit):
    return sumRange(3, limit) + sumRange(5, limit) - sumRange(15, limit)

if __name__ == "__main__":
    assert solution(10) == 23
    print(solution(1000))
    
    count = 100
    scale = 1000
    
    import utils.timing
    utils.timing.table_timing([10, 1000], count, scale)
    utils.timing.plot_timing([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000], count, scale)