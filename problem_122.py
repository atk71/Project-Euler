"""
The following problem is taken from Project Euler.

EFFICIENT EXPONENTIATION

The most naive way of computing n15 requires fourteen multiplications:
n × n × ... × n = n15
But using a "binary" method you can compute it in six multiplications:
n × n = n2n2 × n2 = n4n4 × n4 = n8n8 × n4 = n12n12 × n2 = n14n14 × n = n15
However it is yet possible to compute it in only five multiplications:
n × n = n2n2 × n = n3n3 × n3 = n6n6 × n6 = n12n12 × n3 = n15
We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.
For 1 ≤ k ≤ 200, find ∑ m(k).

Published on Friday, 2nd June 2006, 06:00 pm; Solved by 7565;Difficulty rating: 40%
"""


def problem_122():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_122())