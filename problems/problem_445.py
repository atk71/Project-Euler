"""
Link: [https://projecteuler.net/problem=445]

The following problem is taken from Project Euler.

RETRACTIONS A


For every integer $n>1$, the family of functions $f_{n,a,b}$ is defined 
by  
$f_{n,a,b}(x)\equiv a x + b \mod n\,\,\, $ for $a,b,x$ integer and  $0< a <n, 0 \le b < n,0 \le x < n$. 

We will call $f_{n,a,b}$ a retraction if $\,\,\, f_{n,a,b}(f_{n,a,b}(x)) \equiv f_{n,a,b}(x) \mod n \,\,\,$ for every $0 \le x < n$.
Let $R(n)$ be the number of retractions for $n$.


You are given that
$\displaystyle \sum_{k=1}^{99\,999} R(\binom {100\,000} k)  \equiv 628701600 \mod 1\,000\,000\,007$.
 
Find $\displaystyle \sum_{k=1}^{9\,999\,999} R(\binom {10\,000\,000} k)$.
Give your answer modulo $1\,000\,000\,007$.


Published on Saturday, 16th November 2013, 10:00 pm; Solved by 345;Difficulty rating: 50%
"""


def problem_445():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_445())