#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 18, 2024

@author: johnmcalister

Diophantine approach
'''

from sympy.solvers.diophantine import diophantine
from sympy.abc import a, b, c
import math

def solution(limit):
    eq = 10 * a * c + b * c - 10 * a * b - a * c
    solutions = {}
    for i in range(1, 10):
        solutions[i] = {x for x in diophantine(eq.subs({a : i})) if x[0] > 0 and x[1] > 0 and x[0] < 10 and x[1] < 10 and x[0] != x[1]}
    numerator = 1
    denominator = 1
    for x in solutions:
        if solutions[x] != set():
            for y, z in solutions[x]:
                numerator *= 10 * x + y
                denominator *= 10 * y + z
    gcd = math.gcd(numerator, denominator)
    return denominator // gcd

print(solution(0))

count = 1
scale = 1000

import utils.timing
utils.timing.table_timing([0], count, scale)
# utils.timing.plot_timing([3, 4, 5, 6, 7, 8, 9], count, scale)
