"""
Link: [https://projecteuler.net/problem=433]

The following problem is taken from Project Euler.

STEPS IN EUCLID'S ALGORITHM


Let E(x0, y0) be the number of steps it takes to determine the greatest common divisor of x0 and y0 with Euclid's algorithm. More formally:x1 = y0, y1 = x0 mod y0xn = yn-1, yn = xn-1 mod yn-1
E(x0, y0) is the smallest n such that yn = 0.


We have E(1,1) = 1, E(10,6) = 3 and E(6,10) = 4.


Define S(N) as the sum of E(x,y) for 1 ≤ x,y ≤ N.
We have S(1) = 1, S(10) = 221 and S(100) = 39826.


Find S(5·106).


Published on Saturday, 22nd June 2013, 04:00 pm; Solved by 442;Difficulty rating: 65%
"""


def problem_433():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_433())