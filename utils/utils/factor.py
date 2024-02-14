'''
Created on Feb 23, 2020

@author: johnmcalister

TODO - convert unit tests to PyUnit
TODO - Use DocStrings
'''
from utils.prod import prod

# Generate all prime factors of provided number
def gen_factors(limit):
    if limit < 2:
        return
    current = 2
    while (current * current) < (limit + 1):
        if limit % current != 0:
            current += 1
        else:
            yield current
            limit = limit // current
    yield limit

def testGenFactors(limit, expected):
    assert [*gen_factors(limit)] == expected

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
testGenFactors(-2, [])

# Return dictionary of prime factors in {prime : power} format
def factPow(limit):
    factors = {}
    for factor in gen_factors(limit):
        if factor not in factors:
            factors[factor] = 1
        else:
            factors[factor] += 1
    return factors

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
assert factPow(-2) == {}

# Generate all divisors of provided number - not well ordered
def gen_divisors(limit):
    if (limit < 1):
        yield 1
    current = 1
    while (current * current) < (limit + 1):
        if limit % current == 0:
            yield current
            if current != limit // current:
                yield limit // current
        current += 1

def testGenDivisors(limit, expected):
    assert {*gen_divisors(limit)} == expected

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
testGenDivisors(-2, {1})

def sumDivisors(limit):
    return prod((factor ** (power + 1) - 1) // (factor - 1) for factor, power in factPow(limit).items())

for limit in range(-4, 13):
    assert sumDivisors(limit) == sum(gen_divisors(limit))
