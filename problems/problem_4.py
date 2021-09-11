"""
Link: [https://projecteuler.net/problem=4]

The following problem is taken from Project Euler.

LARGEST PALINDROME PRODUCT

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 Ã— 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Published on Friday, 16th November 2001, 06:00 pm; Solved by 489242;Difficulty rating: 5%
"""


# smallest 100 * 100
# largest 999 * 999
def largest_palindrome_project() -> int:
	largest_palindrome = 0
	smallest_3_digit = 100
	largest_3_digit = 999
	for i in range(smallest_3_digit, largest_3_digit + 1):
		for j in range(smallest_3_digit, largest_3_digit + 1):
			product = i * j
			if str(product) == str(product)[::-1]:
				if product > largest_palindrome:
					largest_palindrome = product
	return largest_palindrome


if __name__ == "__main__":
	print(largest_palindrome_project())
