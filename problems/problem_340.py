"""
Link: [https://projecteuler.net/problem=340]

The following problem is taken from Project Euler.

CRAZY FUNCTION


For fixed integers a, b, c, define the crazy function F(n) as follows:
F(n) = n - c for all n > b 
F(n) = F(a + F(a + F(a + F(a + n)))) for all n ≤ b.

Also, define $S(a, b, c) = \sum \limits_{n = 0}^{b} {F(n)}$.

For example, if a = 50, b = 2000 and c = 40, then F(0) = 3240 and F(2000) = 2040.
Also, S(50, 2000, 40) = 5204240.


Find the last 9 digits of S(217, 721, 127).


Published on Sunday, 29th May 2011, 07:00 am; Solved by 1045;Difficulty rating: 30%
"""


def problem_340():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_340())