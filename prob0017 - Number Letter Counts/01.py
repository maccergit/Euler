#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 25, 2024

@author: johnmcalister
'''

# Convert a numeric value to its text representation.
# TODO - implement this - just a placeholder right now
def words(value):
    return "a"

assert words(1) == "one"
assert words(2) == "two"
assert words(3) == "three"
assert words(4) == "four"
assert words(5) == "five"
assert words(342) == "three hundred and forty-two"
assert words(115) == "one hundred and fifteen"

# Return the significant characters in the text representation of a value.
# "significant characters" means we skip spaces and hyphens - so plain "len()" won't do the trick.
# TODO - implement this - just a placeholder right now
def count(value):
    return len(words(value))

assert count(1) == 3
assert count(2) == 3
assert count(3) == 5
assert count(4) == 4
assert count(5) == 4
assert count(342) == 23
assert count(115) == 20

def solution(limit):
    return sum(count(x + 1) for x in range(limit))

assert solution(5) == 19
print(solution(1000))

count = 1
scale = 1

# mport utils.timing
# utils.timing.table_timing([15, 1000], count, scale)
# utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500], count, scale, "prob0017.01")