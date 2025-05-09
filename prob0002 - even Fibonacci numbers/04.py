#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister

Use closed form of fibonacci numbers (Binet's formula) to get every 3rd fibonacci number and sum them.  To get the index, the formula is reworked to get:
    index = (log(N) + log(5) / 2) / log(phi)
'''

import math

def solution(limit):
    root5 = (5 ** 0.5)
    phi = (1 + root5) / 2
    upsilon = 1 - phi
    i = int((math.log(limit) + math.log(5) / 2.0) / math.log(phi) / 3)
    return int(sum((phi ** x - upsilon ** x) for x in range(3, 3 * i + 3, 3)) / root5)

if __name__ == "__main__":
    assert solution(100) == 44
    print(solution(4000000))
    
    count = 100000
    scale = 1000000
    
    import utils.timing
    utils.timing.table_timing([100, 4000000], count, scale)
    utils.timing.plot_timing([10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000], count, scale)
    
    # This assetion fails because we exceed the precision of float, and it silently computes the wrong answer
    assert solution(10**17) == 49597426547377748
    print("done")