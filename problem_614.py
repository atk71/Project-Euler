"""
Link: [https://projecteuler.net/problem=614]

The following problem is taken from Project Euler.

SPECIAL PARTITIONS 2

An integer partition of a number $n$ is a way of writing $n$ as a sum of positive integers. Partitions that differ only by the order of their summands are considered the same.
We call an integer partition special if 1) all its summands are distinct, and 2) all its even summands are also divisible by 4. For example, the special partitions of $10$ are: \[10 = 1+4+5=3+7=1+9\]
The number $10$ admits many more integer partitions (a total of 42), but only those three are special.
Let be $P(n)$ the number of special integer partitions of $n$. You are given that $P(1) = 1$, $P(2) = 0$, $P(3) = 1$, $P(6) = 1$, $P(10)=3$, $P(100) = 37076$ and $P(1000)=3699177285485660336$.
Find $\displaystyle \sum_{i=1}^{10^7}{P(i)}$. Give the result modulo $10^9+7$.

Published on Sunday, 19th November 2017, 07:00 am; Solved by 282;Difficulty rating: 55%
"""


def problem_614():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_614())