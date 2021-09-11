"""
Link: [https://projecteuler.net/problem=5]

The following problem is taken from Project Euler.

SMALLEST MULTIPLE

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Published on Friday, 30th November 2001, 06:00 pm; Solved by 492697;Difficulty rating: 5%
"""
from math import lcm


def smallest_multiple() -> int:
    return lcm(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)


if __name__ == "__main__":
    print(smallest_multiple())  # 232792560
