"""
Link: [https://projecteuler.net/problem=167]

The following problem is taken from Project Euler.

INVESTIGATING ULAM SEQUENCES

For two positive integers a and b, the Ulam sequence U(a,b) is defined by U(a,b)1 = a, U(a,b)2 = b and for k > 2,
U(a,b)k is the smallest integer greater than U(a,b)(k-1) which can be written in exactly one way as the sum of two distinct previous members of U(a,b).
For example, the sequence U(1,2) begins with
1, 2, 3 = 1 + 2, 4 = 1 + 3, 6 = 2 + 4, 8 = 2 + 6, 11 = 3 + 8;
5 does not belong to it because 5 = 1 + 4 = 2 + 3 has two representations as the sum of two previous members, likewise 7 = 1 + 6 = 3 + 4.
Find âˆ‘â€‰U(2,2n+1)k for 2 â‰¤ n â‰¤10, where k = 1011.

Published on Friday, 9th November 2007, 01:00 pm; Solved by 1590;Difficulty rating: 75%
"""


def problem_167():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_167())