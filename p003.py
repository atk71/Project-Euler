"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import pow


def largest_prime(n: int) -> int:
    factors = []
    denominator = 2
    while n > 1:
        while n % denominator == 0:
            factors.append(denominator)
            n /= denominator
        denominator += 1
        if n < pow(denominator, 2):
            if n > 1:
                factors.append(n)
                break
    return int(factors[-1])


print(largest_prime(600851475143))
