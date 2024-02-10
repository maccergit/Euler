#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 6, 2024

@author: johnmcalister

Direct approach - roll your own file parsing
'''

with open('0022_names.txt') as infile:
    rawData = infile.read().strip()

names = sorted([x[1:-1] for x in rawData.split(',')])

def alphaValueChar(c):
    return ord(c) - ord('A') + 1

assert alphaValueChar('A') == 1
assert alphaValueChar('Z') == 26
assert alphaValueChar('C') == 3
assert alphaValueChar('O') == 15
assert alphaValueChar('L') == 12
assert alphaValueChar('I') == 9
assert alphaValueChar('N') == 14

def alphaValueStr(x):
    return sum(alphaValueChar(c) for c in x)

assert alphaValueStr("COLIN") == 53

def solution(limit):
    return sum((i + 1) * alphaValueStr(names[i]) for i in range(len(names)))

assert [(i + 1) * alphaValueStr(names[i]) for i in range(len(names)) if names[i] == "COLIN"] == [49714]
print(solution(0))

count = 100
scale = 1000

import utils.timing
utils.timing.table_timing([0], count, scale)
# utils.timing.plot_timing([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], count, scale)