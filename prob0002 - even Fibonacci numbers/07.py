#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 16, 2025

@author: johnmcalister

Use closed form of sum of even fibonacci numbers.  Use decimal.Decimal to handle limits over 10**17.
However, decimal is still fixed precision (default = 28 digits, but is configurable).
'''

from decimal import Decimal, localcontext

def solution(limit):
    root5 = Decimal(5).sqrt()
    phi = (1 + root5) / 2
    upsilon = (1 - root5) / 2
    exp = 3 * int((Decimal(limit).log10() + Decimal(5).log10() / 2) / phi.log10() / 3) + 2
    
    with localcontext() as ctx:
        ctx.prec = 100
        return ((phi ** exp - upsilon ** exp - root5) / (2 * root5)).quantize(Decimal(1))

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
    assert solution(10**30) == 727244555616386341839153320976
    # If you comment out the previous line, then this fails because we exceed the local precision used by "quantize()", and quantize() checks for loss of precision.
    print(solution(10**100))
    print("done")