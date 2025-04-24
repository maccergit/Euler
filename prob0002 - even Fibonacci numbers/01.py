#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Brute force - sum generated values that are even.
'''

def fib_gen(limit):
    f0 = 0
    fnext = 1
    while fnext < limit:
        yield fnext
        f0, fnext = fnext, fnext + f0

def solution(limit):
    return sum(x for x in fib_gen(limit) if x % 2 == 0)

if __name__ == "__main__":
    assert solution(100) == 44
    print(solution(4000000))
    
    count = 100000
    scale = 1000000
    
    import utils.timing
    utils.timing.table_timing([100, 4000000], count, scale)
    utils.timing.plot_timing([10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000], count, scale)
    
    assert solution(10**17) == 49597426547377748
    assert solution(10**30) == 727244555616386341839153320976
    assert solution(10**100) == 12065007678944807420403981310014175239608005638595098371630805388439212255831420630608529497465143520
    print("done")