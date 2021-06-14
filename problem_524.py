"""
The following problem is taken from Project Euler.

FIRST SORT II

Consider the following algorithm for sorting a list:
For example, the list { 4 1 3 2 } is sorted as follows:
Let F(L) be the number of times step 2a is executed to sort list L. For example, F({ 4 1 3 2 }) = 5.
We can list all permutations P of the integers {1, 2, ..., n} in lexicographical order, and assign to each permutation an index In(P) from 1 to n! corresponding to its position in the list.


Let Q(n, k) = min(In(P)) for F(P) = k, the index of the first permutation requiring exactly k steps to sort with First Sort. If there is no permutation for which F(P) = k, then Q(n, k) is undefined.
For n = 4 we have:

Let R(k) = min(Q(n, k)) over all n for which Q(n, k) is defined.
Find R(1212).

Published on Sunday, 6th September 2015, 07:00 am; Solved by 197;Difficulty rating: 75%
"""


def problem_524():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_524())