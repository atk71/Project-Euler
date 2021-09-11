"""
Link: [https://projecteuler.net/problem=16]

The following problem is taken from Project Euler.

POWER DIGIT SUM

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

Published on Friday, 3rd May 2002, 06:00 pm; Solved by 230720;Difficulty rating: 5%
"""


def sum_digits(target: int) -> int:
	number_of_digits = len(str(target))
	result = 0
	for i in range(number_of_digits):
		result += target % 10
		target //= 10
	return result


def power_digit_sum() -> int:
	answer = sum_digits(pow(2, 1000))
	return answer


if __name__ == "__main__":
	print(power_digit_sum())
