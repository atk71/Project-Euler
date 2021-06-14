"""
The following problem is taken from Project Euler.

NUMBERS WITH A GIVEN PRIME FACTOR SUM

Consider the numbers 15, 16 and 18:
$15=3\times 5$ and $3+5=8$.
$16 = 2\times 2\times 2\times 2$ and $2+2+2+2=8$.
$18 = 2\times 3\times 3$ and $2+3+3=8$. 

15, 16 and 18 are the only numbers that have 8 as sum of the prime factors (counted with multiplicity).

We define $S(k)$ to be the sum of all numbers $n$ where the sum of the prime factors (with multiplicity)  of $n$ is $k$.
Hence $S(8) = 15+16+18 = 49$.
Other examples: $S(1) = 0$, $S(2) = 2$, $S(3) = 3$, $S(5) = 5 + 6 = 11$.

The Fibonacci sequence is $F_1 = 1, F_2 = 1, F_3 = 2, F_4 = 3, F_5 = 5$, ....
Find the last nine digits of $\displaystyle\sum_{k=2}^{24}{S(F_k)}$.

Published on Saturday, 13th January 2018, 07:00 pm; Solved by 920;Difficulty rating: 20%
"""


def problem_618():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_618())