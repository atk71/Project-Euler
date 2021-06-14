"""
The following problem is taken from Project Euler.

AN ENORMOUS FACTORIAL


For any prime p the number N(p,q) is defined by
N(p,q) = ∑n=0 to q Tn*pn with Tn generated by the following random number generator:

S0 = 290797
Sn+1 = Sn2 mod 50515093
Tn = Sn mod p


Let Nfac(p,q) be the factorial of N(p,q).
Let NF(p,q) be the number of factors p in Nfac(p,q).


You are given that NF(3,10000) mod 320=624955285.


Find NF(61,107) mod 6110

Published on Saturday, 17th April 2010, 01:00 pm; Solved by 1561;Difficulty rating: 35%
"""


def problem_288():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_288())