"""
Link: [https://projecteuler.net/problem=403]

The following problem is taken from Project Euler.

LATTICE POINTS ENCLOSED BY PARABOLA AND LINE


For integers a and b, we define D(a, b) as the domain enclosed by the parabola y = x2 and the line y = a·x + b:D(a, b) = { (x, y) | x2 ≤ y ≤ a·x + b }.


L(a, b) is defined as the number of lattice points contained in D(a, b).
For example, L(1, 2) = 8 and L(2, -1) = 1.


We also define S(N) as the sum of L(a, b) for all the pairs (a, b) such that the area of D(a, b) is a rational number and |a|,|b| ≤ N.
We can verify that S(5) = 344 and S(100) = 26709528.


Find S(1012). Give your answer mod 108.


Published on Saturday, 24th November 2012, 10:00 pm; Solved by 332;Difficulty rating: 55%
"""


def problem_403():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_403())