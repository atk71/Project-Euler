"""
Link: [https://projecteuler.net/problem=713]

The following problem is taken from Project Euler.

TURÁN'S WATER HEATING SYSTEM


Turan has the electrical water heating system outside his house in a shed. The electrical system uses two fuses in series, one in the house and one in the shed. (Nowadays old fashioned fuses are often replaced with reusable mini circuit breakers, but Turan's system still uses old fashioned fuses.)
For the heating system to work both fuses must work.


Turan has $N$ fuses. He knows that $m$ of them are working and the rest are blown. However, he doesn't know which ones are blown. So he tries different combinations until the heating system turns on.
We denote by $T(N,m)$ the smallest number of tries required to ensure the heating system turns on.
$T(3,2)=3$ and $T(8,4)=7$.


Let $L(N)$ be the sum of all $T(N, m)$ for $2 \leq m \leq N$.
$L(10^3)=3281346$


Find $L(10^7)$.


Published on Sunday, 26th April 2020, 02:00 am; Solved by 524;Difficulty rating: 20%
"""


def problem_713():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_713())