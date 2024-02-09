#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 6, 2024

@author: johnmcalister

Direct approach
'''

testData = ["0", "1", "2"]
probData = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def solution(limit):
    return "0"

data = testData

assert solution(1) == "012"
assert solution(2) == "021"
assert solution(3) == "102"
assert solution(4) == "120"
assert solution(5) == "201"
assert solution(6) == "210"

print(solution(1000000))

count = 1
scale = 1

# import utils.timing
# utils.timing.table_timing([24, 28123], count, scale)
# utils.timing.plot_timing([1000, 4000, 7000, 10000, 13000, 16000, 19000, 22000, 25000, 28123], count, scale, "prob0022.01")