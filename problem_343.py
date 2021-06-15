"""
Link: [https://projecteuler.net/problem=343]

The following problem is taken from Project Euler.

FRACTIONAL SEQUENCES

For any positive integer k, a finite sequence ai of fractions xi/yi is defined by:
a1 = 1/k and
ai = (xi-1+1)/(yi-1-1) reduced to lowest terms for i>1.
When ai reaches some integer n, the sequence stops. (That is, when yi=1.)
Define f(k) = n. 
For example, for k = 20:


1/20 → 2/19 → 3/18 = 1/6 → 2/5 → 3/4 → 4/3 → 5/2 → 6/1 = 6


So f(20) = 6.


Also f(1) = 1, f(2) = 2, f(3) = 1 and ∑ f(k3) = 118937 for 1 ≤ k ≤ 100.


Find ∑ f(k3) for 1 ≤ k ≤ 2×106.


Published on Saturday, 18th June 2011, 04:00 pm; Solved by 1332;Difficulty rating: 35%
"""


def problem_343():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_343())