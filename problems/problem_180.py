"""
Link: [https://projecteuler.net/problem=180]

The following problem is taken from Project Euler.

RATIONAL ZEROS OF A FUNCTION OF THREE VARIABLES

For any integer n, consider the three functions
f1,n(x,y,z) = xn+1 + yn+1 âˆ’ zn+1f2,n(x,y,z) = (xy + yz + zx)*(xn-1 + yn-1 âˆ’ zn-1)f3,n(x,y,z) = xyz*(xn-2 + yn-2 âˆ’ zn-2)
and their combination
fn(x,y,z) = f1,n(x,y,z) + f2,n(x,y,z) âˆ’ f3,n(x,y,z)
We call (x,y,z) a golden triple of order k if x, y, and z are all rational numbers of the form a / b with
0 < a < b â‰¤ k and there is (at least) one integer n, so that fn(x,y,z) = 0.
Let s(x,y,z) = x + y + z.
Let t = u / v be the sum of all distinct s(x,y,z) for all golden triples (x,y,z) of order 35. All the s(x,y,z) and t  must be in reduced form.
Find u + v.

Published on Saturday, 2nd February 2008, 09:00 am; Solved by 1495;Difficulty rating: 75%
"""


def problem_180():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_180())