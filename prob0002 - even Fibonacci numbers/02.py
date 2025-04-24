#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Brute force, skipping odd fibonacci numbers
'''

def fib_even(limit):
    f0 = 1
    fnext = 2
    while fnext < limit:
        yield fnext
        fnext2 = f0 + fnext
        fnext3 = fnext + fnext2
        fnext = fnext2 + fnext3
        f0 = fnext3

def solution(limit):
    return sum(x for x in fib_even(limit))

if __name__ == "__main__":
    assert solution(100) == 44
    print(solution(4000000))
    
    count = 100000
    scale = 1000000
    
    import utils.timing
    utils.timing.table_timing([100, 4000000], count, scale)
    utils.timing.plot_timing([10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000], count, scale)
    
    assert solution(10**17) == 49597426547377748
    print("done")