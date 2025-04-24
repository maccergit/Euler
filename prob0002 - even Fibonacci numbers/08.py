#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 16, 2025

@author: johnmcalister

Use closed form of sum of even fibonacci numbers.  Use mpmath.mpf to handle limits over 10**17.
However, mpf is still fixed precision.
'''

import mpmath

# Use same precision as Decimal default
mpmath.mp.dps = 28

def solution(limit):
    root5 = mpmath.mp.sqrt(5)
    phi = (1 + root5) / 2
    upsilon = (1 - root5) / 2
    exp = 3 * int((mpmath.log(limit, 10) + mpmath.log(5, 10) / 2) / mpmath.log(phi, 10) / 3) + 2
    return mpmath.nint((phi ** exp - upsilon ** exp - root5) / (2 * root5))

if __name__ == "__main__":
    assert solution(100) == 44
    print(solution(4000000))
    
    count = 1000
    scale = 1000000
    
    import utils.timing
    utils.timing.table_timing([100, 4000000], count, scale)
    utils.timing.plot_timing([10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000], count, scale)
    
    assert solution(10**17) == 49597426547377748
    # This fails because we have exceeded the default precision of Decimal, and the calculations silently return the wrong value.
    # However, changine the precision to 100 allows this test to pass.
    assert solution(10**30) == 727244555616386341839153320976
    # If you comment out the previous line, this next one won't throw an error in solution code, and silently return the wrong value - and then fail the assertion.
    # However, changing the precision to 200 allows this test to pass.
    assert solution(10**100) == 12065007678944807420403981310014175239608005638595098371630805388439212255831420630608529497465143520
    print("done")