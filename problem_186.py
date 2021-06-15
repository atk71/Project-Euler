"""
Link: [https://projecteuler.net/problem=186]

The following problem is taken from Project Euler.

CONNECTEDNESS OF A NETWORK

Here are the records from a busy telephone system with one million users:
The telephone number of the caller and the called number in record n are Caller(n) = S2n-1 and Called(n) = S2n where S1,2,3,... come from the "Lagged Fibonacci Generator":
For 1 â‰¤ k â‰¤ 55, Sk = [100003 - 200003k + 300007k3] (modulo 1000000)
For 56 â‰¤ k, Sk = [Sk-24 + Sk-55] (modulo 1000000)
If Caller(n) = Called(n) then the user is assumed to have misdialled and the call fails; otherwise the call is successful.
From the start of the records, we say that any pair of users X and Y are friends if X calls Y or vice-versa. Similarly, X is a friend of a friend of Z if X is a friend of Y and Y is a friend of Z; and so on for longer chains.
The Prime Minister's phone number is 524287. After how many successful calls, not counting misdials, will 99% of the users (including the PM) be a friend, or a friend of a friend etc., of the Prime Minister?

Published on Saturday, 15th March 2008, 05:00 am; Solved by 2721;Difficulty rating: 60%
"""


def problem_186():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_186())