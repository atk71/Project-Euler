"""
Link: [https://projecteuler.net/problem=130]

The following problem is taken from Project Euler.

COMPOSITES WITH PRIME REPUNIT PROPERTY

A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.
Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.
You are given that for all primes, p > 5, that p âˆ’ 1 is divisible by A(p). For example, when p = 41, A(41) = 5, and 40 is divisible by 5.
However, there are rare composite values for which this is also true; the first five examples being 91, 259, 451, 481, and 703.
Find the sum of the first twenty-five composite values of n for whichGCD(n, 10) = 1 and n âˆ’ 1 is divisible by A(n).

Published on Friday, 27th October 2006, 06:00 pm; Solved by 5707;Difficulty rating: 45%
"""


def problem_130():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_130())