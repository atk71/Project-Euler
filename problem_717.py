"""
Link: [https://projecteuler.net/problem=717]

The following problem is taken from Project Euler.

SUMMATION OF A MODULAR FORMULA

For an odd prime $p$, define $f(p) = \left\lfloor\frac{2^{(2^p)}}{p}\right\rfloor\bmod{2^p}$
For example, when $p=3$, $\lfloor 2^8/3\rfloor = 85 \equiv 5 \pmod 8$ and so $f(3) = 5$.
Further define $g(p) = f(p)\bmod p$. You are given $g(31) = 17$.
Now define $G(N)$ to be the summation of $g(p)$ for all odd primes less than $N$.
You are given $G(100) = 474$ and $G(10^4) = 2819236$.
Find $G(10^7)$

Published on Saturday, 23rd May 2020, 02:00 pm; Solved by 367;Difficulty rating: 25%
"""


def problem_717():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_717())