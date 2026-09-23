#!/usr/bin/python
# coding=utf-8

'''
Created on Sep 23, 2026

@author: johnmcalister
Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>

Multiply the prime powers in a balanced binary tree instead of accumulating
them into one running product.

13.py established that the sieve is no longer worth attacking - it is 0.04% of
the runtime at a limit of a million.  Everything else is the pi(limit) bignum
multiplies, and the count of those is fixed by the formula.  What is not fixed
is the order.

"result *= power" pairs a huge accumulator with a tiny prime at every step, and
that is the worst possible shape for bignum multiplication.  Schoolbook multiply
of an m-bit number by a k-bit number costs O(m * k), and the one fast algorithm
CPython has - Karatsuba, used once *both* operands reach 70 of its internal
30-bit digits, about 2100 bits - cannot help when one side is a 20-bit prime no
matter how large the other side gets.  The accumulator is also re-built in full
on every one of those multiplies, so the total work is quadratic in the size of
the answer : measurably n^1.93 to n^1.96 in 13.py.

A product tree fixes the shape.  Multiply adjacent pairs, then adjacent pairs of
those results, and so on up : every multiply then has two operands of roughly
equal size, which is the case Karatsuba was written for.  The number of
multiplies is the same, and the total number of bits passing through each level
of the tree is the same, but log2(pi(limit)) levels of balanced multiplies is a
different cost curve from one linear sweep - n^1.54 to n^1.57 measured, against
Karatsuba's log2(3) = 1.585.

The catch is at the small end.  Nothing is gained until partial products pass
the 2100-bit cutoff, so below a limit of about 4000 this is pure overhead - the
list slicing and the extra passes buy schoolbook multiplies that would have been
schoolbook anyway.  At the problem's own limit of 20 it is 3x slower than 13.py.
'''

import primesieve

def solution(limit):
    if limit < 2:
        return 1

    # Highest power of each prime that is still within the limit.
    powers = []
    for p in primesieve.primes(limit):
        power = p
        while power * p <= limit:
            power *= p
        powers.append(power)

    # Collapse the list pairwise until one value is left.  Each pass halves the
    # count and doubles the operand size, so operands stay balanced all the way
    # up - unlike a running product, where one side is always tiny.
    while len(powers) > 1:
        # An odd element at the end is carried up to the next level untouched.
        powers = [a * b for a, b in zip(powers[::2], powers[1::2])] + powers[len(powers) - len(powers) % 2:]

    return powers[0]

if __name__ == "__main__":
    assert solution(10) == 2520
    print(solution(20))

    count = 10000
    scale = 1000000

    import utils.timing
    utils.timing.table_timing([10, 20], count, scale)
    utils.timing.plot_timing([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], count, scale)

    assert solution(43) == 9419588158802421600
    assert solution(100) == 69720375229712477164533808935312303556800
    print("done")
