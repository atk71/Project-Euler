"""
Link: [https://projecteuler.net/problem=722]

The following problem is taken from Project Euler.

SLOWLY CONVERGING SERIES

For a non-negative integer $k$, define
\[
E_k(q) = \sum\limits_{n = 1}^\infty \sigma_k(n)q^n
\]
where $\sigma_k(n) = \sum_{d \mid n} d^k$ is the sum of the $k$-th powers of the positive divisors of $n$.
It can be shown that, for every $k$, the series $E_k(q)$ converges for any $0 < q < 1$.
For example,
$E_1(1 - \frac{1}{2^4}) = \mathrm{3.872155809243e2}$
$E_3(1 - \frac{1}{2^8}) = \mathrm{2.767385314772e10}$
$E_7(1 - \frac{1}{2^{15}}) = \mathrm{6.725803486744e39}$
All the above values are given in scientific notation rounded to twelve digits after the decimal point.
Find the value of $E_{15}(1 - \frac{1}{2^{25}})$.
Give the answer in scientific notation rounded to twelve digits after the decimal point.

Published on Sunday, 28th June 2020, 05:00 am; Solved by 378;Difficulty rating: 25%
"""


def problem_722():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_722())