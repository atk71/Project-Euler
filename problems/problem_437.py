"""
Link: [https://projecteuler.net/problem=437]

The following problem is taken from Project Euler.

FIBONACCI PRIMITIVE ROOTS


When we calculate 8n modulo 11 for n=0 to 9 we get: 1, 8, 9, 6, 4, 10, 3, 2, 5, 7.
As we see all possible values from 1 to 10 occur. So 8 is a primitive root of 11.
But there is more:
If we take a closer look we see:
1+8=9
8+9=17≡6 mod 11
9+6=15≡4 mod 11
6+4=10
4+10=14≡3 mod 11
10+3=13≡2 mod 11
3+2=5
2+5=7
5+7=12≡1 mod 11.


Published on Saturday, 21st September 2013, 10:00 pm; Solved by 724;Difficulty rating: 35%
"""


def problem_437():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_437())