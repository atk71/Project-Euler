"""
The following problem is taken from Project Euler.

EXPONENT DIFFERENCE


For any integer $n>0$ and prime number $p,$ define $\nu_p(n)$ as the greatest integer $r$ such that $p^r$ divides $n$. 


Define $$D(n, m)  = \sum_{p \text{ prime}} \left| \nu_p(n) - \nu_p(m)\right|.$$ For example, $D(14,24) = 4$.


Furthermore, define $$S(N) = \sum_{1 \le n, m \le N} D(n, m).$$ You are given $S(10) = 210$ and $S(10^2) = 37018$.


Find $S(10^{12})$. Give your answer modulo $1\,000\,000\,007$.


Published on Saturday, 18th April 2020, 11:00 pm; Solved by 380;Difficulty rating: 25%
"""


def problem_712():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_712())