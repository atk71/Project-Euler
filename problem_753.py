"""
Link: [https://projecteuler.net/problem=753]

The following problem is taken from Project Euler.

FERMAT EQUATION

Fermat's Last Theorem states that no three positive integers $a$, $b$, $c$ satisfy the equation 
$$a^n+b^n=c^n$$
for any integer value of $n$ greater than 2.
For this problem we are only considering the case $n=3$. For certain values of $p$, it is possible to solve the congruence equation:
$$a^3+b^3 \equiv c^3 \pmod{p}$$
For a prime $p$, we define $F(p)$ as the number of integer solutions to this equation for $1 \le a,b,c < p$.
You are given $F(5) = 12$ and $F(7) = 0$.
Find the sum of $F(p)$ over all primes $p$ less than $6\,000\,000$.

Published on Sunday, 28th March 2021, 05:00 am; Solved by 261
"""


def problem_753():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_753())