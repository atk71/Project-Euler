"""
The following problem is taken from Project Euler.

MAXIMUM PRODUCT OF PARTS

Let N be a positive integer and let N be split into k equal parts, r = N/k, so that N = r + r + ... + r.
Let P be the product of these parts, P = r × r × ... × r = rk.
For example, if 11 is split into five equal parts, 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2, then P = 2.25 = 51.53632.
Let M(N) = Pmax for a given value of N.
It turns out that the maximum for N = 11 is found by splitting eleven into four equal parts which leads to Pmax = (11/4)4; that is, M(11) = 14641/256 = 57.19140625, which is a terminating decimal.
However, for N = 8 the maximum is achieved by splitting it into three equal parts, so M(8) = 512/27, which is a non-terminating decimal.
Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if M(N) is a terminating decimal.
For example, ∑ D(N) for 5 ≤ N ≤ 100 is 2438.
Find ∑ D(N) for 5 ≤ N ≤ 10000.

Published on Friday, 22nd February 2008, 05:00 pm; Solved by 4510;Difficulty rating: 45%
"""


def problem_183():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_183())