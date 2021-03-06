"""
Link: [https://projecteuler.net/problem=554]

The following problem is taken from Project Euler.

CENTAURS ON A CHESS BOARD

On a chess board, a centaur moves like a king or a knight. The diagram below shows the valid moves of a centaur (represented by an inverted king) on an 8x8 board.
It can be shown that at most n2 non-attacking centaurs can be placed on a board of size 2n×2n.
Let C(n) be the number of ways to place n2 centaurs on a 2n×2n board so that no centaur attacks another directly.
For example C(1) = 4, C(2) = 25, C(10) = 1477721.
Let Fi be the ith Fibonacci number defined as F1 = F2 = 1 and Fi = Fi-1 + Fi-2 for i > 2.
Find $\displaystyle \left( \sum_{i=2}^{90} C(F_i) \right) \text{mod } (10^8+7)$.

Published on Sunday, 3rd April 2016, 01:00 am; Solved by 211;Difficulty rating: 80%
"""


def problem_554():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_554())