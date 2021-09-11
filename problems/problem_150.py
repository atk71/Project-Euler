"""
Link: [https://projecteuler.net/problem=150]

The following problem is taken from Project Euler.

SEARCHING A TRIANGULAR ARRAY FOR A SUB-TRIANGLE HAVING MINIMUM-SUM

In a triangular array of positive and negative integers, we wish to find a sub-triangle such that the sum of the numbers it contains is the smallest possible.
In the example below, it can be easily verified that the marked triangle satisfies this condition having a sum of âˆ’42.
We wish to make such a triangular array with one thousand rows, so we generate 500500 pseudo-random numbers sk in the range Â±219, using a type of random number generator (known as a Linear Congruential Generator) as follows:
t := 0

for k = 1 up to k = 500500:

Â  Â  t := (615949*t + 797807) modulo 220
Â  Â  sk := tâˆ’219
Thus: s1 = 273519, s2 = âˆ’153582, s3 = 450905 etc
Our triangular array is then formed using the pseudo-random numbers thus:
Sub-triangles can start at any element of the array and extend down as far as we like (taking-in the two elements directly below it from the next row, the three elements directly below from the row after that, and so on).

The "sum of a sub-triangle" is defined as the sum of all the elements it contains.

Find the smallest possible sub-triangle sum.

Published on Friday, 13th April 2007, 10:00 pm; Solved by 3813;Difficulty rating: 55%
"""


def problem_150():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_150())