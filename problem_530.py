"""
The following problem is taken from Project Euler.

GCD OF DIVISORS

Every divisor d of a number n has a complementary divisor n/d.
Let f(n) be the sum of the greatest common divisor of d and n/d over all positive divisors d of n, that is
$f(n)=\displaystyle\sum\limits_{d|n}\, \text{gcd}(d,\frac n d)$.
Let F be the summatory function of f, that is
$F(k)=\displaystyle\sum\limits_{n=1}^k \, f(n)$.
You are given that F(10)=32 and F(1000)=12776.
Find F(1015).

Published on Sunday, 18th October 2015, 01:00 am; Solved by 412;Difficulty rating: 60%
"""


def problem_530():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_530())