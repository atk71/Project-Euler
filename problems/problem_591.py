"""
Link: [https://projecteuler.net/problem=591]

The following problem is taken from Project Euler.

BEST APPROXIMATIONS BY QUADRATIC INTEGERS

Given a non-square integer $d$, any real $x$ can be approximated arbitrarily close by quadratic integers $a+b\sqrt{d}$, where $a,b$ are integers. For example, the following inequalities approximate $\pi$ with precision $10^{-13}$:
$$4375636191520\sqrt{2}-6188084046055 < \pi < 721133315582\sqrt{2}-1019836515172 $$ 
We call $BQA_d(x,n)$ the quadratic integer closest to $x$ with the absolute values of $a,b$ not exceeding $n$. We also define the integral part of a quadratic integer as $I_d(a+b\sqrt{d}) = a$.
You are given that:
Find the sum of $|I_d(BQA_d(\pi,10^{13}))|$ for all  non-square positive integers less than 100.

Published on Saturday, 18th February 2017, 01:00 pm; Solved by 172;Difficulty rating: 95%
"""


def problem_591():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_591())