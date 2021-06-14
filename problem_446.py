"""
The following problem is taken from Project Euler.

RETRACTIONS B


For every integer $n>1$, the family of functions $f_{n,a,b}$ is defined 
by  
$f_{n,a,b}(x)\equiv a x + b \mod n\,\,\, $ for $a,b,x$ integer and  $0< a <n, 0 \le b < n,0 \le x < n$. 

We will call $f_{n,a,b}$ a retraction if $\,\,\, f_{n,a,b}(f_{n,a,b}(x)) \equiv f_{n,a,b}(x) \mod n \,\,\,$ for every $0 \le x < n$.
Let $R(n)$ be the number of retractions for $n$.


$\displaystyle F(N)=\sum_{n=1}^NR(n^4+4)$.  
$F(1024)=77532377300600$.

Find $F(10^7)$.
Give your answer modulo $1\,000\,000\,007$.


Published on Saturday, 16th November 2013, 10:00 pm; Solved by 324;Difficulty rating: 60%
"""


def problem_446():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_446())