"""
The following problem is taken from Project Euler.

CIRCULAR LOGIC II

Given an integer $n$, $n \geq 3$, let $B=\{\mathrm{false},\mathrm{true}\}$ and let $B^n$ be the set of sequences of $n$ values from $B$. The function $f$ from $B^n$ to $B^n$ is defined by $f(b_1 \dots b_n) = c_1 \dots c_n$ where:
Let $S(n)$ be the number of functions $T$ from $B^n$ to $B$ such that for all $x$ in $B^n$, $T(x) ~\mathrm{AND}~ T(f(x)) = \mathrm{false}$.
You are given that $S(3) = 35$ and $S(4) = 2118$.
Find $S(20)$. Give your answer modulo $1\,001\,001\,011$.

Published on Saturday, 22nd February 2020, 10:00 pm; Solved by 254;Difficulty rating: 45%
"""


def problem_703():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_703())