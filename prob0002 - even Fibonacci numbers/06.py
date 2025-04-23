#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 16, 2025

@author: johnmcalister

Use closed form of sum of even fibonacci numbers.  Note - use of floats and large exponents causes this to fail around 14 quadrillian+.
'''

import math

def solution(limit):
    root5 = (5 ** 0.5)
    phi = (1 + root5) / 2
    upsilon = (1 - root5) / 2
    exp = 3 * int((math.log(limit) + math.log(5) / 2.0) / math.log(phi) / 3) + 2
    return int((phi ** exp - upsilon ** exp - root5) / (2 * root5))

if __name__ == "__main__":
    assert solution(100) == 44
    print(solution(4000000))
    
    count = 100000
    scale = 1000000
    
    import utils.timing
    utils.timing.table_timing([100, 4000000], count, scale)
    utils.timing.plot_timing([10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000], count, scale)