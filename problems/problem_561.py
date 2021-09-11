"""
Link: [https://projecteuler.net/problem=561]

The following problem is taken from Project Euler.

DIVISOR PAIRS


Let $S(n)$ be the number of pairs $(a,b)$ of distinct divisors of $n$ such that $a$ divides $b$.
For $n=6$ we get the following pairs: $(1,2), (1,3), (1,6),( 2,6)$ and $(3,6)$. So $S(6)=5$.
Let $p_m\#$ be the product of the first $m$ prime numbers,  so $p_2\# = 2*3 = 6$.
Let $E(m, n)$ be the highest integer $k$ such that $2^k$ divides $S((p_m\#)^n)$.
$E(2,1) = 0$ since $2^0$ is the highest power of 2 that divides S(6)=5.
Let $Q(n)=\sum_{i=1}^{n} E(904961, i)$
$Q(8)=2714886$.


Evaluate $Q(10^{12})$. 


Published on Saturday, 21st May 2016, 10:00 pm; Solved by 686;Difficulty rating: 30%
"""


def problem_561():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_561())