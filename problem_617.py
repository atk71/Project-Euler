"""
Link: [https://projecteuler.net/problem=617]

The following problem is taken from Project Euler.

MIRROR POWER SEQUENCE

For two integers $n,e > 1$, we define a $(n,e)$-MPS (Mirror Power Sequence) to be an infinite sequence of integers $(a_i)_{i\ge 0}$ such that for all $i\ge 0$, $a_{i+1} = min(a_i^e,n-a_i^e)$ and $a_i > 1$. Examples of such sequences are the two $(18,2)$-MPS sequences made of alternating $2$ and $4$.
Note that even though such a sequence is uniquely determined by $n,e$ and $a_0$, for most values such a sequence does not exist. For example, no $(n,e)$-MPS exists for $n < 6$.
Define $C(n)$ to be the number of $(n,e)$-MPS for some $e$, and $\displaystyle D(N) = \sum_{n=2}^N {C(n)}$.
You are given that $D(10) = 2$, $D(100) = 21$, $D(1000) = 69$, $D(10^6) = 1303$ and $D(10^{12}) = 1014800$.
Find $D(10^{18})$.

Published on Saturday, 30th December 2017, 04:00 pm; Solved by 355;Difficulty rating: 40%
"""


def problem_617():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_617())