"""
The following problem is taken from Project Euler.

MULTIPLES OF 3 AND 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Published on Friday, 5th October 2001, 06:00 pm; Solved by 966555;Difficulty rating: 5%
"""


def multiples_of_3_and_5():
	n = 1000
	return sum(x for x in range(n) if (x % 3 == 0 or x % 5 == 0))


if __name__ == "__main__":
	print(multiples_of_3_and_5())
