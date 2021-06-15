"""
Link: [https://projecteuler.net/problem=3]

The following problem is taken from Project Euler.

LARGEST PRIME FACTOR

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Published on Friday, 2nd November 2001, 06:00 pm; Solved by 553271;Difficulty rating: 5%
"""


def largest_prime_factor():
    target_number = 600851475143
    prime_factors = []
    denominator = 2
    while target_number > 1:
        while target_number % denominator == 0:
            prime_factors.append(denominator)
            target_number /= denominator
        denominator += 1
        if target_number < pow(denominator, 2):
            if target_number > 1:
                prime_factors.append(target_number)
                break
    return int(prime_factors[-1])


if __name__ == "__main__":
    print(largest_prime_factor())  # 6857
