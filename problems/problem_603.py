"""
Link: [https://projecteuler.net/problem=603]

The following problem is taken from Project Euler.

SUBSTRING SUMS OF PRIME CONCATENATIONS

Let $S(n)$ be the sum of all contiguous integer-substrings that can be formed from the integer $n$. The substrings need not be distinct. 
For example, $S(2024) = 2 + 0 + 2 + 4 + 20 + 02 + 24 + 202 + 024 + 2024 = 2304$.
Let $P(n)$ be the integer formed by concatenating the first $n$ primes together. For example, $P(7) = 2357111317$.
Let $C(n, k)$ be the integer formed by concatenating $k$ copies of $P(n)$ together. For example, $C(7, 3) = 235711131723571113172357111317$.
Evaluate $S(C(10^6, 10^{12}))$ mod $(10^9 + 7)$.

Published on Sunday, 14th May 2017, 01:00 am; Solved by 380;Difficulty rating: 45%
"""


def problem_603():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_603())