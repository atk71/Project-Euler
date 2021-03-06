"""
Link: [https://projecteuler.net/problem=57]

The following problem is taken from Project Euler.

SQUARE ROOT CONVERGENTS

It is possible to show that the square root of two can be expressed as an infinite continued fraction.
$\sqrt 2 =1+ \frac 1 {2+ \frac 1 {2 +\frac 1 {2+ \dots}}}$
By expanding this for the first four iterations, we get:
$1 + \frac 1 2 = \frac  32 = 1.5$
$1 + \frac 1 {2 + \frac 1 2} = \frac 7 5 = 1.4$
$1 + \frac 1 {2 + \frac 1 {2+\frac 1 2}} = \frac {17}{12} = 1.41666 \dots$
$1 + \frac 1 {2 + \frac 1 {2+\frac 1 {2+\frac 1 2}}} = \frac {41}{29} = 1.41379 \dots$
The next three expansions are $\frac {99}{70}$, $\frac {239}{169}$, and $\frac {577}{408}$, but the eighth expansion, $\frac {1393}{985}$, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

Published on Friday, 21st November 2003, 06:00 pm; Solved by 41528;Difficulty rating: 5%
"""


def problem_57():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_57())