#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 16, 2025

@author: johnmcalister

Use closed form of sum of even fibonacci numbers.  Use gmpy2 for optimized speed.
'''

import gmpy2

# Set precision to roughly match Decimal default of 28 digits
# gmpy2 precision is in bits: 28 * log2(10) ≈ 93 bits
gmpy2.get_context().precision = 93

def solution(limit):
    # Convert limit to mpfr immediately
    limit_m = gmpy2.mpfr(limit)
    root5 = gmpy2.sqrt(gmpy2.mpfr(5))
    phi = (1 + root5) / 2
    psi = (1 - root5) / 2 # Using psi for clarity
    
    # log10 in gmpy2 is log10(x)
    # The exponent calculation:
    n_val = (gmpy2.log10(limit_m) + gmpy2.log10(5) / 2) / gmpy2.log10(phi)
    k = int(n_val // 3)
    exp = 3 * k + 2
    
    # Calculate sum and round to nearest integer
    numerator = (phi ** exp) - (psi ** exp) - root5
    result = numerator / (2 * root5)
    
    return int(gmpy2.rint(result))

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
    # However, changine the precision to 100 allows this test to pass = 333 bits.
    assert solution(10**30) == 727244555616386341839153320976
    # If you comment out the previous line, this next one won't throw an error in solution code, and silently return the wrong value - and then fail the assertion.
    # However, changing the precision to 200 allows this test to pass = 665 bits.
    assert solution(10**100) == 12065007678944807420403981310014175239608005638595098371630805388439212255831420630608529497465143520
    print("done")