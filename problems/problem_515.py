"""
Link: [https://projecteuler.net/problem=515]

The following problem is taken from Project Euler.

DISSONANT NUMBERS

Let d(p,n,0) be the multiplicative inverse of n modulo prime p, defined as n × d(p,n,0) = 1 mod p.
Let d(p,n,k) = $\sum_{i=1}^n$d(p,i,k−1) for k ≥ 1.
Let D(a,b,k) = $\sum$(d(p,p-1,k) mod p) for all primes a ≤ p < a + b.
You are given:
Find D(109,105,105).

Published on Sunday, 10th May 2015, 07:00 am; Solved by 428;Difficulty rating: 40%
"""


def problem_515():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_515())