"""
Link: [https://projecteuler.net/problem=74]

The following problem is taken from Project Euler.

DIGIT FACTORIAL CHAINS

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145
Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
169 â†’ 363601 â†’ 1454 â†’ 169
871 â†’ 45361 â†’ 871
872 â†’ 45362 â†’ 872
It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
69 â†’ 363600 â†’ 1454 â†’ 169 â†’ 363601 (â†’ 1454)
78 â†’ 45360 â†’ 871 â†’ 45361 (â†’ 871)
540 â†’ 145 (â†’ 145)
Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

Published on Friday, 16th July 2004, 06:00 pm; Solved by 26526;Difficulty rating: 15%
"""


def problem_74():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_74())