"""
The following problem is taken from Project Euler.

A REAL RECURSION


For every real number $a \gt 1$ is given the sequence $g_a$ by:
$g_{a}(x)=1$ for $x \lt a$
$g_{a}(x)=g_{a}(x-1)+g_a(x-a)$ for $x \ge a$

$G(n)=g_{\sqrt {n}}(n)$
$G(90)=7564511$.

Find $\sum G(p)$ for $p$ prime and $10000000 \lt p \lt 10010000$
Give your answer modulo 1000000007.


Published on Saturday, 23rd May 2015, 01:00 pm; Solved by 423;Difficulty rating: 45%
"""


def problem_517():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_517())