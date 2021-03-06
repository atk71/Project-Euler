"""
Link: [https://projecteuler.net/problem=149]

The following problem is taken from Project Euler.

SEARCHING FOR A MAXIMUM-SUM SUBSEQUENCE

Looking at the table below, it is easy to verify that the maximum possible sum of adjacent numbers in any direction (horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).
Now, let us repeat the search, but on a much larger scale:
First, generate four million pseudo-random numbers using a specific form of what is known as a "Lagged Fibonacci Generator":
For 1 â‰¤ k â‰¤ 55, sk = [100003 âˆ’ 200003k + 300007k3] (modulo 1000000) âˆ’ 500000.
For 56 â‰¤ k â‰¤ 4000000, sk = [skâˆ’24 + skâˆ’55 + 1000000] (modulo 1000000) âˆ’ 500000.
Thus, s10 = âˆ’393027 and s100 = 86613.
The terms of s are then arranged in a 2000Ã—2000 table, using the first 2000 numbers to fill the first row (sequentially), the next 2000 numbers to fill the second row, and so on.
Finally, find the greatest sum of (any number of) adjacent entries in any direction (horizontal, vertical, diagonal or anti-diagonal).

Published on Friday, 13th April 2007, 10:00 pm; Solved by 4670;Difficulty rating: 50%
"""


def problem_149():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_149())