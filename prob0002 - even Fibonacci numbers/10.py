#!/usr/bin/python
# coding=utf-8

'''
Created on May 3, 2026

@author: johnmcalister

Matrix exponentiation with exponentiation-by-squaring gives F(n) in O(log n) time.
The sum of even Fibonacci terms through F(3k) is (F(3k+2) - 1) / 2, so one F(3k+2)
call produces the answer.  All arithmetic stays in Python int, so there are no
precision knobs to tune and the algorithm works at any limit Python can represent.
'''

import math

# Fibonacci companion matrix.
#   [ F(n+1) ]   [ 1  1 ] [ F(n)   ]
#   [ F(n)   ] = [ 1  0 ] [ F(n-1) ]
Q = ((1, 1), (1, 0))
I = ((1, 0), (0, 1))

def mat_mul(A, B):
    return (
        (A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]),
        (A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]),
    )

def mat_pow(M, n):
    result = I
    base = M
    while n > 0:
        if n & 1:
            result = mat_mul(result, base)
        n >>= 1
        if n > 0:
            base = mat_mul(base, base)
    return result

def fib(n):
    # F(n) is the top-right (or bottom-left) entry of Q^n.
    return mat_pow(Q, n)[0][1]

def solution(limit):
    phi = (1 + 5 ** 0.5) / 2
    exp = 3 * int((math.log(limit) + math.log(5) / 2.0) / math.log(phi) / 3) + 2
    return (fib(exp) - 1) // 2

if __name__ == "__main__":
    assert solution(100) == 44
    print(solution(4000000))

    count = 100000
    scale = 1000000

    import utils.timing
    utils.timing.table_timing([100, 4000000], count, scale)
    utils.timing.plot_timing([10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000], count, scale)

    # Pure integer arithmetic - no precision knobs needed.
    assert solution(10**17) == 49597426547377748
    assert solution(10**30) == 727244555616386341839153320976
    assert solution(10**100) == 12065007678944807420403981310014175239608005638595098371630805388439212255831420630608529497465143520
    print("done")
