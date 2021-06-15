"""
The following problem is taken from Project Euler.

BOZO SORT


Bozo sort, not to be confused with the slightly less efficient bogo sort, consists out of checking if the input sequence is sorted and if not swapping randomly two elements. This is repeated until eventually the sequence is sorted.


If we consider all permutations of the first 4 natural numbers as input the expectation value of the number of swaps, averaged over all 4! input sequences is 24.75.
The already sorted sequence takes 0 steps. 


In this problem we consider the following variant on bozo sort.
If the sequence is not in order we pick three elements at random and shuffle these three elements randomly.
All 3!=6 permutations of those three elements are equally likely. 
The already sorted sequence will take 0 steps.
If we consider all permutations of the first 4 natural numbers as input the expectation value of the number of shuffles, averaged over all 4! input sequences is 27.5. 
Consider as input sequences the permutations of the first 11 natural numbers.
Averaged over all 11! input sequences, what is the expected number of shuffles this sorting algorithm will perform?


Give your answer rounded to the nearest integer.


Published on Saturday, 14th January 2012, 10:00 pm; Solved by 471;Difficulty rating: 55%
"""


def problem_367():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_367())