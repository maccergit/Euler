#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 19, 2020

@author: johnmcalister
'''

# SymPy (diophantine)

from sympy.solvers.diophantine import diophantine
from sympy.abc import a, b, c
import math

def solution(limit):
    solution = set()
    # The next line computes the Diophantine solutions for "a + b + c = limit"
    # Returns a set of solutions.
    # Each solution contains an equation for a, b, and c - in this case, in 2 unknowns.
    # Note that the first expr is just the first unknown - so we can use "eq[0]" for the first unknown.
    # The second is a bit trickier - we note that the second expr is the sum of the two unknowns, so if we build a new expr from the second expr minus the first, then we get
    #   just the second unknown.  If we save the resulting expression, we now have SymPy expressions for the two unknowns, along with SymPy expressions for a, b, and c.
    # We can then sub the expressions for a, b, and c into the second equation to get Diophantine solutions that satisfy both equations, in terms of the two unknowns.
    # We can then substitute the solution values for the two unknowns back into the values for a, b, and c to get the solution values for a, b, and c, which we can then
    # filter to get only the positive values.  There will be duplicates, permutations, etc... - so sort results into a set to remove extra values.
    for eq in diophantine(a + b + c - limit):
        t1 = eq[1] - eq[0]
        # The next line computes the Diophantine solutions for "a² + b² = c²", with expressions for a, b, and c pulled from previous Diophantine solutions.
        # This means the result will be values for the two unknowns provide by the previous solution - values that satisfy both equations once they are subbed back in.
        for result in diophantine(eq[0] ** 2 + eq[1] ** 2 - eq[2] ** 2):
            candidate = sorted(x.subs({eq[0] : result[0], t1 : result[1]}) for x in eq if result[0] > 0)
            if candidate and candidate[0] > 0:
                solution.add(tuple(candidate))
    return math.prod(solution.pop())

assert solution(12) == 60
print(solution(1000))

count = 10
scale = 1000

import utils.timing
utils.timing.table_timing([12, 1000], count, scale)
utils.timing.plot_timing([12, 108, 200, 300, 400, 504, 600, 700, 800, 900, 1000], count, scale)