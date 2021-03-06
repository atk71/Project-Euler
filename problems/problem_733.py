"""
Link: [https://projecteuler.net/problem=733]

The following problem is taken from Project Euler.

ASCENDING SUBSEQUENCES


Let $a_i$ be the sequence defined by $a_i=153^i \bmod 10\,000\,019$ for $i \ge 1$.
The first terms of $a_i$ are:
$153, 23409, 3581577, 7980255, 976697, 9434375, \dots$


Consider the subsequences consisting of 4 terms in ascending order. For the part of the sequence shown above, these are:
$153, 23409, 3581577, 7980255$
$153, 23409, 3581577, 9434375$
$153, 23409, 7980255, 9434375$
$153, 23409, 976697, 9434375$
$153, 3581577, 7980255, 9434375$ and
$23409, 3581577, 7980255, 9434375$.


Define $S(n)$ to be the sum of the terms for all such subsequences within the first $n$ terms of $a_i$. Thus $S(6)=94513710$.
You are given that $S(100)=4465488724217$.


Find $S(10^6)$ modulo $1\,000\,000\,007$.


Published on Saturday, 7th November 2020, 04:00 pm; Solved by 327;Difficulty rating: 25%
"""


def problem_733():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_733())