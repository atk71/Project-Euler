"""
Link: [https://projecteuler.net/problem=721]

The following problem is taken from Project Euler.

HIGH POWERS OF IRRATIONAL NUMBERS


Given is the function $f(a,n)=\lfloor{(\lceil{\sqrt{a}\:\rceil}+\sqrt{a}\:)^n}\rfloor$.
$\lfloor{.}\rfloor$ denotes the floor function and $\lceil{.}\rceil$ denotes the ceiling function.
$f(5,2)=27$ and $f(5,5)=3935$.


$G(n) = \displaystyle \sum_{a=1}^n f(a, a^2).$
$G(1000) \text{ mod  } 999\,999\,937=163861845. $
Find $G(5\,000\,000).$ Give your answer modulo $999\,999\,937$.


Published on Sunday, 21st June 2020, 02:00 am; Solved by 328;Difficulty rating: 30%
"""


def problem_721():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_721())