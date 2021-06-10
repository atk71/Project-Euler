"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


from math import pow, isqrt


def nth_prime(n):
    return primes_less_than(n*n)[n]


def primes_less_than(n: int) -> list[int]:
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n)):
        if is_prime[i]:
            for x in range(i * i, n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]


print(nth_prime(10001))
