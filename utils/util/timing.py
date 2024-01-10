'''
Created on Feb 19, 2020

@author: johnmcalister

TODO - add unit tests/examples.
'''

import timeit
import matplotlib.pyplot as plt

# Return average execution time of "solution(parm)" when executed "count" times, in sec.
def timing(parm, count, scale):
    total_time = timeit.timeit(stmt = "solution(" + str(parm) + ")", number = count, setup = "from __main__ import solution")
    return total_time / count * scale

def table_timing(parms, count, scale):
    for data in ([parm, timing(parm, count, scale)] for parm in parms):
        print(data)

def plot_timing(parms, count, scale):
    plt.plot(parms, [timing(parm, count, scale) for parm in parms])
    plt.show()