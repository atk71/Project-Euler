"""
Link: [https://projecteuler.net/problem=7]

The following problem is taken from Project Euler.

10001ST PRIME

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

Published on Friday, 28th December 2001, 06:00 pm; Solved by 424045;Difficulty rating: 5%
"""
from math import isqrt
from numpy import full


def primes_less_than(target: int) -> list[int]:
    if target <= 2:
        return []
    is_prime = full(target, True)
    is_prime[:1] = False

    for i in range(2, isqrt(target)):
        if is_prime[i]:
            for x in range(pow(i, 2), target, i):
                is_prime[x] = False

    return [i for i in range(target) if is_prime[i]]


def ten_thousand_and_first_prime():
    target = 10001
    return primes_less_than(pow(target, 2))[target]


if __name__ == "__main__":
    print(ten_thousand_and_first_prime())
