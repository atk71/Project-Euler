"""
Link: [https://projecteuler.net/problem=278]

The following problem is taken from Project Euler.

LINEAR COMBINATIONS OF SEMIPRIMES


Given the values of integers $1 < a_1 < a_2 < \dots < a_n$, consider the linear combination
$q_1 a_1+q_2 a_2 + \dots + q_n a_n=b$, using only integer values $q_k \ge 0$. 


Note that for a given set of $a_k$, it may be that not all values of $b$ are possible.
For instance, if $a_1=5$ and $a_2=7$, there are no $q_1 \ge 0$ and $q_2 \ge 0$ such that $b$ could be 
$1, 2, 3, 4, 6, 8, 9, 11, 13, 16, 18$ or $23$.

In fact, $23$ is the largest impossible value of $b$ for $a_1=5$ and $a_2=7$. We therefore call $f(5, 7) = 23$. Similarly, it can be shown that $f(6, 10, 15)=29$ and $f(14, 22, 77) = 195$.


Find $\displaystyle \sum f( p\, q,p \, r, q \, r)$, where $p$, $q$ and $r$ are prime numbers and $p < q < r < 5000$.


Published on Saturday, 13th February 2010, 05:00 am; Solved by 987;Difficulty rating: 50%
"""


def problem_278():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_278())