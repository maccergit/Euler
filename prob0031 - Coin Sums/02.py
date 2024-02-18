#!/usr/bin/python
# coding=utf-8

'''
Created on Feb 15, 2024

@author: johnmcalister

Direct approach - use tuples in preparation for memoization
'''

coins = (1, 2, 5, 10, 20, 50, 100, 200)

def getCoins(limit, currentCoins):
    if limit == 0:
        retval =  []
    elif currentCoins == (1,):
        retval = [{1 : limit}]
    else:
        maxCoin = max(currentCoins)
        currentCoins = tuple(x for x in currentCoins if x != maxCoin)
        retval = []
        for i in range(1, limit // maxCoin + 1):
            prefix = {maxCoin : i}
            combos = getCoins(limit - maxCoin * i, currentCoins)
            for combo in combos:
                combo |= prefix.copy()
            if combos == []:
                combos = [prefix.copy()]
            retval += combos.copy()
        retval += getCoins(limit, currentCoins)
    return retval

assert getCoins(1, (1,)) == [{1 : 1}]
assert getCoins(2, (1,)) == [{1 : 2}]
assert getCoins(2, (1, 2)) == [{2 : 1}, {1 : 2}]
assert getCoins(3, (1, 2)) == [{2 : 1, 1 : 1}, {1 : 3}]
assert getCoins(4, (1, 2)) == [{2 : 1, 1 : 2}, {2 : 2}, {1 : 4}]
assert getCoins(4, (1, 2, 3)) == [{3 : 1, 1 : 1}, {2 : 1, 1 : 2}, {2 : 2}, {1 : 4}]

def solution(limit):
    return len(getCoins(limit, coins))

# from observation
assert solution(1) == 1
assert solution(2) == 2
assert solution(3) == 2
assert solution(4) == 3
assert solution(5) == 4
assert solution(6) == 5
assert solution(7) == 6
assert solution(8) == 7
assert solution(9) == 8

print(solution(200))

count = 3
scale = 1000

import utils.timing
utils.timing.table_timing([200], count, scale)
utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200], count, scale, ticks = False)
