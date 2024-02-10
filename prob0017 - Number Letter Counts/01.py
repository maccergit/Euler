#!/usr/bin/python
# coding=utf-8

'''
Created on Jan 25, 2024

@author: johnmcalister
'''

number_words = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven", 
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen", 
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety"
}

# Convert a numeric value to its text representation.
def words(value):
    if value < 21:
        return number_words[value]
    if value < 100:
        if value % 10 == 0:
            return number_words[value]
        return number_words[(value // 10) * 10] + "-" + number_words[value % 10]
    if value < 1000:
        if value % 100 == 0:
            return number_words[value // 100] + " hundred"
        return number_words[value // 100] + " hundred and " + words(value % 100)
    return "one thousand"

assert words(1) == "one"
assert words(2) == "two"
assert words(3) == "three"
assert words(4) == "four"
assert words(5) == "five"
assert words(342) == "three hundred and forty-two"
assert words(115) == "one hundred and fifteen"

# Return the significant characters in the text representation of a value.
# "significant characters" means we skip spaces and hyphens - so plain "len()" won't do the trick.
def count_chars(value):
    return len([x for x in words(value) if x not in " -"])

assert count_chars(1) == 3
assert count_chars(2) == 3
assert count_chars(3) == 5
assert count_chars(4) == 4
assert count_chars(5) == 4
assert count_chars(342) == 23
assert count_chars(115) == 20

def solution(limit):
    return sum(count_chars(x + 1) for x in range(limit))

assert solution(5) == 19
print(solution(1000))

count = 100
scale = 1000

import utils.timing
utils.timing.table_timing([5, 1000], count, scale)
utils.timing.plot_timing([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], count, scale)