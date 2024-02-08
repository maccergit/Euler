'''
Created on Feb 23, 2020

@author: johnmcalister

TODO - convert unit tests to PyUnit
TODO - Use DocStrings
'''
import pyprimesieve
import math
import itertools

# Generate all prime factors of provided number
def gen_factors(limit):
    factors = pyprimesieve.factorize(limit)
    for x in factors:
        for _ in range(x[1]):
            yield x[0]

def testGenFactors(limit, expected):
    assert [x for x in gen_factors(limit)] == expected

testGenFactors(2, [2])
testGenFactors(3, [3])
testGenFactors(4, [2, 2])
testGenFactors(5, [5])
testGenFactors(6, [2, 3])
testGenFactors(7, [7])
testGenFactors(8, [2, 2, 2])
testGenFactors(9, [3, 3])
testGenFactors(10, [2, 5])
testGenFactors(11, [11])
testGenFactors(12, [2, 2, 3])

# Return dictionary of prime factors in {prime : power} format
def factPow(limit):
    return {factor : power for (factor, power) in pyprimesieve.factorize(limit)}

assert factPow(2) == {2 : 1}
assert factPow(3) == {3 : 1}
assert factPow(4) == {2 : 2}
assert factPow(5) == {5 : 1}
assert factPow(6) == {2 : 1, 3 : 1}
assert factPow(7) == {7 : 1}
assert factPow(8) == {2 : 3}
assert factPow(9) == {3 : 2}
assert factPow(10) == {2 : 1, 5 : 1}
assert factPow(11) == {11 : 1}
assert factPow(12) == {2 : 2, 3 : 1}

# Generate all divisors of provided number - not well ordered
def gen_divisors(limit):
    s = list(gen_factors(limit))
    return (y for y in {math.prod(x) for x in itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))})

def testGenDivisors(limit, expected):
    assert {x for x in gen_divisors(limit)} == expected

testGenDivisors(1, {1})
testGenDivisors(2, {1, 2})
testGenDivisors(3, {1, 3})
testGenDivisors(4, {1, 2, 4})
testGenDivisors(5, {1, 5})
testGenDivisors(6, {1, 2, 3, 6})
testGenDivisors(7, {1, 7})
testGenDivisors(8, {1, 2, 4, 8})
testGenDivisors(9, {1, 3, 9})
testGenDivisors(10, {1, 2, 5, 10})
testGenDivisors(11, {1, 11})
testGenDivisors(12, {1, 2, 3, 4, 6, 12})

def sumDivisors(limit):
    return math.prod((factor ** (power + 1) - 1) // (factor - 1) for factor, power in factPow(limit).items())

for limit in range(2, 13):
    assert sumDivisors(limit) == sum(x for x in gen_divisors(limit))
