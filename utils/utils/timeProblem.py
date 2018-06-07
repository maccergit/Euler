# coding: utf8
"""
Timing utility

Each of the tests runs a function called "getSolution", which takes a limit as a parameter.
Time the test case, passing the passed in limit, for "count" iterations and display the average execution time of a single iteration.
"""

import timeit

def timeProblem(probLimit, count = 10000):
    print(str(timeit.timeit("getSolution(" + str(probLimit) + ")", setup = "from __main__ import getSolution", number = count) / count) + " sec")