'''
Created on Feb 19, 2020

@author: johnmcalister

TODO - add unit tests/examples.
'''

import timeit
import matplotlib.pyplot as plt
import os
from sys import _getframe

# Return average execution time of "solution(parm)" when executed "count" times, in sec (scaled by "scale" - 1000 = msec, 1000000 = µsec, etc...)
def timing(parm, count, scale):
    total_time = timeit.timeit(stmt = "solution(" + str(parm) + ")", number = count, setup = "from __main__ import solution")
    return total_time / count * scale

def getScaleUnits(scale):
    if scale == 1:
        return "sec"
    elif scale == 1000:
        return "msec"
    elif scale == 1000000:
        return "µsec"
    elif scale == 1000000000:
        return "nsec"

# Display a table of multiple timing runs using different parameters - "parms" is a list of parameters, each of which is used in a separate timing run.  The current parm, "count", and "scale"
# are passed to "timing()", and the results are displayed in tabular form.
def table_timing(parms, count, scale):
    print(os.path.basename(os.getcwd()), "-", os.path.splitext(os.path.basename(_getframe(1).f_locals["__file__"]))[0])
    units = getScaleUnits(scale)
    for data in ([parm, str(timing(parm, count, scale)) + " " + units] for parm in parms):
        print(data)

# Like "table_timing()" above, but displays results in a pyplot graph, with labeled axes.  Time units are inferred from "scale" and included on time axis.
# Default behavior is to use every x value as a tick mark - but more than about 10-20 elements will not be clear - passing "False" for "ticks" parameter will allow PyPlot
# to automatically generate ticks for the x-axis.
def plot_timing(parms, count, scale, ticks = True):
    plt.plot(parms, [timing(parm, count, scale) for parm in parms])
    if (ticks):
        plt.xticks(parms)
    plt.title(os.path.basename(os.getcwd()) + " - " + os.path.splitext(os.path.basename(_getframe(1).f_locals["__file__"]))[0])
    plt.xlabel("limit")
    ylabel = "time (" + getScaleUnits(scale) + ")"
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()