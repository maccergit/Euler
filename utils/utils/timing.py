'''
Created on Feb 19, 2020

@author: johnmcalister

TODO - add unit tests/examples.
'''

import timeit
import matplotlib.pyplot as plt

# Return average execution time of "solution(parm)" when executed "count" times, in sec (scaled byh "scale" - 1000 = msec, 1000000 = µsec, etc...)
def timing(parm, count, scale):
    total_time = timeit.timeit(stmt = "solution(" + str(parm) + ")", number = count, setup = "from __main__ import solution")
    return total_time / count * scale

def table_timing(parms, count, scale, title = ''):
    if title:
        print(title)
    for data in ([parm, timing(parm, count, scale)] for parm in parms):
        print(data)

def plot_timing(parms, count, scale, title = ''):
    plt.plot(parms, [timing(parm, count, scale) for parm in parms])
    plt.xticks(parms)
    plt.title(title)
    plt.xlabel("limit")
    ylabel = "time"
    if scale == 1:
        ylabel = ylabel + " (sec)"
    elif scale == 1000:
        ylabel = ylabel + " (msec)"
    elif scale == 1000000:
        ylabel = ylabel + " (µsec)"
    elif scale == 1000000000:
        ylabel = ylabel + " (nsec)"
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()